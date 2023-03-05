from storages.backends.s3boto3 import S3BotoStorage

StaticRootS3BotoStorage = lambda: S3BotoStorage(location='static')
class MediaStorage(S3BotoStorage):
    location = 'media'
    file_overwrite = False

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        return url.replace('https://', 'http://')