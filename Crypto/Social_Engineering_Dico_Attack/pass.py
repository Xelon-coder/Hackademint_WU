import hashlib

text = """Abeille, Agneau, Aigle, Albatros, Asticot, Alligator, Alpaga, Ane, Anguille, Antilope, Araignée, Asticot, Autruche, 
Babouin, Baleine, Béluga, Bigorneau, Bison, Blaireau, Blobfish, Boa, Boeuf, Bourdon, Buffle, 
Cafard, Calmar, Caméléon, Canard, Caribou, Carpe, Castor, Cerf, Chacal, Chameau, Chamois, Chat, Chauve-souris, Chenille, Cheval, Chèvre, Chevreuil, Chien, Chimpanzé, Chouette, Cigale, Cigogne, Cobra, Coccinelle, Cochon, Cochon d'Inde, Colombe, Coq, Couleuvre, Coyote, Crabe, Crapaud, Crevette, Criquet, Crocodile, Cygne, 
Dauphin, Dromadaire, 
Ecureuil, Eléphant, Escargot, Espadon, 
Fennec, Flament rose, Fouine, Fourmi, Frelon, Furet, 
Gendarme, Gerbille, Girafe, Gorille, Grenouille, Guépard, Guêpe, 
Hamster, Hérisson, Hibou, Hippocampe, Hippopotame, Hirondelle, Homard, Huître, Hyène, 
Iguane, 
Jaguar, 
Kangourou, Kiwi, Koala, 
Lama, Lapin, Larve, Léopard, Lézard, Libellule, Lièvre, Limace, Lion, Loup, Loutre, Luciole, Lynx, 
Macaque, Manchot, Mante religieuse, Méduse, Mille-pattes, Morse, Mouche, Moustique, Mouton, Mulet, Mygale, 
Narval, 
Oie, Orang-outan, Ornithorynque, Orque, Otarie, Ouistiti, Ours, Ours polaire, 
Panda, Panda roux, Pangolin, Panthère, Paon, Papillon, Papillon de nuit, Paresseux, Pélican, Perce-oreille, Perroquet, Perruche, Phacochère, Phasme Phoque, Pic vert, Pieuvre, Pigeon, Piranha, Poisson rouge, Poisson clown, Poisson-globe, Poney, Porc, Porc-épic, Pou, Poule, Poulpe, Poussin, Puce, Puma, Punaise, Putois, Python, 
Raie, Rat, Raton laveur, Renard, Requin, Requin-marteau, Rhinocéros, Rouge-gorge, 
Salamandre, Sanglier, Sangsue, Sardine, Saumon, Scarabée, Scorpion, Serpent, Singe, Souris, Suricate, 
Tapir, Tatou, Taupe, Taureau, Thon, Tigre, Tortue, Toucan, Triton, Truite, 
Vache, Vautour, Ver, Ver de terre, Vipère, 
Zèbre"""

text= text.replace("\n","").replace("é","e").replace("è","e").split(', ')
for i in range(0,999):
	for animal in text:
		animal = animal[0:len(animal)-1]+ animal[len(animal)-1].upper() + str(i)+"@#"
		#print(animal)
		res = hashlib.sha256(animal.encode()).hexdigest()
		if(res == "ca868318d6a3283d089377545a7c3275be934177d9946aba86638b658bae131e"):
			print("FLAG")
			print(animal)
