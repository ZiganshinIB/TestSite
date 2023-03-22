from django.urls import path
from .views import *

urlpatterns = [
    path('', Curses.as_view(), name='index'),
    path('curses/', Curses.as_view(), name='curses'),
    path('curses/<int:group_id>/', CursesByGroup.as_view(), name='group'),
    path('create/curse/', CreateCurse.as_view(), name='create_curse'),
    path('create/group/', CreateGroup.as_view(), name='create_group'),
    path('homeworks/<int:curse_id>/', HomeworksByCurse.as_view(), name='homeworks'),
    path('curse/<int:pk>/', get_curse, name='curse'),
    path('homework/create/<int:curse_id>/', create_homework, name='create_homework'),
]
