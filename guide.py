
from object_situation import *

import os
import sys
import collections as c


def write_fifo(path, message):
	fifo = open(path, "w")

        fifo.write(message)
        fifo.close()

def read_fifo(path):
	fifo = open(path, "r")
	message=fifo.readline()
	fifo.close()
	return message

def description (liste):
	if not liste:
		phrase = "Je ne reconnais rien de ce que j'ai appris"
	else:
		dic = c.Counter(liste)
		phrase = "il y a "
		plur = ""
		for mot in dic.keys():
			if dic[mot] > 1:
				plur = "des"
			else:
				plur = objects_list[mot][1]
				phrase += plur+" "
				phrase+=mot
				phrase +=", "
	return phrase




while True:
        path2 = "/tmp/vocal_fifo"
	obj_names, objects = liste_des_objets()
        word = read_fifo("/tmp/detection")

	if not (obj_names and objects):
		print("ok")	
		write_fifo(path2, "je ne reconnais rien de ce que j'ai appris")
		continue

	phrase = ""
	if word =="description":
		phrase = description(obj_names)
	elif word in  objects_list.keys():
		object, obstacles = return_reachable_object(objects, word,10)
		if object:
			phrase = situate_object(object, obstacles, 15, 2)
		else:
			phrase = "Cet objet ne se trouve pas dans mon champs de vision"
	else:
		phrase = "je ne comprends pas la requete"
		print(phrase)

	print(phrase)
	write_fifo(path2, phrase)
