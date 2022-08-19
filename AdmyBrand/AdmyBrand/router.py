from RestCrudApi.viewsets import FriendViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Friend', FriendViewset)
