from object_situation import *

table=Objet("table", 150,250,50,50)
chaise=Objet("chaise",100,150,50,50)
table1=Objet("table",600,550,150,150)
liste=[]
liste.append(table1)
liste.append(chaise)
liste.append(table)


#print(detection_obstacle(liste,0,25))
print(selection_objet(liste,"table",15).x)


