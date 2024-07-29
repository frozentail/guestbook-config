import boto3
import json

# Get S3 Session
def getResource(sts_connection) :
  acct_b = sts_connection.assume_role(
    RoleArn = 'arn:aws:iam::527449218003:role/AWS',
    RoleSessionName = "frozentail@kalmate.net_CLI"
  )
  
  ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
  SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
  SESSION_TOKEN = acct_b['Credentials']['SessionToken']
  
  session = boto3.resource(
    's3', 'ap-northeast-2',
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY,
    aws_session_token = SESSION_TOKEN
  )
  return session





if __name__ == "__main__":
  
  sts_connection = boto3.client('sts')


  s3 = getResource(sts_connection)
  while True:
      filename = str(input('\n S3에 업로드 할 yaml 파일 이름을 쓰시오 : \n'))
      if " " in filename:
        print('\n띄어쓰기 없이 쓰시오 : \n')
      else:
        break
  local_path = 'D:/DCO/Python/ssm/yaml/'
  object = s3.Object(
      bucket_name='awsdc-s3-shr-com-fileshare', 
      key=f'ssm/automation/yaml/{filename}'
  )
  
  with open(local_path+filename, 'rb') as file:
    object.put(Body=file)
