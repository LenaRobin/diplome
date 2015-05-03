#!/bin/bash
# utilitymenu.sh - A sample shell script to display menus on screen
# Store menu options selected by the user
INPUT=/tmp/menu.sh.$$
 
# Storage file for displaying cal and date command output
OUTPUT=/tmp/output.sh.$$
 
# get text editor or fall back to vi_editor
vi_editor=${EDITOR-vi}
 
# trap and delete temp files
trap "rm $OUTPUT; rm $INPUT; exit" SIGHUP SIGINT SIGTERM
 
function display_output(){
	local h=${1-10}			# box height default 10
	local w=${2-41}			# box width default 41
	local t=${3-Output}		# box title 
	dialog --backtitle "Linux Shell Script Tutorial" --title "${t}" --clear --msgbox "$(<$OUTPUT)" ${h} ${w}
}
#
function display_info(){
local h=${1-10}                 # box height default 10
        local w=${2-41}                 # box width default 41
        local t=${3-Output}             # box title 
        dialog --infobox "$(<$OUTPUT)" 15 60 ; sleep 3
}
#
# Récupèrer du contenu sur emergent.info
#
function recup_emergent(){
	echo "Récupération des informations en cours..." >$OUTPUT
	display_info
	./emergent.sh #ajouter dialog dans le script
	echo "Récupération terminée." >$OUTPUT
    display_output 15 60 "Récupérer les informations"
}
#
# Purpose 
#
function search_twitter(){
	echo "Cette fonction n'est pas encore au point." >$OUTPUT
	display_output 10 50 "Rechercher des Tweets associés"
}
#
# Purpose 
#
function twitter_bot(){
	echo "Cette fonction n'est pas encore au point." >$OUTPUT
	display_output 10 50 "Lancer le robot de diffusion"
}
#
# Purpose 
#
function search_emergent(){
	echo "Cette fonction n'est pas encore au point." >$OUTPUT
	display_output 10 50 "Récupérer les articles de presse en ligne"
}
#
# set infinite loop
#
while true
do
 
### display main menu ###
dialog --clear  --help-button --backtitle "Projet diplome" \
--title "Menu" \
--menu "Bienvenue" 15 80 4 \
1 "Récupérer les informations" \
2 "Rechercher les Tweets associés " \
3 "Récupérer les articles de presse en ligne" \
4 "Lancer le robot de diffusion de la plateforme sur Twitter" 2>"${INPUT}"
 
menuitem=$(<"${INPUT}")
 
 
# make decsion 
case $menuitem in
	1) recup_emergent;;
	2) search_twitter;;
	3) search_emergent;;
	4) twitter_bot;;
esac
 
done
 
# if temp files found, delete em
[ -f $OUTPUT ] && rm $OUTPUT
[ -f $INPUT ] && rm $INPUT
