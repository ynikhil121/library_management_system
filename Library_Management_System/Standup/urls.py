from django.urls import path
from Standup import views
urlpatterns = [
    path('sun/', views.bkf),
    path('delete/<int:id>/', views.delete),
    # path('softdelete/<int:id>/',views.softdelete),
    path('update/<int:id>/',views.update),
    path('allbook/',views.allbook),
    path('htol/',views.hightolow),
    path('ltoh/',views.lowtohigh),
    path('NonFiction/',views.NonFiction),
    path('Fiction/',views.Fiction),
    path('Reference/',views.Reference),
    path('Edited/',views.Edited),
    path('search/',views.search),
]
