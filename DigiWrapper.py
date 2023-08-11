import requests
import shutil
import time
import json
import pandas

class DigiWrapper:
    allCards = {}
    allCardsWithDatas = []
    cardInformationJsonLike = {}
    def __init__(self) -> None:
        print("Init....")
        self.allCards = self.GetAllCard()
        print("Reading json file...")
        self.ReadJsonFile()

    def DownloadRequiredDatas(self):
        with open("digicards.json", "w",encoding='utf-8') as f:
            for i in range(len(self.allCards)):
                time.sleep(1.5)
                card = self.GetCardByCardNumber(self.allCards[i]["cardnumber"])
                json.dump(card, f, ensure_ascii=False, indent=4,separators=(',',':'))
                print("added")

    def ReadJsonFile(self):
        test = pandas.read_json("digicards.json")

        for i in range(len(test)):
            self.cardInformationJsonLike[i] = test[0][i]
        
    def TestJson(self):
        for i, card in self.cardInformationJsonLike.items():
            try:
                print(card["name"])
            except Exception:
                print(Exception)

    def GetCardsByName(self, name : str):
        url = "https://digimoncard.io/api-public/search.php?n="+name
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    #card id like bt1-010
    def GetCardByCardNumber(self,card_id : str):
        url = "https://digimoncard.io/api-public/search.php?card="+card_id
        res = requests.get(url)
        if res.status_code == 200:
            print("asd?")
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    def GetAllCardsFromColor(self,color:str):
        url = "https://digimoncard.io/api-public/search.php?color="+color
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    #type cards like digimon, digi-egg, option etc..
    def GetCardsFromType(self,c_type:str):
        url = "https://digimoncard.io/api-public/search.php?type="+c_type
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    #like Vaccine
    def GetCardsByAttribute(self, attr:str):
        url = "https://digimoncard.io/api-public/search.php?color="+attr
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    def GetCardsByColorAndType(self,color:str, c_type:str):
        url = "https://digimoncard.io/api-public/search.php?color="+color+"&type="+c_type
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    def GetCardsByNameAndColor(self, name:str,color:str):
        url = "https://digimoncard.io/api-public/search.php?n="+name+"&color="+color
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    def GetCardsByNameAndType(self, name:str, type:str):
        url = "https://digimoncard.io/api-public/search.php?n="+name+"&type="+type
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    def GetCardsByColorAndAttribute(self, color:str, attr:str):
        url = "https://digimoncard.io/api-public/search.php?color="+color+"&attribute="+attr
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    def GetAllCard(self):
        url = "https://digimoncard.io/api-public/getAllCards.php?sort=name&series=Digimon Card Game&sortdirection=asc"
        res = requests.get(url)
        #print(res.json)
        if res.status_code == 200:
            return res.json()
        else:
            return "Cannot get the cards, reason: "+res.reason

    def GetCardSetsWhereICanFindThisDigimonByName(self,name:str):
        list = self.GetCardsByName(name)
        retList = []
        for digimon in list:
            retList.append(digimon["card_sets"])
        return retList

    def GetCardSetBySerialId(self, serial_id:str):
        return self.GetCardByCardNumber(serial_id)[0]["card_sets"]

    def GetCardsWithResourceCost(self, res_cost):
        paramCostCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if card["play_cost"] == res_cost:
                    paramCostCards.append(card)
            except Exception:
                print(Exception)
        return paramCostCards

    def GetCardsWithLevel(self, level):
        paramLevelCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if card["level"] == level:
                    paramLevelCards.append(card)
            except Exception:
                print(Exception)
        return paramLevelCards

    def GetCardsWithEvolutionCost(self,evo_cost):
        paramEvoCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if card["evolution_cost"] == evo_cost:
                    paramEvoCards.append(card)
            except Exception:
                print(Exception)
        return paramEvoCards
    
    def GetCardsByRarity(self,rarity):
        paramRarityCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if card["cardrarity"] == rarity:
                    paramRarityCards.append(card)
            except Exception:
                print(Exception)
        return paramRarityCards
    
    def GetCardsByColorAndLevel(self,color,level):
        paramCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if  card["color"] == color and card["level"]:
                    paramCards.append(card)
            except Exception:
                print(Exception)
        return paramCards
    
    def GetCardByColorAndCost(self,color,cost):
        paramCards = []
        for i, card in card.items():
            try:
                if card[i]["color"] == color and card[i]["play_cost"] == cost:
                    paramCards.append(card)
            except Exception:
                print(Exception)
        return paramCards
    
    def GetCardsByNameAndLevel(self,name,level):
        paramCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if card["name"] == name and card["level"] == level:
                    paramCards.append(card)
            except Exception:
                print(Exception)
        return paramCards
    
    def GetCardsByNameAndCost(self,name,cost):
        paramCards = []
        time.sleep(3)
        for i in range(len(self.allCards)):
            time.sleep(1)
            card = self.GetCardByCardNumber(self.allCards[i]["cardnumber"])
            #print(card)
            if(card[0]["name"] == name and card[0]["play_cost"] == cost):
                paramCards.append(card)
        return paramCards
    
    def GetAllMultiColorCards(self):
        paramCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if card["color2"] is not None:
                    paramCards.append(card)
            except Exception:
                print(Exception)
        return paramCards        

    def GetMultiColorCards(self,color1, color2):
        paramCards = []
        for i, card in self.cardInformationJsonLike.items():
            try:
                if (card["color"] == color1 and card["color2"] == color2) or (card["color2"] == color1 and card["color"] == color2):
                   paramCards.append(card)
            except Exception:
                print(Exception)
        return paramCards        

    #You need the card number here
    def DownloadCardImage(self,card_id):
        url = "https://images.digimoncard.io/images/cards/"+card_id+".jpg"
        res = requests.get(url,stream=True)
        file_name = card_id+".jpg"

        if res.status_code == 200:
            with open(file_name, "wb") as f:
                shutil.copyfileobj(res.raw,f)
        else:
            print(res.reason)

    def DownloadAllCardImage(self):
        time.sleep(3)
        for i in range(len(self.allCards)):
            time.sleep(1)
            self.DownloadCardImage(self.allCards[i]["cardnumber"])