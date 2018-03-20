import os

import boto3


class BotoS3Client(object):
    
    client_pool = {}
    
    def __new__(cls, config):
        """
        Reuse BotoS3Client Object to reduce init time
        """
        client_addr = "{}@{}:{}".format(
                config['AWS_DEFAULT_REGION'], 
                config['S3_BUCKET_NAME'], 
                config['S3_REPORT_URL']
        )

        if client_addr in cls.client_pool:
            return cls.client_pool[client_addr]
        else:
            client = super(BotoS3Client, cls).__new__(cls)
            client.__init__(config)
            cls.client_pool[client_addr] = client
            return client

    def __init__(self, config):
        self.REGION_NAME = config['AWS_DEFAULT_REGION']
        self.BUCKET_NAME = config['S3_BUCKET_NAME']
        self.S3_URL = config['S3_REPORT_URL']
        self.s3_obj = boto3.resource(
            's3',
            region_name=config["S3_REGION_CODE"],
            aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY']
        )

    def upload_to_s3(self, abs_file_path):
        """
        This is to be used in case we use the abs file path upload
        :param abs_file_path:
        :return:
        """
        if not os.path.isfile(abs_file_path):
            raise FileNotFoundError('Pdf file is not found')
        try:
            file_name = os.path.basename(abs_file_path)
            self.s3_obj.meta.client.upload_file(abs_file_path, self.BUCKET_NAME, file_name)
        except Exception as e:
            raise e
        return self.S3_URL + "/" + file_name
