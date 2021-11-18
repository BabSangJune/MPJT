from django.urls import path
from . import views


urlpatterns = [
    path('movie/',views.movie_list), # main page
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('movie/<int:movie_pk>/review/', views.create_review), #리뷰생성
    path('movie/review/<int:review_pk>/', views.review_detail),
    # 데이터 들고오기
    path('create_genre/', views.genre_get),
    path('create_movie/', views.movie_get),


]


# 1. 영화 전체목록(main page) : GET
# 2. 단일 영화목록(movie datail page) : GET