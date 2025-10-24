from django.urls import path
from .views import IndexView, UserIconClickView, LoginView
from .views import LoginView, CreateAccountView
from .views import IndexView, ProductCategoryView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('user-click/', UserIconClickView.as_view(), name='user_icon_click'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-account/', CreateAccountView.as_view(), name='create_account'),
    path('category/<str:category>/', ProductCategoryView.as_view(), name='category'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)