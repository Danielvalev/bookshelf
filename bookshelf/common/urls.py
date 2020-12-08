from django.urls import path

from common.views import landing_page, NoAccessView

urlpatterns = [
    path('', landing_page, name='index'),
    path('noaccess/', NoAccessView.as_view(), name='no access'),
]