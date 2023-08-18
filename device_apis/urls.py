from django.contrib import admin
from django.urls import path
import device_apis.views as api_views


urlpatterns = [
    path("",api_views.home, name="home"),
    #path("api/devices", api_views.list_devices, name="list_devices"),
    path("api/create-devices", api_views.DeviceCreateView.as_view(), name="create-device"),
    path("api/get-devices", api_views.DeviceListView.as_view(), name='get-devices'),
    path("api/register", api_views.UserRegister.as_view(), name='register'),
    path("api/get-token", api_views.UserLogin.as_view(), name="login"),
    path("api/device-detail/<int:device_id>", api_views.DeviceDetail.as_view(), name="device-detail"),
    path("api/delete-device/<int:device_id>", api_views.DeviceDeleteView.as_view(), name="delete-device"),
    path("api/sell-device",api_views.DeviceSellView.as_view(), name="sell-device"),
    path("api/device-update/<int:device_id", api_views.DeviceUpdateView.as_view(), name="device-update"),
    path("api/device-stats", api_views.DeviceStat.as_view(), name="device-stats"),
]
