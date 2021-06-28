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
router.register('teams', TeamViewSet)
router.register('sport', SportViewSet)
router.register('events', EventViewSet)
router.register('athletes', AthleteViewSet)
router.register('games', GameViewSet)
router.register('medals', MedalViewSet)
