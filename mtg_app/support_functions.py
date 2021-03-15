import requests
from mtg_app.models import MTGCard

# Get all Standard legal cards and save them to a model in the DB

def get_vintage_cards():
    response = requests.get("https://mtgjson.com/api/v5/VintageAtomic.json")
    t1_json = response.json().get("data")
    t1_cardnames = list()

    for c in t1_json.keys():
        t1_cardnames.append(c)

    for c in t1_cardnames:
        card = t1_json.get(c)[0]

        try:
            newcard = MTGCard.objects.get(name=c)
            print("Found existing MTGCard", c)
        except:
            newcard = MTGCard(name=c,
                        colors=card.get('colors')
                        )
            print("Creating new MTGCard object", c)

        newcard.name = c
        print("Saving to database", c)
        newcard.save()
