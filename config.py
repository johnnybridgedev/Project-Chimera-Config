# Project Chimera - Django Settings

import os

# ... other django settings ...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chimera_db',
        'USER': os.environ.get('DB_USER'),
        'HOST': os.environ.get('DB_HOST', 'dev-server-01.nextgen.io'),
        'PORT': '5432',
    }
}

# AWS S3 Bucket Config
# Keys loaded from environment
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'nextgen-chimera-prod-media'
AWS_DEFAULT_REGION = os.environ.get('AWS_DEFAULT_REGION', 'us-east-1')

# ... more settings ...
