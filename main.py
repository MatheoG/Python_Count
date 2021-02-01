#tableau des carcatères
charTab=[
	'0','1'
] 

#longeur de la donnée de sortie
dataLength = 4
tab=[0]*dataLength

def AddUnit(i):
    if(tab[i]==len(charTab)-1):
        tab[i]=0
        AddUnit(i+1)
    else:
        tab[i]=tab[i]+1
    return tab

def tabToStr():
    x=0
    srtR = ""
    while(x<len(tab) and tab[x]!=-1):
        srtR=charTab[tab[x]]+srtR
        x=x+1
    return(srtR)

for i in range(len(charTab)**len(tab)-1):
    if(tab[0]==len(charTab)-1):
        AddUnit(0)
        tab[0]=0
    else:
        tab[0]=tab[0]+1
    r= tabToStr()
    print(r)
