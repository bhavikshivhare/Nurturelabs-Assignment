from django.urls import path
from django.urls.resolvers import URLPattern
from application.views import CreateAdvisorAPIView,RegisterAPIView,ListAdvisorAPIView,BookingCallAPIView

booking_call = BookingCallAPIView.as_view({
    'post': 'create',
})


urlpatterns = [
    path("advisor/",CreateAdvisorAPIView.as_view(),name="add_advisor"),
    path("user/<int:pk>/advisor",ListAdvisorAPIView.as_view(),name="list_advisor"),
    path('user/register/', RegisterAPIView.as_view(), name='register'),
    path("user/<int:pk>/advisor/<int:advisor_pk>",booking_call,name="Booking"),
    # path("user/advisor/<int:pk>",AdverisorRetrive.as_view(),name="retrive_advisor"),
]
