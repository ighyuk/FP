import base64
from urllib.request import urlretrieve
import numpy as np
from django.shortcuts import render, get_object_or_404
from simple_websocket_server import WebSocketServer, WebSocket

from .models import User
from django.core.paginator import Paginator

from django.views.decorators import gzip
from django.http import  StreamingHttpResponse
import cv2
import threading

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass
# Create your views here.

from django.http import HttpResponse


def chat(request):
  return render(request, 'FP/chat.html')
  
def room(request, room_name):
  return render(request, 'FP/room.html', {
    'room_name': room_name
    })

def index(request):
    """
    FP 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지

    # 조회
    user_list = User.objects.order_by('-user_id')

    # 페이징처리
    paginator = Paginator(user_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'user_list': page_obj}
    return render(request, 'FP/user_list.html', context)

def detail(request, user_id):
    """
    FP 내용 출력
    """
    user = get_object_or_404(User, pk=user_id)
    context = {'user' : user}
    return render(request, 'FP/user_detail.html', context)

def management(request):
    """
    FP 내용 출력
    """
    """server = WebSocketServer('192.168.35.204', 8001, SimpleEcho)
    server.serve_forever()"""
    return render(request, 'FP/management.html')

def visitRecord(request):
    """
    FP 내용 출력
    """

    return render(request, 'FP/visitRecord.html')
