from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UserAccount, UserProfile


class UserAccountSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'url',
            'username',
            'email',
        ]

class UserProfileSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'url',
            'user',
            'profile_picture',
            'first_name',
            'middle_name',
            'last_name',
            'display_name',
        ]