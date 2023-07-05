from django.urls import path,include
from .views import *

from rest_framework import routers
router = routers.SimpleRouter(trailing_slash=False)
router.register(r'tab', TabViewSet)
router.register(r'column', ColumnViewSet)
router.register(r'param', ParamViewSet)
router.register(r'record', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reorder', ReorderColumns.as_view()),
]
