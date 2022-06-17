"""Me app"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MeConfig(AppConfig):
    """Me app config"""

    name = "resume.me"
    verbose_name = _("Me")
