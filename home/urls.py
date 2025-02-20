from django.urls import path
from django.views.generic import TemplateView
from .views import about_view, contact_view


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about/', about_view, name='about'),
    path('about/', contact_view, name='contact' ),
]
