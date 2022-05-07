#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from simple_websocket_server import WebSocketServer, WebSocket
import base64, cv2
import numpy as np
import warnings

warnings.simplefilter("ignore", DeprecationWarning)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    """server = WebSocketServer('192.168.35.204', 8001, SimpleEcho)
    server.serve_forever()"""

class SimpleEcho(WebSocket):
    def handle(self):
        msg = self.data
        img = cv2.imdecode(np.fromstring(base64.b64decode(msg.split(',')[1]), np.uint8), cv2.IMREAD_COLOR)
        cv2.imshow('image', img)
        cv2.waitKey(1)

    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')


if __name__ == '__main__':
    main()



