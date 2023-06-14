from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_page),
    path('<uuid:movie_id>/', views.detail, name='detail'),
    path('<uuid:movie_id>/create/', views.createreview, name='createreview'),
    path('movies/', views.MovieList.as_view(), name='all'),
    path('movie/<uuid:pk>/detail/', views.MovieDetail.as_view(), name='movie'),
    path('movie/create/', views.MovieList.as_view(), name='movie_create'),
    path('movie/<uuid:pk>/update/', views.MovieDetail.as_view(), name='movie_update'), # noqa E501
    path('movie/<uuid:pk>/delete/', views.MovieDetail.as_view(), name='movie_delete'), # noqa E501
    path('home/', views.home, name='home'),
    path('review/<int:review_id>/', views.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete/', views.deletereview, name='deletereview'), # noqa E501
]
