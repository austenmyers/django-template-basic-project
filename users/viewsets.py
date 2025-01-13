from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import UserAccount, UserProfile
from .serializers import UserAccountSerializer, UserProfileSerializer


class UserAccountViewSet(ModelViewSet):
    queryset = UserAccount.objects.all().order_by('-date_joined')
    serializer_class = UserAccountSerializer
    permission_classes = [IsAdminUser]

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all().order_by('user')
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]