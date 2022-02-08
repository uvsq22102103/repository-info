def virguleEnPoint(mot):
    if ',' in mot:
        chiffre = mot.replace(',','.')
        return(chiffre)
    else:
        return(mot)

entree = input('Entrez des notes\n')
liste = entree.split()
x=0
print (liste, len(liste))

for i in range(0,len(liste)) :
    if len(liste[i-x]) >= 6:
        del liste[i-x]
        x += 1
    elif "ABJ" in liste[i-x]:
        del liste[i-x]
        x += 1
    elif "en" in liste[i-x]:
        del liste[i-x]
        x += 1
    else:
        continue
print (liste)

#fonctionnel
liste2 = float()
liste3 = 0
liste4 = 0
for i in range (0,len(liste)):
    liste2 += float(virguleEnPoint(str(liste[i])))
    if float(virguleEnPoint(str(liste[i]))) >= 10.0:
        liste3 += 1
    elif float(virguleEnPoint(str(liste[i]))) >= 2.5:
        liste4 += 1
print("Sur",len(liste),"notes, la moyenne est de",round(liste2/len(liste),2),"\n et le pourcentage de notes au dessus de 10 est de",round(liste3/len(liste)*100,2),"%\n et le pourcentage de notes au dessus de 2.5 est de",round(liste4/len(liste)*100,2),"%")
