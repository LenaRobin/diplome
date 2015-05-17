import json
#initialisation des variables
#data.json correspond au contenu de api.emergent.info/claims
data = json.loads(open("data.json").read())
main = "" 

#programme principal : on parse le fichier json et on en recupere ce qu'on veut.
for x in range(0,328):
    if data['claims'][x]['truthiness'] != 'true' and  data['claims'][x]['originUrl'] != None:# and data['claims'][x]['publishedat'][5:7]   [:4]>=  :
         
        main = ('<div class="news_info">' + '<div id=news' + str([x]) +'>' \
             + '<div class ="trueorfalse">"' + data['claims'][x]['truthiness'] + '"</div>' \
             + '<div class ="url">"' + data['claims'][x]['slug'] + '"</div>' \
             + '<div class ="title">"' + data['claims'][x]['headline'] + '"</div>' \
             + '<div class ="description">"' + data['claims'][x]['origin'] + '"</div>' \
             + '<div class ="date">"' + data['claims'][x]['publishedAt'][10] + '"</div></div>'\
             + '<div class="news_article"><div class ="origine">"'\
             + data['claims'][x]['originUrl'] + '"</div><div class="article"></div></div>' \
             + '<div class="news_twitter"><div class ="share">"'\
             + str(data['claims'][x]['nShares']) + '"</div><div class="twitter_bloc"></div></div> \n').encode('utf8')
#            + '<div class ="pouroucontre">"' + data['claims'][x]['stances'] + '"</div>'\
#            + '<div class ="tags">"' + data['claims'][x]['tags'] + '"</div>'\
        titleindex = ('<div id="index_sommaire_title'+ str([x]) + '">' + data['claims'][x]['headline']+ '</div>\n <a href="#title'+ str([x]) + '"></a>').encode('utf8')
        
        if "zashini" in data['claims'][x]['slug']: 
            result=file("test.html","r").read().replace("jambon", "jambon" + main)
            file("test.html","w").write(result)
            result=file("test.html","r").read().replace("saucisse", "saucisse" + titleindex)
            file("test.html","w").write(result)
        
        elif "penis" in data['claims'][x]['slug']:
            result=file("test.html","r").read().replace("salami", "salami" + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace("saucisse", "saucisse" + titleindex)
            file("test.html","w").write(result)

        elif "ISIS" in data['claims'][x]['slug']:
            result=file("test.html","r").read().replace("fromage", "fromage" + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace("saucisse", "saucisse" + titleindex)
            file("test.html","w").write(result)
        
#        elif "ISIS" in data['claims'][x]['slug']:
#            result=file("test.html","r").read().replace("fromage", "fromage" + main)
#            file("test.html","w").write(result)
#            #index
#            result=file("test.html","r").read().replace("saucisse", "saucisse" + titleindex)

        else :
            result=file("test.html","r").read().replace("oeuf", "oeuf" + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace("saucisse", "saucisse" + titleindex)
            file("test.html","w").write(result)
        


