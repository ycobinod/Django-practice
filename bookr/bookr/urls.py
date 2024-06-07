from reviews.admin import admin_site
from django.urls import include, path

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('reviews.urls')),
    path('book_management/', include('book_management.urls'))
]
