"""
Core App
"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Config Class for the Core App"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
