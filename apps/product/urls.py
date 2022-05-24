from django.urls import include, path

from apps.product.views import CategoryListView, index, get_product

urlpatterns = [
    # path('home/', index, name='home'),
    path('products/json', CategoryListView.as_view(), name='list category'),
    path('products/', index, name='list category'),
    path('<str:slug>/', get_product, name='list-product'),
    path('post-detail/<int:pk</', CategoryListView.as_view()),
]