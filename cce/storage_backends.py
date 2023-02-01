from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        return url.replace('https://', 'http://')