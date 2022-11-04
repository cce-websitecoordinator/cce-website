from storages.backends.s3boto3 import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: S3BotoStorage(location='media')