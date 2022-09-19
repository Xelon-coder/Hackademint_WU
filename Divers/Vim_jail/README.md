La première jail est vraiment trop simple pour le coup, en appuyant sur q on quitte la jail et on a accès au bash directement.

La seconde est assez classique pour une vim jail/privesc il suffit de faire :
:set shell=/bin/bash
:shell

La dernière est la même que la seconde sauf que nous sommes bloqués dans le mode insert en faisant Ctrl^O on peut sortir et faire le même payload que pour la seconde pour obtenir un shell
