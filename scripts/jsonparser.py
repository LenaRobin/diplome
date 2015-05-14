import json

#initialisation des variables
#data.json correspond au contenu de api.emergent.info/claims
data = json.loads(open("data.json").read())
main = "" 
fichierhtml = 'test.html' 

#programme principal : on parse le fichier json et on en recupere ce qu'on veut.
for x in range(0, 10):
    if data['claims'][x]['truthiness'] != 'true': 
        main += ('<div class="news">' + '<div id=news' + str([x]) +'>' \
             + '<div class ="trueorfalse">"' + data['claims'][x]['truthiness'] + '"</div>' \
             + '<div class ="url">"' + data['claims'][x]['slug'] + '"</div>' \
             + '<div class ="title">"' + data['claims'][x]['headline'] + '"</div>' \
             + '<div class ="description">"' + data['claims'][x]['origin'] + '"</div>' \
             + '<div class ="origine">"' + data['claims'][x]['originUrl'] + '"</div>' \
             + '<div class ="share">"' + str(data['claims'][x]['nShares']) + '"</div>' \
             + '<div class ="date">"' + data['claims'][x]['publishedAt'][:10] + '"</div>'\
             + '</div></div>\n').encode("utf8")
#            + '<div class ="pouroucontre">"' + data['claims'][x]['stances'] + '"</div>'\
#            + '<div class ="tags">"' + data['claims'][x]['tags'] + '"</div>'\

Fichier = open(fichierhtml,'w')
Fichier.write(main)
Fichier.close()

