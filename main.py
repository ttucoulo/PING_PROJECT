from object_situation import *

#table=Objet("table", 150,250,50,70)
chaise=Objet("chaise",600,550,150,150)
table1=Objet("table",1000,150,50,50)
liste=[]
#liste.append(table)
liste.append(chaise)
liste.append(table1)

print(detection_obstacle(liste,1,20))
#print(selection_objet(liste,"table",20).x)

