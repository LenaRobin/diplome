import json
#initialisation des variables
#data.json correspond au contenu de api.emergent.info/claims
data = json.loads(open("data.json").read())
main = "" 
nsharesindex = ""
shareslist = []
politic_strings = ("ISIS","Jihad","Jihadi John","Iraq","Israel","Gaza","Yemen","marines","manson","King of Jordan","Boko Haram","Taliban","sharia","saudi arabia","obama","Michele Bachmann","Boston marathon","Charlie hebdo","Fidel Castro","saudi","president","seal","buckingham palace","pope francis","Kim jong un","ferguson","Abu Bakr al Baghdadi","the euro","plot","elon university","putin","kurdish female fighter","kevin vickers","afghanistan","fort carson","cub of baghdadi","mass grave mexico","jong un","hand up dont shoot","pilot disowned","jongun","alBritani","Foley","syria","libya","Bary","North Korea")
economic_strings = ("apple","sell","selling","watch","TBS","Brian Williams","highest paid","IBM","iphone","Fox News","resort old snow","movie","big mac","sony","customer","NSA elf","video game","trader","ben edelman","microsoft","amazon","nbc meteorologist","lenovo","steve jobs","comcast","ios8","beats shutdown","LG","Gruber stainless steel","spicy condom")
sante_strings = ("GMO","Ebola","Planetary alignment","oldest tree","magneto boy","darkness","spider","crabzilla","hazmat","sashimi","third breast","meteorite","bear attack","bigfoot")
misc_strings = ("sex","lunch","tanker","castrated","release","testicles","porn","priest","bride","burger","Star wars","blogger","app ","snowy owl","suspects","bosnian girls","penis","Hobbit","pizza","catcallers","italian nun","baby","underwear","sell son","cat coat","pig brothel","homeless man","naked","college on fire","adulterous","woman in kfc","trans teen","dms","self rape","teletubbies","gay teacher","polar bear","fail video","text jesus","batmobile","man under atm","nhl vegas","thief")
people_strings = ("Tiger","Willie","shane smith","macklemore","Kanye","Michael jackson","Bruno Mars","Hugh Hefner","axel rose","Cesar Millan","lisa bonet","vogue","Taylor Lianne Chandler","Raven Symone","led zeppelin","Macaulay Culkin","paul rudd","judd nelson","banksy","ESPN domestic violence panel")
#cesar millan avec un accent chelou en vrai

#programme principal : on parse le fichier json et on en recupere ce qu'on veut.
for x in range(0,328):
    if data['claims'][x]['truthiness'] != 'true' and  data['claims'][x]['originUrl'] != None:# and data['claims'][x]['publishedat'][5:7]   [:4]>=  :
         
        main = ('<div class="news_info">' + '<div id=news' + str([x]) +'>' \
             + '<div class ="trueorfalse">"' + data['claims'][x]['truthiness'] + '"</div>' \
             + '<div class ="url">"' + data['claims'][x]['slug'] + '"</div>' \
             + '<div class ="title">"' + data['claims'][x]['headline'] + '"</div>' \
             + '<div class ="description">"' + data['claims'][x]['origin'] + '"</div>' \
             + '<div class ="date">"' + data['claims'][x]['publishedAt'][:10] + '"</div></div>'\
             + '<div class="news_article"><div class ="origine">"'\
             + data['claims'][x]['originUrl'] + '"</div><div class="article"></div></div>' \
             + '<div class="news_twitter"><div class ="share">"'\
             + str(data['claims'][x]['nShares']) + '"</div><div class="twitter_bloc"></div></div> \n').encode('utf8')
#            + '<div class ="pouroucontre">"' + data['claims'][x]['stances'] + '"</div>'\
#            + '<div class ="tags">"' + data['claims'][x]['tags'] + '"</div>'\
        titleindex = ('<div id="index_sommaire_title'+ str([x]) + '">' + data['claims'][x]['headline']+ '</div>\n <a href="#title'+ str([x]) + '"></a>').encode('utf8')
        shareslist.append([data['claims'][x]['nShares'] ,data['claims'][x]['headline'],x])        
        shareslist.sort(reverse = True) 


        if any(n in data['claims'][x]['slug'] for n in politic_strings): 
            result=file("test.html","r").read().replace('news_politic">', 'news_politic">' + main)
            file("test.html","w").write(result)
            result=file("test.html","r").read().replace('Partie 1</div>','Partie 1</div>\n'+ titleindex)
            file("test.html","w").write(result)
        
        elif any(n in data['claims'][x]['slug'] for n in economic_strings): 
            result=file("test.html","r").read().replace('news_economics">', 'news_economics">' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 2</div>','Partie 2</div>\n'+ titleindex)
            file("test.html","w").write(result)

        elif any(n in data['claims'][x]['slug'] for n in sante_strings): 
            result=file("test.html","r").read().replace('news_sante">','news_sante">' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 3</div>','Partie 3</div>\n'+ titleindex)
            file("test.html","w").write(result)
        
        elif any(n in data['claims'][x]['slug'] for n in people_strings): 
            result=file("test.html","r").read().replace('news_people">','news_people">' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 5</div>','Partie 5</div>\n'+ titleindex)

        elif any(n in data['claims'][x]['slug'] for n in misc_strings): 
            result=file("test.html","r").read().replace('news_miscellaneous">', 'news_miscellaneous" >' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Partie 4</div>','Partie 4</div>\n'+ titleindex)
            file("test.html","w").write(result)

        else:
            print("not found")
       
#for item in shareslist:
for i in range(len(shareslist)):  
    nsharesindex = '<span class ="share_numero">'  \
    + str(shareslist[i]).replace(', u\'Claim:','</span>\n<span class="share_descriptif">')[1:]
    nsharesindex = nsharesindex.replace('\', ','</span>\n<span class="share_page"><a href="#title[')
    nsharesindex = nsharesindex.replace(']',']"></a></span>') 
print(nsharesindex)
#remplacer "shared rumors<br>"


#en vrai l'ajouter au document en n'oubliant pas
#<div id = "colonne_share"> ... </id>

