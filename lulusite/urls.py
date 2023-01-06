"""lulusite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('lulublog/', include('lulublog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from lulublog import views
from allauth.account.views import SignupView


# registration view class (from django-allauth applications set)

class RegistrationView(SignupView):
    template_name = 'registration/register.html'


urlpatterns = [
    path('admin/', admin.site.urls),  # lulusite project administration site url
    path('lulu_stories/', include('lulublog.urls')),  # lulublog app non-registration urls
    path('login/', auth_views.LoginView.as_view(), name='login'),  # lulublog account login url
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # lulublog account logout url
    path('register/', RegistrationView.as_view(), name="register_request"),  # lulublog account register url (from django-allauth applications set)
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password-change.html'),
         name='password_change_request'),  # lulublog account password change url
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password-change-done.html'),
         name='password_change_done'),  # lulublog account password change success url
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password-reset-form.html'),
         name='password_reset'),  # lulublog account password reset e-mail form url
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password-reset-done.html'),
         name='password_reset_done'),  # lulublog account password reset message url
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password-reset-confirm.html'),
         name='password_reset_confirm'),  # lulublog account password reset new password form url
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password-reset-complete.html'),
         name='password_reset_complete'),  # lulublog account password reset success message url
    path('accounts/', include('allauth.urls'))  # lulublog account registration messages urls (from django-allauth applications set)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
