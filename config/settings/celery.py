from config.env import env

CELERY_BROKER_URL = env("CELERY_BROKER_URL")


CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = True
