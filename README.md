# DigimonWrapper
Digimon api wrapper, currently on python only but there will be a C# one out soon for a simulator project what will have more feature but I'd like to extense this one as well

Things you can get currently:
  - Get Digimon cards by name
  - Get all card from the database
  - Get one Digimon card by it's number(like bt1-010)
  - Get cards from it's
      - color
      - type
      - attribute
      - name and color
      - name and type
      - name and playcost
      - name and level
      - color and attribute
      - color and cost
      - color and level
      - rarity
      - evolution cost
      - level
  - Get the card sets where you can find that type of card by the number
  - Multicolored cards or cards with input colors
  - Download one card image by it's card number
  - Download all cards image

#Update
If you want to use some feature you have use first DownloadRequiredDatas function what is download the cards data in json file format

Used crates: requests, shutil, json, pandas
