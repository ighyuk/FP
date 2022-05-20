"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")


from channels.auth import AuthMiddlewareStack #추가
from channels.routing import ProtocolTypeRouter, URLRouter #URLRouter 추가
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import FP.routing # chat import
from django.urls import path


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack( # 추가
        URLRouter(
            FP.routing.websocket_urlpatterns
        )
    ),
})