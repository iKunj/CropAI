from django.contrib import admin
from django.urls import path,include
from rainfall import views as rainfall_views
from predict import views as predict_views
from fertilizer import views as fertilizer_views
from news import views as news_views
from policy import views as policy_views
from temperature import views as temperature_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('fertilizer/', fertilizer_views.home, name='fertilizer-home'),
    path('news/', news_views.home, name='news-home'),
    path('policy/', policy_views.home, name='policy-home'),
    path('rainfall/', rainfall_views.home, name='rainfall-home'),
    path('predict/', predict_views.home, name='predict-home'),
    path('temperature/', temperature_views.home, name='temperature-home'),

    #User Part
    path('login/', auth_views.LoginView.as_view(template_name = 'home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'home/logout.html'), name='logout'),
]
