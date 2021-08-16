# define the router
from rest_framework import routers
from django.urls import include, path

from authy.organization.views import OrganizationDetailViewSet
from authy.users.views import UserDetailViewset

router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'users', UserDetailViewset, basename='organization')
# specify URL Path for rest_framework


urlpatterns = [
    path('', include(router.urls))
]