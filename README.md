# À faire

**récupérer le contenu des sites en lien dans les commentaires d'emergent**

**récupérer les liens sur les articles d'emergent, puis le contenu**

**recupérer des tweets plus anciens :**
https://github.com/Jefferson-Henrique/GetOldTweets/

**index par nom des rumeurs**
*harmoniser les noms des balises : il faut choisir entre title ou news*
```html
<a href="#title[234]"></a>
et
<div id="news[234]">```

*index par site d'origine*

*index par taux de partage*

*index des mots clés*

**bosser les liens internes :**

avoir un texte balisé avec des thématiques associées en fixe, avoir un flux d'actualité qui vient,
scanner le flux et voir si il y a des mots clés correspondant aux thématiques,
dès que ça correspond, ajouter :

```html
(See also "animals" page <a href="#animals"> </a>)
```

Exemple :
```html
"The story first made it into the press with the Daily Mail on Jan. 14. It cites a Russian TV report about a group of "investigators" who supplied footage of a Yeti (See also "animals" page <a href="#animals"></a>) in the Adygeya Republic. The images of the video were provided by Central European News, a newswire that has often been the source of false/dubious stories."
```

**changer div class="news" par div class="news" div id="news1", div id="news2" etc**

```html
<div class="news"><div id="news1">

<div class="trueorfalse"> "false"</div>  
<div class="url"> "sandwich-thief"</div>  
<div class="tags"> []</div>  
<div class="title2"> Two office workers in an epic battle over a stolen sandwich</div>  
<div class="description"> "It began to spread as real after being posted to Reddit, with the College Humor watermarks removed."</div>  
<div class="origin"> "http://www.reddit.com/r/funny/comments/2e6q4i/hi_tina_from_hr_again/%20"</div>  
<div class="share"> 108045</div>  
<div class="pouroucontre">     "ignoring": 1,    "for": 4,    "against": 2  </div>  
<div class="date"> "2014-08-26T20:33:29.558</div>
</div>
</div>
```

# Liste des index à mettre en place

**Index des noms des rumeurs (variable "title")**

Index/sommaire selon l'ordre du livre (par thème, puis par ordre chronologique de la plus récente à la plus ancienne)  
Nom de la partie 1  
rumeur 1, n°page  
rumeur 3, n°page  
Nom de la partie 2  
rumeur 2, n°page  
etc.  

```html
<div id="index_sommaire">  
  
<div class="index_partie">Partie 1</div>  
<div id="index_sommaire_title1">North Korea plans to open a restaurant in Scotland</div>  
<a href="#title1"></a>  

<div id="index_sommaire_title3">Two office workers in an epic battle over a stolen sandwich</div>  
<a href="#title3"></a>  
  
<div class="index_partie">Partie 2</div>  
<div id="index_sommaire_title2">North Korea plans to open a restaurant in Scotland</div>  
<a href="#title2"></a>  
  
</div>
```

**Index de la rumeur la plus partagée sur les réseaux (variable "share")**

Utiliser la variable "share"  
rumeur 4, nombre de partage, n°page  
rumeur 18, nombre de partage, n°page  
rumeur 2, nombre de partage, n°page  

```html
<div id="index_partage">  
  
<div id="index_partage_title4">North Korea plans to open a restaurant in Scotland</div>  
<div id="share4">111990999 shares</div>  
<a href="#title4"></a>  
  
<div id="index_partage_title18">Two office workers in an epic battle over a stolen sandwich</div>  
<div id="share18">856 shares</div>  
<a href="#title18"></a>  
  
</div>
```

**Index des rumeurs par url (variable "origin")**

Utiliser la variable "origin" et les classer par ordre alphabétique de A à Z.
rumeur 36, url (americanwebsite.com/blablabla), n°page  
rumeur 21, url (besthistory.com/blablabla), n°page  
rumeur 153, url (zebesthistory.com/blablabla), n°page  
  
Implique de retirer les préfixes :  
http://  
www.  
https://  
 
```html
<div id="index_url">  
  
<div id="index_url_title36">North Korea plans to open a restaurant in Scotland</div>  
<div id="origin36">americanwebsite.com/blablabla</div>  
<a href="#title36"></a>  
  
<div id="index_url_title21">Two office workers in an epic battle over a stolen sandwich</div>  
<div id="origin21">besthistory.com/blablabla</div>  
<a href="#title21"></a>  
  
</div>
```

**Index des mots-clés (variables "tags" et "url")**

Lister tous les mots-clés des rumeurs, utiliser les variables "tags" et "url" (url correspond au "slug" du site)    
america, n°page, n°page, n°page  
berlusconi, n°page, n°page, n°page  
cameron, n°page, n°page  
  
Rajouter une virgule et un espace dans chaque div  
```html
<a href="#title168">, </a>
```
  
N'implique pas de prédéfinir des mots-clés à l'avance, ils se mettent en place avec les nouvelles rumeurs.  
Implique de définir des variables dans le css avec get-string.  

```html
<div id="index_motscles">  
  
<div class="motscles1">america</div><a href="#title18"></a>, <a href="#title21">, </a><a href="#title37"></a>  
<div class="motscles2">berlusconi</div><a href="#title168">, </a><a href="#title23">, </a><a href="#title37"></a>  
<div class="motscles3">cameron</div><a href="#title90"></a>, <a href="#title56"></a>  




