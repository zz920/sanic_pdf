class Default_Config():

    # AWS settings
    AWS_CONFIG = {
        'AWS_DEFAULT_REGION': '',
        'S3_BUCKET_NAME': '',
        'S3_REPORT_URL': '',
        'S3_REGION_CODE': '',
        'AWS_ACCESS_KEY_ID': '',
        'AWS_SECRET_ACCESS_KEY': ''
    }

    # Log settings
    LOG_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'loggers': {
            '': {
                'level': 'INFO',    
            },
        } 
    }
