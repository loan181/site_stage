
from django.urls import path
from django.conf.urls.static import static
from django.views.generic import RedirectView


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('concept/<str:concept_name>', views.concept, name='concept'),
    path('test', views.test, name='test'),
    path('scratch', views.scratchOffline, name='scratchOffline'),
    path('slide', views.slide, name='slide'),
    path('project/<str:project_name>', views.project, name='project'),
    path('locale/<str:fileName>', views.locale),
]