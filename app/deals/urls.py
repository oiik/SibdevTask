from django.urls import path
from .views import DealsView
from .views import FileView

app_name = "deals"
urlpatterns = [
  path('deals/', DealsView.as_view()),
  path('upload/', FileView.as_view(), name='file-upload'),
]
