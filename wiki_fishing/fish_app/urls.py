from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from fish_app import views

urlpatterns = ([
    path('', views.index, name='index'),
    path('fish/', views.fish_list, name='fish_list'),
    path('fish/<int:fish_id>/', views.fish_detail, name='fish_detail'),
    path('baits/', views.bait_list, name='bait_list'),
    path('baits/<int:bait_id>/', views.bait_detail, name='bait_detail'),
    path('add_fish/', views.add_fish, name='add_fish'),
    path('add_bait/', views.add_bait, name='add_bait'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
