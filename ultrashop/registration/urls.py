from django.urls import path
from .views import EnterView, GetUserView, RegisterView

urlpatterns = [
    path('', GetUserView.as_view(), name='all-profiles'),
    path('reg/', RegisterView.as_view()),
    path('auth/', EnterView.as_view()),
]