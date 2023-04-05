from django.urls import path
from .views import home, about, destinations, blog, contact
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('destinations/', destinations, name='destinations'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)