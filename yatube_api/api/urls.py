from django.urls import include, path
from rest_framework.routers import SimpleRouter
from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowApiView


router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path(
        'posts/<int:post_pk>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments-list',
    ),
    path(
        'posts/<int:post_pk>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='post-comments-detail',
    ),
    path('', include('djoser.urls.jwt')),
    path('follow/', FollowApiView.as_view()),
]
