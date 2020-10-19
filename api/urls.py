from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet, ChangingStatusViewSet, ReminderViewSet


router = DefaultRouter()
router.register('users', UserViewSet)
router.register('tasks', TaskViewSet)
router.register('changing_status', ChangingStatusViewSet)
router.register('reminders', ReminderViewSet)

urlpatterns = router.urls
