from rest_framework import routers

from companies.views import CommerceViewSet, OrganizationViewSet

router = routers.DefaultRouter()

router.register(r'organizations', OrganizationViewSet)
router.register(r'commerces', CommerceViewSet)

urlpatterns = router.urls
