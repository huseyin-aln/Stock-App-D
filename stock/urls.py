from rest_framework import routers
from .views import CategoryView


router = routers.DefaultRouter()
router.register('categories', CategoryView)

urlpatterns = [
    
]

urlpatterns += router.urls