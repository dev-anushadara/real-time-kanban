from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrganizationViewSet,
    TenantViewSet,
    MembershipViewSet,
    BoardViewSet,
    ColumnViewSet,
    TaskViewSet,
    ActivityLogViewSet,
)

router = DefaultRouter()

router.register(r'organizations', OrganizationViewSet)
router.register(r'tenants', TenantViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'boards', BoardViewSet)
router.register(r'columns', ColumnViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'activity-logs', ActivityLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]