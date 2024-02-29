from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'account'

router = DefaultRouter()
router.register(r'', views.MyLoginView, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('42oauth', views.FtAuthView.as_view(), name="42oauth"),

    #테스트용
    path('devsignup', views.SignupView.as_view(), name="devsignup"),
    path('test', views.TestView.as_view(), name="test"),
    # profile
    path('user/profile-stats/', views.user_profile_stats, name='user-profile-stats'),
    # user 조회
    path('search/<str:username>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user-stats/<int:user_id>/', views.OtherUserProfileStatsView.as_view(), name='other-user-profile-stats'),
    # username 변경
    path('change-username/', views.change_username, name='change-username'),
    # user image 변경
    path('update-image/', views.UpdateUserImageView.as_view(), name='update-image'),
    # user password 변경
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
]
