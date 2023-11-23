from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from .tasks import send_welcome_email


class UserList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.email)
