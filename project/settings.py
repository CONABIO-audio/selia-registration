from irekua_dev_settings.settings import *
from selia_templates.settings import *
from selia_forms.settings import *
from selia_registration.settings import *


INSTALLED_APPS = (
    SELIA_REGISTRATION_APPS +
    SELIA_FORMS_APPS +
    SELIA_TEMPLATES_APPS +
    IREKUA_BASE_APPS
)
