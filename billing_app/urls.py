from django.conf.urls import url
from billing_app import views

urlpatterns = [
    url(r'^billing/$', views.BillingList.as_view()),
    url(r'^billing/(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/$',
        views.BillingDetail.as_view()),
]