from django.urls import path
from .views import PollListView, PollDetailView, VoteCreateView

urlpatterns = [
    path("", PollListView.as_view()),
    path("<int:pk>/", PollDetailView.as_view()),
    path("vote/", VoteCreateView.as_view()),
]
