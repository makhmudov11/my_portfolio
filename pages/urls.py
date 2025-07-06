
from django.urls import path

from pages.views import home_view, about_view, contact_view

# from pages.views import currency_data_view

app_name = 'pages'


urlpatterns = [
    # path('', currency_data_view, name='pages'),
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
]