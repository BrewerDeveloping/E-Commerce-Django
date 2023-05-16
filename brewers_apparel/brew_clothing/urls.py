from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('category/<int:id>/', views.category, name='category'),
    path('product/<str:name>/', views.product, name='product'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('search/', views.search_results, name='search_results'),
    # path('search/', views.search, name='search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)