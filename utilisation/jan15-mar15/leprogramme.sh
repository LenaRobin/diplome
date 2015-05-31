#!/bin/sh
echo "copie du fichier à editer"
cp HtmlARemplir.html test.html

echo "programme python"
python insertion.py

echo "modifications"
sed -i "s#\"Claim: ##g" test.html
sed -i "s#'Claim: ##g" test.html
sed -i "s#Claim: ##g" test.html
sed -i "s#'</s#</s#g" test.html
sed -i "s#\"</s#</s#g" test.html
sed -i "s#tif\">'#tif\">#g" test.html
#sed -i "s/#.\w*/<balise>&<\/balise>/g" tweets.html

echo "bravobravobravo"
