from django.http import UnreadablePostError


def skip_unreadable_post(record):
    if record.exc_info:
        exc_type, exc_value = record.exc_info[:2]
        if isinstance(exc_value, UnreadablePostError):
            return False
    return True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'short': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'medium': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
        'long': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        },
        'full': {
            'format': 'asctime: %(asctime)-12s \n created: %(created)-12f \n filename: %(filename)-12s \n funcName: %(funcName)-12s \n levelname: %(levelname)-12s \n levelno: %(levelno)-12s \n lineno: %(lineno)-12d \n message: %(message)-12s \n module: %(module)-12s \n msecs: %(msecs)-12d \n name: %(name)-12s \n pathname: %(pathname)-12s \n process: %(process)-12d \n processName: %(processName)-12s \n relativeCreated: %(relativeCreated)-12d \n thread: %(thread)-12d \n threadName: %(threadName)-12s' # NOQA
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'DEBUG',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'short'
        },
        'console_critical': {
            'level': 'CRITICAL',
            'class': 'logging.StreamHandler',
            'formatter': 'long'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'medium',
            'filename': 'logs/debug.log'
        },
        'file_critical': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'formatter': 'full',
            'filename': 'logs/critical.log'
        },
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.django.raven_compat.handlers.SentryHandler',
        },
    },
    'filters': {
        'skip_unreadable_posts': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': skip_unreadable_post,
        },
        'special': {
            '()': 'app.logging_filters.SpecialFilter',
            # 'foo': 'bar',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': [
                'console',
                'file',
                'sentry',
                'mail_admins',
            ],
            # required to avoid double logging with root logger
            # 'propagate': False
        },
        'app': {
            'level': 'DEBUG',
            'handlers': [
                'console',
                'file',
            ],
            # Этим параметром регулируется возможность передачи сообщения другим логгерам.
            # Если оно установлено в False то дальше сообщение не пойдет.
            'propagate': True
        },
        'app.views': {
            'level': 'INFO',
            'handlers': [
                'console',
                'file',
            ],
            'propagate': True
        }
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
