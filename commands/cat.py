#!/usr/bin/python3
import json
import urllib.request

CAT_API_URL = 'https://api.thecatapi.com/v1/images/search?mime_types=png,jpg'
BREED_URL = 'https://api.thecatapi.com/v1/images/search?mime_types=png,jpg&breed_ids='

NAMES_IDS = {"Abyssinian": "abys", "Aegean": "aege", "AmericanBobtail": "abob", "AmericanCurl": "acur", "AmericanShorthair": "asho", "AmericanWirehair": "awir", "Ankara": "tang", "ArabianMau": "amau", "AustralianMist": "amis", "Balinese": "bali", "Bambino": "bamb", "Bengal": "beng", "Birman": "birm", "Bombay": "bomb", "BritishLonghair": "bslo", "BritishShorthair": "bsho", "Burmese": "bure", "Burmilla": "buri", "CaliforniaSpangled": "cspa", "ChantillyTiffany": "ctif", "Chartreux": "char", "Chausie": "chau", "Cheetoh": "chee", "ColorpointShorthair": "csho", "CornishRex": "crex", "Cymric": "cymr", "Cyprus": "cypr", "DevonRex": "drex", "Donskoy": "dons", "DragonLi": "lihu", "EgyptianMau": "emau", "EuropeanBurmese": "ebur",
             "ExoticShorthair": "esho", "HavanaBrown": "hbro", "Himalayan": "hima", "JapaneseBobtail": "jbob", "Javanese": "java", "KhaoManee": "khao", "Korat": "kora", "Kurilian": "kuri", "Laperm": "lape", "MaineCoon": "mcoo", "Malayan": "mala", "Manx": "manx", "Munchkin": "munc", "Nebelung": "nebe", "NorwegianForestCat": "norw", "Ocicat": "ocic", "Oriental": "orie", "Persian": "pers", "PixieBob": "pixi", "Ragamuffin": "raga", "Ragdoll": "ragd", "RussianBlue": "rblu", "Savannah": "sava", "ScottishFold": "sfol", "SelkirkRex": "srex", "Siamese": "siam", "Siberian": "sibe", "Singapura": "sing", "Snowshoe": "snow", "Somali": "soma", "Sphynx": "sphy", "Tonkinese": "tonk", "Toyger": "toyg", "Van": "tvan", "YorkChocolate": "ycho"}


def load_cat_url(url):
    json_data = json.loads(urllib.request.urlopen(url).read())
    return json_data[0].get('url')


class CatQueue():
    def __init__(self, breeds=None):
        if breeds == None:
            self.url = CAT_API_URL
        else:
            self.url = BREED_URL + ",".join(breeds)

    def get(self):
        return load_cat_url(self.url)


if __name__ == "__main__":
    cat_queue = CatQueue()
    print(cat_queue.get())
