Ce challenge m'a pris pas mal de temps pour au final une solution assez simple qui permet de réussir les 3 défis avec le même payload.
En y regardant de plus près on appelle que l'argument 1 soit \$\1 mais jamais un autre argument \$\2, le fait de mettre \$\1 en majusccule avec \${1^^} ne marche pas quand les caractères ne sont pas des lettres.
De plus le programme à une faille importante encore, il utilise des doubles quotes ce qui nous permet d'injecter des caractères comme $ et qu'il ne soit pas vu en tant que caratère textuel.
En executant le programme de la façon suivante :[ ./caps_locked.sh \\$2 'sh' ] nous pouvons ouvrir un shell. En faisant un sudo -l nous nous aprecevons que l'on peut executer ce programme en tant que bobcat-gg qui lui à les droits de lecture du flag.

Final payload: sudo -u bobcat-gg ./caps_locked.sh \\$2 'sh'
