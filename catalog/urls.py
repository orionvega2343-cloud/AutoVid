from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog_view, name='catalog'),
    path('part/<int:part_id>/', views.part_detail_view, name='part_detail'),
    path('order/quick/<int:part_id>/', views.quick_order_view, name='quick_order'),
]
