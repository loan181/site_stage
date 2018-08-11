
from django.urls import path
from django.conf.urls.static import static
from django.views.generic import RedirectView


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('concept/<str:concept_name>', views.concept, name='concept'),
    path('test', views.test, name='test'),
    path('scratch', views.scratch, name='scratch'),
    path('locale/<str:fileName>', views.locale),
]