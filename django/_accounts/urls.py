from django.urls import path, include 
from allauth.account import views, urls, forms
from django.contrib.auth import views, urls, forms
from .custom_views import *


urlpatterns = [
    
    path('register/',           register_view, name="register_view"),
    path('login/',              login_view,    name="login_view"),
    path('logout/',             logout_view,   name="logout_view"),



    # include django.contrib.auth.urls
    # path('login/',                  LoginView.as_view(),                 name='login'),
    # path('logout/',                 LogoutView.as_view(),                name='logout'),
    # path('password_change/',        PasswordChangeView.as_view(),        name='password_change'),
    # path('password_change/done/',   PasswordChangeDoneView.as_view(),    name='password_change_done'),
    # path('password_reset/',         PasswordResetView.as_view(),         name='password_reset'),
    # path('password_reset/done/',    PasswordResetDoneView.as_view(),     name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),  name='password_reset_confirm'),
    # path('reset/done/',             PasswordResetCompleteView.as_view(), name='password_reset_complete'),




    # include allauth.urls
    # url(r"^signup/$", views.signup, name="account_signup"),
    # url(r"^login/$",  views.login, name="account_login"),
    # url(r"^logout/$", views.logout, name="account_logout"),
    # url(r"^password/change/$", views.password_change,
    #     name="account_change_password"),
    # url(r"^password/set/$",    views.password_set, 
    #     name="account_set_password"),
    # url(r"^inactive/$",      views.account_inactive, name="account_inactive"),
    # # E-mail
    # url(r"^email/$",         views.email, name="account_email"),
    # url(r"^confirm-email/$", 
    #     views.email_verification_sent,
    #     name="account_email_verification_sent"),
    # url(r"^confirm-email/(?P<key>[-:\w]+)/$", 
    #     views.confirm_email,
    #     name="account_confirm_email"),
    # # password reset
    # url(r"^password/reset/$",      
    #     views.password_reset,
    #     name="account_reset_password"),
    # url(r"^password/reset/done/$", 
    #     views.password_reset_done,
    #     name="account_reset_password_done"),
    # url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
    #     views.password_reset_from_key,
    #     name="account_reset_password_from_key"),
    # url(r"^password/reset/key/done/$", 
    #     views.password_reset_from_key_done,
    #     name="account_reset_password_from_key_done"),
]