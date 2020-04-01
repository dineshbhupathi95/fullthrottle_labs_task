from rest_framework.generics import *
from .serializers import *
from rest_framework.response import Response

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()






