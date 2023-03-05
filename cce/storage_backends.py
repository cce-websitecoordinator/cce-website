from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

    def url(self, name, parameters=None, expire=None):
        url = super().url(name, parameters, expire)
        if self.custom_domain:
            url = url.replace('https://', 'http://')
        return url

    def get_available_name(self, name, max_length=None):
        return super().get_available_name(name, max_length)

    def _save(self, name, content):
        return super()._save(name, content)

    def exists(self, name):
        return super().exists(name)

    def size(self, name):
        return super().size(name)

    def modified_time(self, name):
        return super().modified_time(name)

    def accessed_time(self, name):
        return super().accessed_time(name)

    def created_time(self, name):
        return super().created_time(name)

    def get_valid_name(self, name):
        return super().get_valid_name(name)

    def get_available_overwrite_name(self, name):
        return super().get_available_overwrite_name(name)

    def get_content_type(self, name):
        return super().get_content_type(name)

    def get_object(self, name):
        # Use CloudFront URL for 'get' method
        if self.custom_domain:
            return self.bucket.meta.client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': self.bucket.name,
                    'Key': self._normalize_name(name),
                },
                ExpiresIn=self.presigned_url_expiry,
                HttpMethod='GET',
            )
        else:
            return super().get_object(name)

    def delete(self, name):
        return super().delete(name)

    def get_available_name(self, name, max_length=None):
        return super().get_available_name(name, max_length)