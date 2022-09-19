Pour ce défi, l'oracle est similaire sauf que nous ne disposons pas de N.
Pas grave l'arithmétique permet de résoudre facilement ce problème. En effet 1^x = 1 pour tout x différent 0.
Cela revient à dire que chiffrer le message 1 revient à faire 1^e % N soit 1 car N est très grand et que le reste de la division euclidienne de N par 1 vaut toujours 1.
En jouant avec les propriétés des modulos on peut donc déchiffrer le message -1 car -1 = Y^e % N <=> Y = N-1. En effet, 0 % N =0 et donc -1 % N = N-1
Donc N vaut la valeur qu'indique l'orcale pour -1 auquel on ajoute 1.
Puis nous revoilà sur le même problème que Rsa_oracle1 donc il suffit de refaire les mêmes étapes pour obtenir le flag 
