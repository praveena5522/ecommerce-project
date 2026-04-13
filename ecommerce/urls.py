"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home1,name='home'),
    path('allpets/',views.allpets,name='allpets'),
    path('login/',views.login1,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout1,name='logout'),
    path('detailes/<int:p_id>/',views.detailes1,name='detailes'),
    path('add_to_cart/<int:p_id>/', views.add_to_cart, name='add_to_cart'),
    path('minus_from_cart/<int:p_id>/', views.minus_from_cart, name='minus_from_cart'),
    path('remove_cart_item/<int:p_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('buying_detailes/<int:p_id>/',views.buying_detailes,name='buying_detailes'),
    path('my-orders/',views.my_orders,name='my_orders'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
