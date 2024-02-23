# settings.py

INSTALLED_APPS = [
    # other apps
    'paypal.standard.ipn',
]

# PayPal configurations
PAYPAL_TEST = True  # Set to False for production
PAYPAL_RECEIVER_EMAIL = 'sb-mgyus29596541@business.example.com'  # Your Sandbox Business email
PAYPAL_CLIENT_ID = 'ARmLuCBVNPUQhqiPTmLWUu...'
PAYPAL_SECRET_KEY = 'ARmLuCBVNPUQhqiPTmLWUu...'

# Add IPN URL for PayPal Instant Payment Notification
PAYPAL_NOTIFY_URL = 'https://sandbox.paypal.com'
################################

import environ

env = environ.Env()
environ.Env.read_env()  # Assuming you have .env file at the project root

PAYPAL_CLIENT_ID = env('ARmLuCBVNPUQhqiPTmLWUu...')
PAYPAL_SECRET = env('ARmLuCBVNPUQhqiPTmLWUu...')
PAYPAL_MODE = env('https://sandbox.paypal.com')  # sandbox or live