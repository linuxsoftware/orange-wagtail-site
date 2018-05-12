from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@tm_6wd$(17$5%5f%ci&+&_6(#*a9=24e2@mxbej4136&8r)$)'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# LOGGING = {
#     'version': 1,
#
#     'disable_existing_loggers': True,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console':{
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': [],
#         }
#     },
#
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     },
# }

try:
    from .local import *
except ImportError:
    pass
