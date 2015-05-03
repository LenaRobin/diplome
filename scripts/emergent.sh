#!/bin/sh

#---------------------------------------------#
#			Récupération du contenu			  #
#---------------------------------------------#
curl -s http://api.emergent.info/claims | jq '.claims[] | 
	{trueorfalse:.truthiness,
	url:.slug,
	tags:.tags,
	title:.headline,
	description:.origin,
	origine:.originUrl,
	share:.nShares,
	pouroucontre:.stances,
	date:.publishedAt,
	}' > contenu_emergent.txt

echo "\n Le contenu est récupéré sur emergent.info"

#---------------------------------------------#
#		Traitement de texte et mise en forme			  #
#---------------------------------------------#
#il y a des \ ajoutés devant les " à l'intérieur du texte, on les supprime
sed -i -e 's/\\\"/\"/g' contenu_emergent.txt
#ensuite, on supprime les {} pour que le texte soit découpé en paragraphes
sed -i 's/{//g;s/}//g' contenu_emergent.txt
#on veut maintenant ajouter les balises <div>, il y a quelques subtilités :
sed -i -e 's/\"trueorfalse\"\:/\<\/div\>\<div\ class\=\"trueorfalse\"\>/g' contenu_emergent.txt
sed -i -e 's/\"url\"\:/\<\/div\>\<div\ class\=\"url\"\>/g' contenu_emergent.txt
sed -i -e 's/\"tags\"\:/\<\/div\>\<div\ class\=\"tags\"\>/g' contenu_emergent.txt
sed -i -e 's/\"title\"\:\ \"/\<\/div\>\<div\ class\=\"title\"\>/g' contenu_emergent.txt
sed -i -e 's/Claim\://g' contenu_emergent.txt #on suppr "Claim:
sed -i -e 's/\"description\"\:/\<\/div\>\<div\ class\=\"description\"\>/g' contenu_emergent.txt
sed -i -e 's/\"origine\"\:/\<\/div\>\<div\ class\=\"origin\"\>/g' contenu_emergent.txt
sed -i -e 's/\"share\"\:/\<\/div\>\<div\ class\=\"share\"\>/g' contenu_emergent.txt
sed -i -e 's/\"pouroucontre\"\:/\<\/div\>\<div\ class\=\"pouroucontre\"\>/g' contenu_emergent.txt
sed -i -e 's/\"date\"\:/\<\/div\>\<div\ class\=\"date\"\>/g' contenu_emergent.txt
#il faut encore ajouter un </div> tout à la fin
echo "\<\/div\>" >> contenu_emergent.txt
#on supprime TOUS les retours à la ligne pour mieux trier par la suite
cat contenu_emergent.txt | tr -d '\n' > contenu_ligne.txt
#et supprimer celui tout au début (on supprime les 1ers caractères du fichier)
sed -i -e 's/^........//' contenu_ligne.txt
#on supprime le fichier devenu obsolète
rm contenu_emergent.txt
#on ajoute un retour à la ligne à la fin de chaque bloc : une rumeur par ligne
sed -i -e 's+Z"  </div>+</div>\n+g' contenu_ligne.txt
#et on supprime les virgules de fin de div
sed -i -e 's+,\ \ </div>+</div>+g' contenu_ligne.txt
#on supprime les rumeurs "true"
grep -v '"true"' contenu_ligne.txt > contenu_notrue.txt
#on supprime les fichiers temporaires
#rm contenu_ligne.txt
echo "Le contenu est mis en forme, on a effectué un premier tri"
#avant d'insérer le texte, on prend le soin de protéger certains caractères :
#en ajoutant des \ devant
sed -i -e 's+\"+\\\"+g' contenu_notrue.txt
sed -i -e "s/'/\\\'/g" contenu_notrue.txt
sed -i -e "s/%/\\\%/g" contenu_notrue.txt
sed -i -e "s/+/\\\+/g" contenu_notrue.txt
sed -i -e "s/&/\\\&/g" contenu_notrue.txt

#---------------------------------------------#
#			Recuperation des tags			  #
#---------------------------------------------#

#ecrire une fonction

#---------------------------------------------#
#		Insertion dans le fichier html		  #
#---------------------------------------------#

#on copie maintenant les lignes une à une dans le document html, on ajoute des balises autour et des sauts de ligne.
#on compte d'abord le nombre de lignes que l'on a :
nblignes=`wc -l contenu_notrue.txt | head -c3`
#puis on fait une boucle
i=1 # on initialise le compteur
while [ $i -le $nblignes ]; do
  ligne_emergent=`sed -n ' '"$i"'p' contenu_notrue.txt`
#  python pour recupérer les tags, faire la recherche sur twitter, ajouter les balises
#passer ligne_emergent en entrée du script python
#on utilise le fichier contenu_notrue.txt
#on obtient ligne_twitter
# a rajouter dans sed : les twits	
  sed -i -e 's+partie-news\">+partie-news\">\n\n<div class=\"news\">'"$ligne_emergent"'</div>+' testfile.html
  i=$(($i + 1))
done
#on supprime le fichier qui ne sert plus à rien
rm contenu_notrue.txt
echo "Le contenu récupéré sur emergent.info a été ajouté au fichier html" 



#à modifier par la suite pour gagner du temps:
#   sed '/foo/ s/foo/bar/g' nomdefichier   # exécution plus rapide
