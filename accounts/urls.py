from django.urls import path
from django.conf.urls import url
from accounts import views as account_views
from address.views import load_district, load_upazila


urlpatterns = [
    path('signup', account_views.signup_view, name='signup'),
    path('login/', account_views.login_view, name='login'),
    path('logout/', account_views.logout_view, name='logout'),
    url('profile/(?P<profile>\w+)$', account_views.profile_view, name='profile'),
    path('load-district/', load_district, name='load_district'),
    path('load-upazila/', load_upazila, name='load_upazila'),
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
