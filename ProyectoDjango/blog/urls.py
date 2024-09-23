from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Blog, name="Blog"),
    path('categoria/<int:id_categorias>/', views.Categorias, name="Categorias"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)