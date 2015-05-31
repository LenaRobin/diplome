import json
#initialisation des variables
#data.json correspond au contenu de api.emergent.info/claims
data = json.loads(open("data.json").read())
main = "" 
nsharesindex = ""
titleindex = ""
shareslist = []
jojo = 0
politic_strings = ("ISIS","Jihad","Jihadi-John","Iraq","Israel","Gaza","Yemen","marines","manson","King-of-Jordan","Boko-Haram","Taliban","sharia","saudi-arabia","obama","Michele-Bachmann","Boston-marathon","Charlie-hebdo","Fidel-Castro","saudi","president","seal","buckingham-palace","pope-francis","Kim-jong-un","ferguson","Abu-Bakr-al-Baghdadi","the-euro","plot","elon-university","putin","kurdish-female-fighter","kevin-vickers","afghanistan","fort-carson","cub-of-baghdadi","mass-grave-mexico","jong-un","hand-up-dont-shoot","pilot-disowned","jongun","alBritani","Foley","syria","libya","Bary","North-Korea")
economic_strings = ("apple","sell","selling","watch","TBS","Brian-Williams","highest-paid","IBM","iphone","Fox-News","resort-old-snow","movie","big-mac","sony","customer","NSA-elf","video-game","trader","ben-edelman","microsoft","amazon","nbc-meteorologist","lenovo","steve-jobs","comcast","ios8","beats-shutdown","LG","Gruber-stainless-steel","spicy-condom")
misc_strings = ("GMO","Ebola","Planetary-alignment","oldest-tree","magneto-boy","darkness","spider","crabzilla","hazmat","sashimi","third-breast","meteorite","bear-attack","bigfoot","sex","lunch","tanker","castrated","release","testicles","porn","priest","bride","burger","Star-wars","blogger","app","snowy-owl","suspects","bosnian-girls","penis","Hobbit","pizza","catcallers","italian-nun","baby","underwear","sell-son","cat-coat","pig-brothel","homeless-man","naked","college-on-fire","adulterous","woman-in-kfc","trans-teen","dms","self-rape","teletubbies","gay-teacher","polar-bear","fail-video","text-jesus","batmobile","man-under-atm","nhl-vegas","thief")
people_strings = ("Tiger","tiger","willie-shane","Kanye","willie","shane","bruno-mars","bruno","hugh","hefner","lisa","bonet","taylor-lianne-chandler","raven-simone","macaulay-culkin","espn","rudd","zeppelin","domestic-violence","Willie-shane","smith","macklemore","kanye","michael-jackson","Bruno-Mars","Hugh-Hefner","axel-rose","Cesar-Millan","lisa-bonet","vogue","Taylor-Lianne-Chandler","Raven-Symone","led-zeppelin","Macaulay-Culkin","paul-rudd","judd-nelson","banksy","ESPN-domestic-violence-panel")
#cesar millan avec un accent chelou en vrai
#programme principal : on parse le fichier json et on en recupere ce qu'on veut.
for x in range(0,328):
    pdate = data['claims'][x]['publishedAt']
    if (data['claims'][x]['truthiness'] != 'true') and ((str(pdate[5:7]) in ('78') and str(pdate[3]) == '4') or ( str(pdate[5:7]) in ('01','02','03') and str(pdate[3]) == '5') ):
        #print(pdate)
        if data['claims'][x]['originUrl'] != None: 
            main = ('<div class="news">\n\n' + '<div id="news' + str(x) +'">' \
                 + '<div class ="title">' + data['claims'][x]['headline'] + '</div>' \
                 + '<div class ="description">' + data['claims'][x]['origin'] + '</div>' \
                 + '<div class ="date">\n' + data['claims'][x]['publishedAt'][:10] + '</div>'\
                 + '<div class="news_article"><div class ="origin">The rumor first appeared on:<br>\n' + data['claims'][x]['originUrl'] \
                 + '<br>Then, other websites peddled the rumor. Here are some examples found at this period.</div></div>'\
                 + '<div class="journal">\n\n\n\n</div>'
                 + '<div class="news_twitter"><div class ="share">The rumor has been shared '\
                 + str(data['claims'][x]['nShares']) + ' times on Twitter.<br>Below are the very first tweets. </div><div class="twitter_bloc">\n' \
                 +'<!--' + data['claims'][x]['slug'] + ' -fake -hoax -rumor -->\n\n\n</div></div></div></div> \n').encode('utf8')

        titleindex = ('<span class="index_sommaire_title'+ str(x) + '">' + data['claims'][x]['headline']+ '</span><br>\n <a href="#news'+ str(x) + '"></a>').encode('utf8')
        shareslist.append([data['claims'][x]['nShares'],data['claims'][x]['headline'],str(x)])        
        shareslist.sort() 


        if any(n in data['claims'][x]['slug'] for n in politic_strings): 
            result=file("test.html","r").read().replace('news_politic">', 'news_politic">' + main)
            file("test.html","w").write(result)
            result=file("test.html","r").read().replace('Political Field<br><br>','Political Field<br><br>\n'+ titleindex)
            file("test.html","w").write(result)
        
        elif any(n in data['claims'][x]['slug'] for n in economic_strings): 
            result=file("test.html","r").read().replace('news_economics">', 'news_economics">' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Economics & Technology<br><br>','Economics & Technology<br><br>\n'+ titleindex)
            file("test.html","w").write(result)

#        elif any(n in data['claims'][x]['slug'] for n in sante_strings): 
#            result=file("test.html","r").read().replace('news_sante">','news_sante">' + main)
#            file("test.html","w").write(result)
            #index
#            result=file("test.html","r").read().replace('Public Health & Environment<br><br>','Public Health & Environment<br><br>\n'+ titleindex)
#            file("test.html","w").write(result)
        
        elif any(n in data['claims'][x]['slug'] for n in people_strings): 
            result=file("test.html","r").read().replace('news_people">','news_people">' + main)
            file("test.html","w").write(result)
            #index
            print(pdate)
            result=file("test.html","r").read().replace('People<br><br>','People<br><br>\n'+ titleindex)
            file("test.html","w").write(result)

        elif any(n in data['claims'][x]['slug'] for n in misc_strings): 
            result=file("test.html","r").read().replace('news_miscellaneous">','news_miscellaneous">' + main)
            file("test.html","w").write(result)
            #index
            result=file("test.html","r").read().replace('Miscellaneous<br><br>','Miscellaneous<br><br>\n'+ titleindex)
            file("test.html","w").write(result)

        else:
            jojo=1
       
#for item in shareslist:
#il faut rajouter des balises <br> a la fin de chaque span
for i in range(len(shareslist)):  
    nsharesindex = '\n<span class="share_numero">'  \
    + str(shareslist[i]).replace(', u','</span><br>\n<span class="share_descriptif">')[1:]
    nsharesindex = nsharesindex.replace(', \'','</span>\n<span class="share_page"><a href="#title')
    nsharesindex = nsharesindex.replace('\']','"></a></span><br>') 
#    print(nsharesindex)
#remplacer "shared rumors<br>"
    result=file("test.html","r").read().replace('shared rumors<br><br>','shared rumors<br><br>'+nsharesindex)
    file("test.html","w").write(result)
#en vrai l'ajouter au document en n'oubliant pas
#<div id = "colonne_share"> ... </id>

