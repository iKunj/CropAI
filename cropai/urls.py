from django.contrib import admin
from django.urls import path,include
from rainfall import views as rainfall_views
from predict import views as predict_views
from fertilizer import views as fertilizer_views
from news import views as news_views
from policy import views as policy_views
from temperature import views as temperature_views
from django.contrib.auth import views as auth_views
from users import views as users_view
from home import views as home_views
from fertilizer_shop import views as fertilizer_shop_views
from finance import views as finance_views
from sell import views as sell_views
from company import views as comapany_views
from library import views as library_views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('fertilizer/', fertilizer_views.home, name='fertilizer-home'),
    path('news/', news_views.home, name='news-home'),
    
    #Policy 
    path('policy/', policy_views.home, name='policy-home'),
    path('policy/apply', policy_views.apply, name='policy-add'),
    
    path('rainfall/', rainfall_views.home, name='rainfall-home'),
    path('temperature/', temperature_views.home, name='temperature-home'),
    
    #Finance Module Links
    path('finance/', finance_views.home, name='finance-home'),
    path('finance/expanse', finance_views.expense, name='finance-expanse'),
    path('finance/expanse/confirm', finance_views.expense_confirm, name='finance-expense-confirm'),
    path('finance/budget', finance_views.totalbudget, name='finance-tbudget'),
    path('finance/budget/confirm', finance_views.totalbudget_confirm, name='finance-tbudget-confirm'),
    path('finance/emi', finance_views.emi, name='emi-cal'),

    #User Part
    path('login/', home_views.login_view , name='login'),
    path('logout/', users_view.logout_view , name='logout_view'),

    #Fertilizer Shop
    path('fertilizer_shop/add',fertilizer_shop_views.add, name='fertilizer_shop'),
    path('fertilizer_shop/add/confirm',fertilizer_shop_views.add_confirm, name='fertilizer_shop_confirm'),

    #Sell Here part
    path('sell/', sell_views.home, name='sell-home'),
    path('sell/add', sell_views.add, name='sell-add'),
    path('sell/add/confirm', sell_views.add_confirm, name='sell_add_confirm'),
    path('sell/add/confirm/attach', sell_views.add_confirm_attach, name='sell_add_confirm_attach'),

    #Comapany Links
    path('company/', comapany_views.home, name='company-home'),
    path('company/add', comapany_views.add, name='company-add'),
    path('company/add/confirm', comapany_views.add_confirm, name='company_add_confirm'),
    path('company/add/confirm/attach', comapany_views.add_confirm_attach, name='company_add_confirm_attach'),

    #Crop Library
    path('library/', library_views.home, name='library-home'),

    #youtube link
    path('youtube/', home_views.ysearch, name='youtube-search'),

    #Help link
    path('help/', home_views.help, name='help-home'),

    #Predict Urls
    path('predict/', predict_views.home, name='predict-home'),
    path('predres/', predict_views.predres, name='predres-home'),
    path('predresyes/', predict_views.predresyes, name='predresyes-home'),
    path('predresno/', predict_views.predresno, name='predresno-home'),
    path('predresno2/', predict_views.predresno2, name='predresno2-home'),
]
