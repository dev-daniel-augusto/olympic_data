from rest_framework.routers import SimpleRouter

from .views import (
    TeamViewSet,
    SportViewSet,
    EventViewSet,
    AthleteViewSet,
    GameViewSet,
    MedalViewSet,
    )


router = SimpleRouter()
router.register('teams', TeamViewSet, basename='teams')
router.register('sport', SportViewSet, basename='sport')
router.register('events', EventViewSet, basename='events')
router.register('athletes', AthleteViewSet, basename='athletes')
router.register('games', GameViewSet, basename='games')
router.register('medals', MedalViewSet, basename='medals')
