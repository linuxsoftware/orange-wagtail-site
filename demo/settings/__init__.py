# settings/__init__.py

import os

ENV = os.getenv('DEMOENV', 'dev')

if ENV == 'dev':
    from .dev import *
elif ENV == 'prd':
    from .prd import *
