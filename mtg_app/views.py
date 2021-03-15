from django.shortcuts import render
from mtg_app import support_functions, models

# App homepage
def home(request):
    data = dict()
    return render(request, "home.html")

def card_search(request):
    data = dict()
    return render(request, "card_search.html")

def search_results(request):
    query = request.GET.get('q')
    results = models.MTGCard.objects.filter(
        name__icontains=query
        )
    return render(request, 'search_results.html', {'results': results})

def maintenance(request):
    data = dict()

    try:
        form_submitted = request.GET['form_submitted']
        choice = request.GET['selection']
        print(choice)
        if choice == "1":
            support_functions.get_vintage_cards()

    except:
        pass

    return render(request, "maintenance.html")



