import requests
import shutil

def GetCardsByName(name : str):
    url = "https://digimoncard.io/api-public/search.php?n="+name
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

#card id like bt1-010
def GetCardByCardNumber(card_id : str):
    url = "https://digimoncard.io/api-public/search.php?card="+card_id
    res = requests.get(url)
    if res.status_code == 200:
        print("asd?")
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

def GetAllCardsFromColor(color:str):
    url = "https://digimoncard.io/api-public/search.php?color="+color
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

#type cards like digimon, digi-egg, option etc..
def GetCardsFromType(c_type:str):
    url = "https://digimoncard.io/api-public/search.php?type="+c_type
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

#like Vaccine
def GetCardsByAttribute(attr:str):
    url = "https://digimoncard.io/api-public/search.php?color="+attr
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

def GetCardsByColorAndType(color:str, c_type:str):
    url = "https://digimoncard.io/api-public/search.php?color="+color+"&type="+c_type
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

def GetCardsByNameAndColor(name:str,color:str):
    url = "https://digimoncard.io/api-public/search.php?n="+name+"&color="+color
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

def GetCardsByNameAndType(name:str, type:str):
    url = "https://digimoncard.io/api-public/search.php?n="+name+"&type="+type
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

def GetCardsByColorAndAttribute(color:str, attr:str):
    url = "https://digimoncard.io/api-public/search.php?color="+color+"&attribute="+attr
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

def GetAllCard():
    url = "https://digimoncard.io/api-public/getAllCards.php?sort=name&series=Digimon Card Game&sortdirection=asc"
    res = requests.get(url)
    #print(res.json)
    if res.status_code == 200:
        return res.json()
    else:
        return "Cannot get the cards, reason: "+res.reason

def GetCardSetsWhereICanFindThisDigimonByName(name:str):
    list = GetCardsByName(name)
    retList = []
    for digimon in list:
        retList.append(digimon["card_sets"])
    return retList

def GetCardSetBySerialId(serial_id:str):
    return GetCardByCardNumber(serial_id)[0]["card_sets"]

#You need the card number here
def DownloadCardImage(card_id):
    url = "https://images.digimoncard.io/images/cards/"+card_id+".jpg"
    res = requests.get(url,stream=True)
    file_name = card_id+".jpg"

    if res.status_code == 200:
        with open(file_name, "wb") as f:
            shutil.copyfileobj(res.raw,f)
    else:
        print(res.reason)

def DownloadAllCardImage():
    allCards = [number for number in GetAllCard()]
    for i in range(len(allCards)):
        DownloadCardImage(allCards[i]["cardnumber"])
