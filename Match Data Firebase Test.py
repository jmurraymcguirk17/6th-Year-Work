from firebase import firebase
import pandas
myDBConn=firebase.FirebaseApplication("https://round-towers-stats-default-rtdb.europe-west1.firebasedatabase.app/",None)
name=[]
turnoversWon=[]
data=pandas.read_csv("Match Data 2.csv")

for i in data['Players']:
    name.append(i)
print(name)
count=0
for i in name:
    turnover=0
    for x in data['Events']:
        if i in x and "turnover won" in x:
            turnover+=1
        turnoversWon.append(turnover)
            

'''for i in data['Turnovers Won:']:
    turnoversWon.append(i)
print(turnoversWon)'''

counter=0
for i in name:
    data={
        "name":i,
        "turnovers won":turnoversWon[counter]
    }
    myDBConn.post("/{name}/data",data)
    counter+=1
