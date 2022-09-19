En accedant a cet oracle, nous avons la possibilité de connaitre la clé publique (N,e)
Le RSA est une méthode de chiffrement très sécurisé sauf si on met un oracle qui déchiffre tout sauf le message entre ces mains.
En effet M(x*y) = M(x)*M(y) donc de même C(x*y) = C(x)*C(y).
Par conséquent il suffit de diviser le message chiffrer en 2 facteurs, l'oracle changeant de clés à chaque connexion, ces facteurs ne sont pas les mêmes.
Pour généraliser une solution est la suivante:
Soit N la clé, e l'exposant et c le message chiffré tel que c=x*y (par exemple si c est paire, on a c=2*y avec y=c/2)
En demandant à l'oracle le message en clair quand celui-ci chiffrer vaut x on obtient le résultat m1, de même pour y on obtient m2

Il ne reste plus qu'à executer la commane suivante en python print(long_to_bytes((m1*m2)%N)) et puf voilà le flag