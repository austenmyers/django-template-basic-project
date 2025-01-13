from rest_framework.routers import DefaultRouter
from users.viewsets import UserAccountViewSet, UserProfileViewSet


router = DefaultRouter()
router.register(r'user_accounts', UserAccountViewSet)
router.register(r'user_profiles', UserProfileViewSet)