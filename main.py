import boto3
region = 'us-east-1'

def getting_list_of_functions():
    lambda_client = boto3.client('lambda', region_name=region)
    return lambda_client.list_functions()
    #print(response['Functions'])


def write_functions_to_file():
    f = open('list_of_functions.txt', 'w')
    f.close()
    with open("list_of_functions.txt", "w") as fl:
        for each in getting_list_of_functions()['Functions']:
            fl.write(each['FunctionName']+'\n')
        fl.close()



def create_s3_bucket(bn):
    s3_client = boto3.resource('s3', region_name=region)
    response = s3_client.create_bucket(
        Bucket=bn
    )

    print(response)
    return s3_client

def upload_file(bucket_name):
    #create_s3_bucket(bucket_name)
    write_functions_to_file()
    create_s3_bucket(bucket_name).Bucket(bucket_name).upload_file('list_of_functions.txt', 'list_of_functions.txt')


if __name__ == "__main__":
    bucket_name = input('Bucket name: ')
    upload_file(bucket_name)

