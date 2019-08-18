from django.urls import path,include
from .views import my_api,api_viewsets
from rest_framework.routers  import DefaultRouter

router=DefaultRouter()
router.register('api_viewset',api_viewsets,base_name='api_viewset')
# views.api_viewsets

urlpatterns = [

    path('view', my_api.as_view(),name='api'),
    path('', include(router.urls)),
]
