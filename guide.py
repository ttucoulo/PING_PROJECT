
from object_situation import *
from helper import *

import os
import sys
import collections as c


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
	phrase = ""
	try:
		path2 = "/tmp/vocal_fifo"
		try:
			obj_names, objects = liste_des_objets()
		except Exception as inst:
			print(inst)
			_ = read_fifo("/tmp/detection")
			continue
		word = read_fifo("/tmp/detection")

		if not (obj_names and objects):
			print("je ne reconnais rien")	
			write_fifo(path2, "je ne reconnais rien de ce que j'ai appris")
			continue

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
	except Exception as ex:
		print(ex)
		phrase = "Desole je n'ai pas pu traiter la requete suite a un bug"

	print(phrase)
	write_fifo(path2, phrase)
