from django.urls import path

from . import views
from . import user
from . import business

urlpatterns = [
    path('', views.index, name='index'),
    # path('businessCount/', views.businessCount, name='businessCount'),
    path('terminalG4CountCity/', views.terminalG4CountCity, name='terminalG4CountCity'),
    path('terminalG4DetailCount/', views.terminalG4DetailCount, name='terminalG4DetailCount'),
    path('terminalG5CountCity/', views.terminalG5CountCity, name='terminalG5CountCity'),
    path('terminalG5DetailCount/', views.terminalG5DetailCount, name='terminalG5DetailCount'),

    path('allUserCountCity/', user.allUserCountCity, name='allUserCountCity'),
    path('allUserDetailCount/', user.allUserDetailCount, name='allUserDetailCount'),
    path('g4UserCountCity/', user.g4UserCountCity, name='g4UserCountCity'),
    path('g4UserDetailCount/', user.g4UserDetailCount, name='g4UserDetailCount'),
    path('g5UserCountCity/', user.g5UserCountCity, name='g5UserCountCity'),
    path('g5UserDetailCount/', user.g5UserDetailCount, name='g5UserDetailCount'),
    path('potentialG5UserCountCity/', user.g5UserCountCity, name='g5UserCountCity'),
    path('potentialG5UserDetailCount/', user.g5UserDetailCount, name='g5UserDetailCount'),
    path('arpuhighUserCountCity/', user.arpuhighUserCountCity, name='arpuhighUserCountCity'),
    path('arpuhighUserDetailCount/', user.arpuhighUserDetailCount, name='arpuhighUserDetailCount'),
    path('userTerminalPriceHighCountCity/', user.userTerminalPriceHighCountCity, name='userTerminalPriceHighCountCity'),
    path('userTerminalPriceHighDetailCount/', user.userTerminalPriceHighDetailCount,
         name='userTerminalPriceHighDetailCount'),
    path('userDouhighCountCity/', user.userDouhighCountCity, name='userDouhighCountCity'),
    path('userDouhighDetailCount/', user.userDouhighDetailCount, name='userDouhighDetailCount'),

    path('businessAllMCountCity/', business.businessAllMCountCity, name='businessAllMCountCity'),
    path('businessAllMDetailCount/', business.businessAllMDetailCount, name='businessAllMDetailCount'),
]
