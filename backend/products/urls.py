from django.urls import path
from .views import (
    CreateProductView,
    ValidateProductView,
    GetAllProductsView,
    GetOneProductView,
    CategoryCreateView,
    GetAllCategoriesView,
    GetAllUnapprovedProductsView,
    ProductViewSet,
    CreateOrderView,
    GetOneUserAllOrdersView, 
    GetProductsByCategoryView,
    GetAllOrdersBySupplierView,
    UpdateOrderStatusView,
    DeleteProductView,
    GetAllOrdersAdminView,
    GetProductsByUserView,
    UpdateProductView
)
urlpatterns = [
    path('create/product/', CreateProductView.as_view(), name='create_product'),
    path('validate/product/<int:pk>/', ValidateProductView.as_view(), name='validate_product'),
    path('products/', GetAllProductsView.as_view(), name='get_all_products'),
    path('products/<int:id>/', GetOneProductView.as_view(), name='get_one_product'),
    path('create/category/', CategoryCreateView.as_view(), name='create_category'),
    path('categories/', GetAllCategoriesView.as_view(), name='get_all_categories'),
    path('products/unapproved/', GetAllUnapprovedProductsView.as_view(), name='get_all_unapproved_products'),
    path('products/filtred/', ProductViewSet.as_view({'get': 'list'}), name='get_all_products'),
    path('create/order/', CreateOrderView.as_view(), name='create_order'),
    path('orders/user/', GetOneUserAllOrdersView.as_view(), name='get_one_user_all_orders'),
    path('products/category/<int:category_id>/', GetProductsByCategoryView.as_view(), name='get_products_by_category'),
    path('orders/supplier/', GetAllOrdersBySupplierView.as_view(), name='get_all_orders_by_supplier'),
    path('orders/<int:id>/update-status/', UpdateOrderStatusView.as_view(), name='update-order-status'),
    path('products/<int:id>/delete/', DeleteProductView.as_view(), name='delete-product'),
    path('orders/admin/', GetAllOrdersAdminView.as_view(), name='admin-orders'),
    path('products/user/', GetProductsByUserView.as_view(), name='user-products'),
     path('products/<int:id>/update/', UpdateProductView.as_view(), name='update-product'),

]