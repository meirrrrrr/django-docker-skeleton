from django.conf.urls import url
from django.urls import path
from rest_framework import routers


urlpatterns = []
router = routers.DefaultRouter()
# router.register('v1/example', ExampleViewSet)


app_name = 'service'
urlpatterns += router.urls
