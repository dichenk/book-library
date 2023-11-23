from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from .tasks import send_welcome_email
from rest_framework import status
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Access to the list of users is forbidden"}, status=status.HTTP_403_FORBIDDEN)

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email)
