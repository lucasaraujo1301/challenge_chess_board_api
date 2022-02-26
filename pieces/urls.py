from pieces.views import PieceViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'pieces', PieceViewSet)

urlpatterns = router.urls
