"""levelup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Resource routing allows you to quickly declare all of the common routes for a given resourceful controller.
# Instead of declaring separate routes for your index... a resourceful route declares them in a single line of code.

# from levelupapi.views import GameTypes
from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from levelupapi.views import GameTypeView, GameView, EventView, Profile

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

# There are two mandatory arguments to the register() method:
# prefix - The URL prefix to use for this set of routes.
# viewset - The viewset class.
# r' = regex string
# http://localhost:3000/gametypes?game=
# basename - third argument / The base to use for the URL names that are created. 

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypeView, 'gametype')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')
router.register(r'profile', Profile, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]