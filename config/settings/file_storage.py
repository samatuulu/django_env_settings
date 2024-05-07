from config.env import env


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {}
    },
}

AW_S3_ACCESS_KEY_ID = env("AW_S3_ACCESS_KEY_ID")
AW_S3_SECRET_ACCESS_KEY = env("AW_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
