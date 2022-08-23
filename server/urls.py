from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views
from api.views import UserCreate, UserDetail,ApiView,NoteListApiView, NoteDetailApiView

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),

    # api
    path('api', ApiView.as_view()),
    
    # users
    path('api/auth/', include('rest_framework.urls')),
    path("api/auth/register/", UserCreate.as_view(), name="register"),
    path("api/auth/user/", UserDetail.as_view(), name="user"),
    path("api/auth/obtain/token/",views.TokenObtainPairView.as_view(),name="obtain-token"),
    path("api/auth/obtain/refreh/",views.TokenRefreshView.as_view(),name="refresh-token"),

    #notes
    path('api/notes', NoteListApiView.as_view()),
    path('api/notes/<int:note_id>/', NoteDetailApiView.as_view()),
]