SELIA_REGISTRATION_APPS = [
    'selia_registration',
]

LOGIN_URL = '/registration/accounts/login/'

# Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '....@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'