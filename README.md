# projet_A
 
Ce code est un script Python qui modifie un fichier G-code. Le G-code est un langage de programmation utilisé pour contrôler les machines-outils à commande numérique, telles que les imprimantes 3D. Ce script lit un fichier G-code d’entrée et permet à l’utilisateur de modifier les paramètres de température et de vitesse pour deux phases différentes (A et B) en entrant les températures et vitesses de départ et de fin pour chaque phase. Le script calcule ensuite les variations de température et de vitesse pour chaque tranche de la phase et modifie les commandes de température (M104) et de vitesse (F) dans le fichier G-code en conséquence.

"fichier_entree.gcode": le fichier G-code d'entrée à lire. 


« PHASE_A_QUANTITY = 10 »: définit une variable « PHASE_A_QUANTITY » qui contient le nombre de tranches pour la phase A. 

 « PHASE_B_QUANTITY = 40 »: définit une variable « PHASE_B_QUANTITY » qui contient le nombre de tranches pour la phase B. 


Ouvrir le fichier gcode en mode lecture ("r"), lire son contenu ligne par ligne et stocke dans une liste (_content), fermer le fichier et renvoie la liste. 


Ouvrir un fichier output qui   prend en entrée un nom de fichier et un tableau numpy, convertit le tableau en liste (content) et sauvegarde son contenu dans le fichier spécifié. Elle ouvre le fichier en mode écriture ("w"), écrit les lignes de la liste dans le fichier, ferme le fichier. 



La fonction treat_temperature_inputs():demande à l'utilisateur d'entrer les températures de départ et de fin pour les phases A et B, puis calcule les variations de température pour chaque tranche de chaque phase en utilisant la fonction « np.linspace » de la bibliothèque numpy. Les variations de température sont stockées dans les variables globales « temperature_variation_A » et « temperature_variation_B ». 


La fonction treat_speed_inputs():demande à l'utilisateur d'entrer les vitesses de départ et de fin pour les phases A et B, puis calcule les variations de vitesse pour chaque tranche de chaque phase en utilisant la fonction « np.linspace »de la bibliothèque numpy. Les variations de vitesse sont stockées dans les variables globales « speed_variation_A » et « speed_variation_B ». 


La fonction  modify_temperature(np_array_sliced): prend en entrée un tableau numpy contenant des tranches de G-code et modifie les commandes de température (M104) pour chaque tranche en fonction des variations de température calculées précédemment. Elle parcourt les tranches du tableau, vérifie si la tranche appartient à la phase A ou B, obtient la variation de température correspondante, construit une nouvelle commande de température (M104) avec cette variation et insère cette commande au début de la tranche. 


La fonction  modify_speed(np_array_sliced): prend en entrée un tableau numpy contenant des tranches de G-code et modifie les commandes de vitesse (F) pour chaque tranche en fonction des variations de vitesse calculées précédemment. Elle parcourt les tranches du tableau, vérifie si la tranche appartient à la phase A ou B, obtient la variation de vitesse correspondante, puis parcourt les lignes de la tranche pour trouver les instructions de vitesse (F). Pour chaque instruction de vitesse trouvée, elle calcule la nouvelle vitesse en appliquant la variation de vitesse, met à jour l'instruction avec la nouvelle vitesse et reconstruit la ligne avec les parties mises à jour. 





