from rest_framework import routers
from .views import PokemonViewSet

router = routers.SimpleRouter()
router.register(r"pokemon", PokemonViewSet)
urlpatterns = router.urls
