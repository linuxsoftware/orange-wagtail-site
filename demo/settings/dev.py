from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@tm_6wd$(17$5%5f%ci&+&_6(#*a9=24e2@mxbej4136&8r)$)'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
