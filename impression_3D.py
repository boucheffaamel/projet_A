
def modifier_temperature_gcode(temperature_initiale,temperature_finale,hauteur_couche):
    #ouvrir le fichier de lecture gcode
    with open ('fichier_entree.gcode','r')as f_entree:

        #ouvrir le fichier de sortie
        with open ('fichier_sortie.gcode','w')as f_sortie:
            lignes = f_entree.readlines()
            couche_actuelle=1
            #parcourir chaque ligne dans le fichier d'entree
            for ligne in lignes:
                #verifier si la ligne contient un changement de couche
                if ligne.startswith(';LAYER:'):
                    couche_actuelle +=1
                #verifier si la ligne contient un changement de tepmérature
                    if ligne.startswith('G1'):
                        # calculer la nouvelle température en foncion de la couche actuelle
                        poucentage = couche_actuelle / hauteur_couche
                        nouvelle_temp = temperature_initiale + poucentage * (temperature_finale - temperature_initiale)
                        ligne += f' M104 S{nouvelle_temp[couche_actuelle]}\n'
                    #modifier la ligne du gcode avec la nouvelle température
                    f_sortie.write(ligne)

temperature_initiale=180
temperature_finale=220
hauteur_couche=50
modifier_temperature_gcode(temperature_initiale,temperature_finale,hauteur_couche)