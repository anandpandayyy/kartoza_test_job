from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from app.forms import UserForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',
         RegistrationView.as_view(
             form_class=UserForm
         ),
         name='django_registration_register',
         ),
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]
