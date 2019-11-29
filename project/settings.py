import os

from irekua_dev_settings.settings import *
from selia_templates.settings import *
from selia_forms.settings import *
from selia_registration.settings import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]


INSTALLED_APPS = (
    SELIA_REGISTRATION_APPS +
    SELIA_FORMS_APPS +
    SELIA_TEMPLATES_APPS +
    IREKUA_BASE_APPS
)
