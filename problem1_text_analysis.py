#ENONCE
phrase=input("Entrer un phrase:")

phrase=phrase.lower()

mots=phrase.split()

#AFFICHE

#le nombre total de mot dans la phrase
nbrmot=len(mots)
print("le nombre total de mot dans cette phrase est:",nbrmot)

#le plus long mot
long =mots[0]
for i in mots:
    if len(i) > len(long):
        long=i
print("le mot le plus long est",long)

#le nombre de voyelle dans la phrase
voyelle=0
for i in phrase:
    if i in "aeiouy":
        voyelle+=1
print("cette phrase contient",voyelle,"voyelles")

#Construire une nouvelle phrase dans laquelle les mots de longueur paire sont son convertis en majuscule et les mots de longuer impaire reste intacte en utilisant les fonctions
def convert(mot):
    if len(mot)%2==0:
        return mot.upper()
    else:
        return mot
nouvelle_phrase=""
for i in mots:
    nouvelle_phrase+=convert(i)+" " 
print("la nouvelle phrase est:",nouvelle_phrase)



