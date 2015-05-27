#!/bin/sh
#supprimer en début de description
sed -i "s#\"Claim: ##g" test.html
sed -i "s#'Claim: ##g" test.html
sed -i "s#Claim: ##g" test.html
sed -i "s#'</s#</s#g" test.html
sed -i "s#\"</s#</s#g" test.html
sed -i "s#tif\">'#tif\">#g" test.html

