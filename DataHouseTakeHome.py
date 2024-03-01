'''Setting the Data'''

import json


# f = open('practice.json')
with open("practice.json", "r") as f:
    data = json.load(f)

# #Shows team stats for each member
# print("\nTeam Stats: \n")
# for i in data['team']:
#     #print("Attributes: ", i['attributes'])
#     print("Intelligence: ", i['attributes']['intelligence'])
#     print("Strength: ", i['attributes']['strength'])
#     print("Endurance: ", i['attributes']['endurance'])
#     print("Spicy Food Tolerance: ", i['attributes']['spicyFoodTolerance'], "\n")

#Created variables for stats of the team 
# print("Total Stats \n")
    
'''Team Data'''
Intel     = 0
Strength  = 0
Endurance = 0
SpicyTol  = 0

#adding all the stats together to get a total
for i in data['team']:
    #print("Intelligence: ", i['attributes']['intelligence'])
    Intel     += i['attributes']['intelligence']
    Strength  += i['attributes']['strength']
    Endurance += i['attributes']['endurance']
    SpicyTol  += i['attributes']['spicyFoodTolerance']

# print("Intel: ", Intel, "\n")
# print("Strength: ", Strength, "\n")
# print("Endurance: ", Endurance, "\n")
# print("Spicy Food Tolerance: ", SpicyTol, "\n")
# print("Total: ", (Intel + Strength + Endurance + SpicyTol), "\n")


# print("\nApplicants")
# for i in data['applicants']:
#     print(i)

# print("Team Scores with Applicant: ")
    

'''Applicants'''

scoresT = []
#print('scoresT', scoresT)
scoresB = []
names = []

for i in data['applicants']:
    # print(i['name'], " : ")
    Intel2 = Intel
    Intel2 += i['attributes']['intelligence']
    # print("I    : ", Intel2)
    
    Strength2 = Strength
    Strength2 += i['attributes']['strength']
    # print("S    : ", Strength2)

    Endurance2 = Endurance
    Endurance2 += i['attributes']['endurance']
    # print("E    : ", Endurance2)

    SpicyTol2 = SpicyTol
    SpicyTol2 += i['attributes']['spicyFoodTolerance']
    # print("sFT  : ", SpicyTol2)

    names.append(i['name'])



    Total2 = Intel2 + Strength2 + Endurance2 + SpicyTol2
    # print("Total: ", Total2, "\n")
    scoresT.append((Total2/(Intel + Strength + Endurance + SpicyTol)) - 1)
    # print("scoresT: ", scoresT)



    avgD = Total2/4
    # print("avgD", avgD)
    difIntel = (abs(Intel2 - avgD))/avgD
    # print(difIntel)
    difStr   = (abs(Strength2 - avgD))/avgD
    # print(difStr)
    difEnd   = (abs(Endurance2 - avgD))/avgD
    # print(difEnd)
    difSFT   = (abs(SpicyTol2 - avgD))/avgD
    # print(difSFT)

    scoresB.append(.25*(1-difIntel) + .25*(1-difStr) + .25*(1-difEnd) + .25*(1-difSFT))
    # print("scoresB: ", scoresB)


ScoreTot = []
for i in range(len(scoresB)):
    ScoreTot.append(0.5*scoresT[i] + 0.5*scoresB[i])
    ScoreTot[i]=round(ScoreTot[i], ndigits=2)

# print(ScoreTot)
# print(names)


'''Returning File'''

DicTot = {"scoredApplicants" : []}

for name, score in zip(names, ScoreTot):
    applicants = {"name" : name, "score" : score}

    DicTot["scoredApplicants"].append(applicants)

# print(DicTot)

with open ("result.json", "w") as f:
    json.dump(DicTot, f, indent = 5)

# f.close()