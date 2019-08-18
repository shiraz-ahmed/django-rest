from django.urls import path,include
from .views import my_api,api_viewsets,userprofile_viewset
from rest_framework.routers  import DefaultRouter

router=DefaultRouter()
router.register('api_viewset',api_viewsets,base_name='api_viewset')
router.register('userprofile_apiview',userprofile_viewset)
#if you have a queryset in the modelview then dont use name here
# views.api_viewsets

urlpatterns = [

    path('view', my_api.as_view(),name='api'),
    path('', include(router.urls)),

]
