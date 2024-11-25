print ("Bien ? Tié le bienvenue dans la bijouterie, voici l'inventaire. Fais ton choix et rends pas fou")
print ("**")
print ("Il te faut quoi chef ?")
print ("1) Chaîne en or   2) Chaîne en argent")

choix = int(input("Fais ton choix : "))

compte = 2000
quantite = 0
inflation = 1.10

objet1 = "Chaîne en or"
prix1 = 2406.49
quantite1 = 3
inflation1 = (inflation + prix1)

objet2 = "Chaîne en argent"
prix2 = 1208.25
quantite2 = 5
inflation2 = (inflation + prix2)

if choix == 1 :

    print ("Tia prit la chaîne en or batard, rah oe tu vis hein")
    print (f"Tu prends bien la {objet1} ça te coûte {prix1} y'en a {quantite1} en tout chef")
    print ("**")
    print ("Tu veux mettre à jour la quantité chien ?")
    print ("1) Oui   2) Non")
    ajout = int(input("Entre la valeur de la quantité qu'il reste stp chef "))
    if ajout == 1 :
        print (f"Vous disposez de {compte}€")
        print ("Après inflation le prix des produits est de 10%")
        print (f"Le prix après inflation est de {inflation1}")
        print ("Y t'en faut combien trou du cul ? ")
        quantite = int(input())
        achat = prix1 * quantite
        if achat <= compte:
            compte -= achat
            quantite1 += quantite
            print (f"C'est bon le djain y te reste {compte}€ et y reste {quantite1} chaîne en or, fdp prends le reste stp j'ai des bouches à nourrir")
        else :
            print("Bah alors on a pas assez batard ? Retourne au charbon fdp")

if choix == 2 :
    print ("Tia prit la chaîne en argent batard, clando de merde")
    print (f"Tu prends bien la {objet2} ça te coûte {prix2} y'en a {quantite2} en tout chef")
    print ("**")
    print ("Tu veux mettre à jour la quantité chien ?")
    print ("1) Oui   2) Non")
    ajout = int(input("Entre la valeur de la quantité qu'il reste stp chef"))
    if ajout == 1 :
        print (f"Vous disposez de {compte}€")
        print ("Après inflation le prix des produits est de 10%")
        print (f"Le prix après inflation est de {inflation1}")
        print ("Y t'en faut combien trou du cul ?")
        quantite = int(input())
        achat = prix2 * quantite
        if achat <= compte:
            compte -= achat
            quantite1 += quantite
            print (f"C'est bon le djain y te reste {compte}€ et y reste {quantite2} chaîne en argent, fdp prends le reste stp j'ai des bouches à nourrir")
        else :
            print("Alors t'as pas assez batard ? Retourne au charbon fdp")