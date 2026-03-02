from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('army-training/', views.army_training, name='army_training'),
    path('police-training/', views.police_training, name='police_training'),
    path('courses-fees/', views.courses_fees, name='courses_fees'),
    path('past-results/', views.past_results, name='past_results'),
    path('gallery/', views.gallery, name='gallery'),
    path('facilities/', views.facilities, name='facilities'),
    path('contact/', views.contact, name='contact'),
]
