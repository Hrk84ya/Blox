"""
Development settings — extends base with DEBUG=True and relaxed security.
"""
from .base import *  # noqa: F401, F403

DEBUG = True

# Allow all hosts in development
ALLOWED_HOSTS = ["*"]

# CORS — allow all origins in development
CORS_ALLOW_ALL_ORIGINS = True
