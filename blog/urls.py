from django.urls import path
from .views import PostView, PostDetail, AddComments, AddLike, DisLike

urlpatterns = [
    path('', PostView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('review/<int:pk>/', AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes/', AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes/', DisLike.as_view(), name='del_likes'),
]
