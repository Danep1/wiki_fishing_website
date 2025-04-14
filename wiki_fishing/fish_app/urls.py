from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from fish_app.views import *

urlpatterns = ([
    path('', index, name='index'),
    path('fish/', fish_list, name='fish_list'),
    path('fish/<int:fish_id>/', fish_detail, name='fish_detail'),
    path('baits/', bait_list, name='bait_list'),
    path('baits/<int:bait_id>/', bait_detail, name='bait_detail'),
    path('add_fish/', add_fish, name='add_fish'),
    path('add_bait/', add_bait, name='add_bait'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
