# diplome

# à faire

**récupérer le contenu des sites en lien dans les commentaires d'emergent**

**récupérer les liens sur les articles d'emergent, puis le contenu**

**recupérer des tweets plus anciens :**
https://github.com/Jefferson-Henrique/GetOldTweets/

**emergent sont des vendus (cimer Craig)**

**bosser les indexes :**

*index par nom des rumeurs*

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

"The story first made it into the press with the Daily Mail on Jan. 14. It cites a Russian TV report about a group of "investigators" who supplied footage of a Yeti (See also "animals" page <a href="#animals"></a>) in the Adygeya Republic. The images of the video were provided by Central European News, a newswire that has often been the source of false/dubious stories."

**changer div class="news" par div class="news" div id="news1", div id="news2" etc**

```html
<div class="news"><div id="news1">

<div class="trueorfalse"> "false"</div><div class="url"> "sandwich-thief"</div><div class="tags"> []</div><div class="title2"> Two office workers in an epic battle over a stolen sandwich"</div><div class="description"> "It began to spread as real after being posted to Reddit, with the College Humor watermarks removed."</div><div class="origin"> "http://www.reddit.com/r/funny/comments/2e6q4i/hi_tina_from_hr_again/%20"</div><div class="share"> 108045</div><div class="pouroucontre">     "ignoring": 1,    "for": 4,    "against": 2  </div><div class="date"> "2014-08-26T20:33:29.558</div>
</div>
</div>
```
