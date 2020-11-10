# path 함수를 사용하기 위해서 import
from django.urls import path

# posts에 있는 views
from . import views

app_name = 'posts'
# posts/ 제외
urlpatterns = [
    # url pattern, view 함수, 별칭
    # posts의 main 페이지
    path('', views.index, name='index'),
    # 항상 맨 끝에 '/'를 붙여줘야 한다 (자동으로 브라우저가 끝에 '/'를 붙여준다)
    path('<int:post_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/like/', views.like, name='like'),
]