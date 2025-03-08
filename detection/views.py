from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .models import Tableossec, Tablessnort
import json

# Create your views here.

def accueil(request):
    return render(request, 'accueil.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            return render(request, 'connexion.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    return render(request, 'connexion.html')

def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        nomprenom = request.POST['nomprenom']
        mdp = request.POST['mdp']
        confirmer_mdp = request.POST['confirmer_mdp']

        if mdp != confirmer_mdp:
            return render(request, 'inscription.html', {'error': 'Les mots de passe ne correspondent pas.'})
        
        try:
            user = User.objects.create_user(username=username, first_name=nomprenom.split()[0], last_name=" ".join(nomprenom.split()[1:]), password=mdp)
            user.save()
            login(request, user)
            return redirect('connexion')
        except Exception as e:
            return render(request, 'inscription.html', {'error': str(e)})

    return render(request, 'inscription.html')

def tableO(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Vérifie si la requête est une requête AJAX
        donnees = list(Tableossec.objects.values())  # Récupère toutes les données de la table
        return JsonResponse(donnees, safe=False)
    else:
        donnees = list(Tableossec.objects.values())  # Assurez-vous que donnees est défini pour les requêtes non-AJAX
        return render(request, 'tableO.html', {'donnees': donnees})


def tableS(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Vérifie si la requête est une requête AJAX
        donnees = list(Tablessnort.objects.values())  # Récupère toutes les données de la table
        return JsonResponse(donnees, safe=False)
    else:
        donnees = list(Tablessnort.objects.values())  # Assurez-vous que donnees est défini pour les requêtes non-AJAX
        return render(request, 'tableS.html', {'donnees': json.dumps(donnees)})  # Convertir en JSON avant de passer au template
    

def dashboardO(request):
    return render(request, 'dashboardO.html')  # Ajoutez cette ligne pour définir la vue dashboardO


def dashboardS(request):
    return render(request, 'dashboardS.html')  # Assurez-vous que ce chemin correspond à votre template HTML

def graphe_data(request):
    donnees = list(Tableossec.objects.values('timestamp', 'rule_firedtimes', 'rule_level', 'prediction_ml', 'rule_groups'))
    return JsonResponse(donnees, safe=False)

def graphe_data_snort(request):
    data = Tablessnort.objects.values('ID', 'alert', 'Prediction_ml')
    return JsonResponse(list(data), safe=False)