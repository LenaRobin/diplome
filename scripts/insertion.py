import json
#initialisation des variables
#data.json correspond au contenu de api.emergent.info/claims
data = json.loads(open("data.json").read())
main = "" 
politic_strings = ("ISIS","Jihad","Jihadi John" )
economic_strings = ("apple","sell","selling")
sante_strings = ("GMO","Ebola","Planetary alignment")
misc_strings = ("sex","lunch","tanker")
people_strings = ("Tiger","Willie","shane smith")




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
        
        if any(n in data['claims'][x]['slug'] for n in politic_strings): 
            result=file("test.html","r").read().replace('news_politic" >', 'news_politic" >' + main)
            file("test.html","w").write(result)
            result=file("test.html","r").read().replace('Partie 1</div>','Partie 1</div>\n'+ titleindex)
            file("test.html","w").write(result)
        
        elif any(n in data['claims'][x]['slug'] for n in economic_strings): 
            result=file("test.html","r").read().replace('news_economics" >', 'news_economics" >' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 2</div>','Partie 2</div>\n'+ titleindex)
            file("test.html","w").write(result)

        elif any(n in data['claims'][x]['slug'] for n in sante_strings): 
            result=file("test.html","r").read().replace('news_sante" >','news_sante" >' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 3</div>','Partie 3</div>\n'+ titleindex)
            file("test.html","w").write(result)
        
        elif any(n in data['claims'][x]['slug'] for n in people_strings): 
            result=file("test.html","r").read().replace('news_people" >','news_people" >' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 5</div>','Partie 5</div>\n'+ titleindex)

        elif any(n in data['claims'][x]['slug'] for n in misc_strings): 
            result=file("test.html","r").read().replace('news_miscellaneous" >', 'news_miscellaneous" >' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 4</div>','Partie 4</div>\n'+ titleindex)
            file("test.html","w").write(result)

        else:
            print("not found")

