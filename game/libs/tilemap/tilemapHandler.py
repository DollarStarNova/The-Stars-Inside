import json
mydata = []
with open("assets/spritesheets/testtiles.json", "r") as tiledata:
    mydata = json.load(tiledata)
