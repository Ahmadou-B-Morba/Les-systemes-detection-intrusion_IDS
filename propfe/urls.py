from django.contrib import admin
from django.urls import path
from detection import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accueil/', views.accueil, name='accueil'),
    path('', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('tableO/', views.tableO, name='tableO'),
    path('tableS/', views.tableS, name='tableS'),
    path('dashboardS/', views.dashboardS, name='dashboardS'),
    path('dashboardO/', views.dashboardO, name='dashboardO'),
    path('graphe_data/', views.graphe_data, name='graphe_data'),
    path('graphe_data_snort/', views.graphe_data_snort, name='graphe_data_snort'),
]