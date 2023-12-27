from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.VoteView.as_view(), name="vote"),
    path("new/", views.PollNewView.as_view(), name="poll_new"),
    path('<int:pk>/edit/', views.PollEditView.as_view(), name='poll_edit'),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("register", views.AccountRegisterView.as_view(), name="register"),
    path("activate/<uidb64>/<token>", views.AccountActivationView.as_view(), name="activate"),
]