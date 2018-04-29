from object_situation import *

table1=objet("table", 400,300,100,120)
chaise=objet("chaise",100,150,50,50)
table=objet("table",635,550,150,150)
liste=[]
liste.append(table1)
liste.append(chaise)
liste.append(table)

#print(detection_obstacle(liste,0,25))
print(selection_objet(liste,"table",15).x)


