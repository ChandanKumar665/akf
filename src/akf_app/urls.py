from django.urls import path
from akf_app import views
from akf_app.api.gpcontest import aggregate

urlpatterns = [
    path('index',views.show,name='index'),
    path('urlsubmit',views.url_submit,name='urlsubmit'),
    path('api/gpcontest/aggregate',aggregate.get_aggregate,name='aggregate'),
    path('api/gpcontest/index',views.show,name='index')
]