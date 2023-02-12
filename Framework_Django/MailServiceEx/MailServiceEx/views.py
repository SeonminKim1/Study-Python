from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class mailView(APIView):
    def get(self, request):
        send_mail('메일 제목입니당.', '메일 메시지 입니당', 'moagudok1@gmail.com', ['yubi5050@naver.com'], fail_silently=False)
        return Response({'detail': '메일 전송완료'}, status=status.HTTP_200_OK)