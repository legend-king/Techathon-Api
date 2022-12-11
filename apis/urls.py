from . import views
from django.urls import path


urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('forgotPass', views.forgotPass),
    path('addDish', views.addDish),
    path('viewDish', views.viewDish),
    path('removeDish', views.removeDish),
    path('order', views.order),
    path('setOrder', views.setOrder),
    path('viewOrder', views.viewOrder),
    path('viewOrders', views.viewOrders),
    path('cancelOrder', views.cancelOrder),
    path('acceptOrder', views.acceptOrder)
]