# flake8: noqa

# Formerly Python 2.7 diverted, so stored here
string_types = (str, bytes)
text_type = str
from urllib.parse import parse_qsl, urlparse, urlunparse
from urllib.request import urlopen


def setup_managers(sender):
    from .models.managers import money_manager

    default_manager_name = sender._meta.default_manager_name or "objects"
    for manager in filter(lambda m: m.name == default_manager_name, sender._meta.local_managers):
        money_manager(manager)
