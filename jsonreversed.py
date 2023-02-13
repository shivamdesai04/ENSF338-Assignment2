import json

with open("ex2TestData.json", "r") as reverse:
    data = json.load(reverse)

reversedJson = []

for tests in data:
    reversedJson.append(tests[::-1])

with open("ex2.5.json", "w") as reversed:
    json.dump(reversedJson, reversed)
