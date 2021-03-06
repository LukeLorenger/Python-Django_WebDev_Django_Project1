from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)
from . import views # Imports views.py module

urlpatterns = [
	# Path for home route
    path('', PostListView.as_view(), name='blog-home'), 
    # User Post path
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # Primary key of post we want to view, pk grabbing value from url, using in view function  
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    # URL for Create new post
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    # Update Path, this allows for posts to be updated
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # Delete Path
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  
    # Path for about route
    path('about/', views.about, name='blog-about'), 



    # 3. program sees empty string, so it looks for pattern to match empty route^
    # 4. empty string pattern matches, will be handled by the function views.home^
]







# <app>/<model>_<viewtype>.html Looking for a template with a same condition