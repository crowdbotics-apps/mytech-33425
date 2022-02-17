from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('mytek-admin-now/', admin.site.urls),
    path('', views.index, name='index'),
    path('store/', include("store.urls")),
    path('cart/', include("cart.urls")),
    path('accounts/', include("accounts.urls")),
    path('orders/', include("orders.urls")),
    path('newsletter/', include("newsletter.urls")),
    path('api/', include("api.urls")),
]