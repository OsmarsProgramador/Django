from django.contrib import admin
from django.urls import include, path

app_name = 'core'

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('expense/', include('expense.urls', namespace='expense')),
    path('bookstore/', include('bookstore.urls', namespace='bookstore')),
    path('state/', include('state.urls', namespace='state')),
    path('product/', include('product.urls', namespace='product')),
    path('admin/', admin.site.urls),
]
