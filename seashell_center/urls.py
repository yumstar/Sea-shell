from django.urls import path
from . import views

urlpatterns = [
    path('centerUser/register', views.CenterUserRegister.as_view(), name='register'),
    path('centerUser/signin', views.CenterUserSignin.as_view(), name='signin'),
    path('centerUser/signout', views.CenterUserSignout.as_view(), name='signout'),
    path('centerUser/view', views.CenterUserView.as_view(), name='view'),
    path('tag/', views.TagListView.as_view(), name='tags'),
    path('tag/tags/<int:pk>', views.TagView.as_view(), name='tag'),
    path('message/', views.MessageListView.as_view(), name='messages'),
    path('message/message/<int:pk>', views.MessageView.as_view(), name='message'),
    path('day-experience/', views.DayExperienceListView.as_view(), name='day-experiences'),
    path('day-experience/day-experience/<int:pk>', views.DayExperienceView.as_view(), name='day-experience')
]