#suppression des guillemets offerts gracieusement par google
sed -i 's/twitter_user">\t"/twitter_user">/g' tweets.html
sed -i 's/\."/\./g' tweets.html

#ajout de balises # et @
sed -i "s/#.\w*/<span class="lien">&<\/span>/g" tweets.html
sed -i "s/@.\w*/<span class="ate">&<\/span>/g" tweets.html
