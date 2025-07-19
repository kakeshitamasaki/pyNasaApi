from django.urls import path, include
from . import views


from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'api/posts', views.PostViewSet)


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # APIルーターを追加
    path('', include(router.urls)),
]