#
import numpy as np

GCODE_FILE = "fichier_entree.gcode"
# Supposing that phase slices are constant
PHASE_A_QUANTITY = 10
PHASE_B_QUANTITY = 40


# Open the file, read the content, close the file and return the content.
def read_file(_file_name):
    # read the content of the file in the list
    with open(_file_name, "r") as _file:
        _content = _file.readlines()
    # close the file
    _file.close()
    # return the content
    return _content

def save_file(_file_name,np_array):
    content=list(np_array)
    with open(_file_name, "w") as _file:
        _file.writelines(content)
    _file.close()
#
# [F<rate>] The maximum movement rate of the move between the start and end point.

def modify_extruder():

    return False


def offset_position(_offset_X, _offset_Y):

    return False


# Function receives the temperatures (starting and ending) for phase A and B from the entry
# Function creates 2 tuples with variation values of each phase
def treat_temperature_inputs():
    global temperature_start_A, temperature_end_A, temperature_start_B, temperature_end_B
    global temperature_variation_A, temperature_variation_B
    temperature_start_A = int(input("Enter the start temperature for phase A: "))
    temperature_end_A = int(input("Enter the end temperature for phase A: "))
    temperature_start_B = int(input("Enter the start temperature for phase B: "))
    temperature_end_B = int(input("Enter the end temperature for phase B: "))
    temperature_variation_A = np.linspace(temperature_start_A, temperature_end_A, num=PHASE_A_QUANTITY, endpoint=False)
    temperature_variation_B = np.linspace(temperature_start_B, temperature_end_B, num=PHASE_B_QUANTITY)

def treat_speed_inputs():
    global speed_start_A, speed_end_A, speed_start_B, speed_end_B
    global speed_variation_A, speed_variation_B
    speed_start_A = int(input("Enter the starting speed for phase A: "))
    speed_end_A = int(input("Enter the ending speed for phase A: "))
    speed_start_B = int(input("Enter the starting speed for phase B: "))
    speed_end_B = int(input("Enter the ending speed for phase B: "))
    speed_variation_A = np.linspace(speed_start_A, speed_end_A, num=PHASE_A_QUANTITY, endpoint=False)
    speed_variation_B = np.linspace(speed_start_B, speed_end_B, num=PHASE_B_QUANTITY)



def modify_temperature(np_array_sliced):
    # index pour suivre les variations de température
    temperature_index_A = 0
    temperature_index_B = 0

    # parcourir les tranches du tableau numpy
    for  i, slice in enumerate(np_array_sliced):
        # vérifier si nous sommes dans la phase A ou B
        if i < PHASE_A_QUANTITY:
            # obtenir la variation de température pour cette tranche
            temperature_variation = temperature_variation_A[temperature_index_A]
            # incrémenter l'index de température pour la phase A
            temperature_index_A += 1
        else:
            # obtenir la variation de température pour cette tranche
            temperature_variation = temperature_variation_B[temperature_index_B]
            # incrémenter l'index de température pour la phase B
            temperature_index_B += 1
        #construire la nouvelle commande de température
        temperature_command="M104 S"+str(temperature_variation)+"\n"
        #inserer la nouvelle commande de temperature au debut de la tranche
        np_array_sliced[i] = np.insert(slice, 0,temperature_command)

    return np_array_sliced


def modify_speed(np_array_sliced):
    # index pour suivre les variations de vitesse
    speed_index_A = 0
    speed_index_B = 0

    # parcourir les tranches du tableau numpy
    for i, slice in enumerate(np_array_sliced):
        # vérifier si nous sommes dans la phase A ou B
        if i < PHASE_A_QUANTITY:
            # obtenir la variation de vitesse pour cette tranche
            speed_variation = speed_variation_A[speed_index_A]
            # incrémenter l'index de vitesse pour la phase A
            speed_index_A += 1
        else:
            # obtenir la variation de vitesse pour cette tranche
            speed_variation = speed_variation_B[speed_index_B]
            # incrémenter l'index de vitesse pour la phase B
            speed_index_B += 1

        # parcourir les lignes de la tranche
        for j, line in enumerate(slice):
            # vérifier si la ligne contient une instruction de vitesse
            if line.startswith("G1") and "F" in line:
                # diviser la ligne en parties
                line_parts = line.split(" ")
                # parcourir les parties de la ligne
                for k, part in enumerate(line_parts):
                    # vérifier si cette partie contient une instruction de vitesse
                    if part.startswith("F"):
                        # obtenir la vitesse actuelle
                        current_speed = float(part[1:])
                        # calculer la nouvelle vitesse
                        new_speed = current_speed * (1 + speed_variation / 100)
                        # mettre à jour la partie avec la nouvelle vitesse
                        line_parts[k] = "F" + str(new_speed)
                # reconstruire la ligne avec les parties mises à jour
                new_line = " ".join(line_parts)
                # mettre à jour la ligne dans la tranche
                slice[j] = new_line

    return np_array_sliced

# get raw data from gcode file
gcode_content = read_file(GCODE_FILE)
# transfer to np array
np_array = np.array(gcode_content)
# get the list of the indexes wher the layer is changed
np_array_slice_indexes = (np.where(np_array == ";AFTER_LAYER_CHANGE\n"))[0]
# get the list of the slices
np_array_sliced = np.split(np_array, np_array_slice_indexes)

# input treatments for temperature
treat_temperature_inputs()
# input treatments for speed
treat_speed_inputs()
#ajouter les commandes M104 et la variation dans le tableau numpy
np_array_sliced=modify_temperature(np_array_sliced)
#modifier les instruction de vitesse dan le tableau numpy
np_array_sliced=modify_speed(np_array_sliced)
#enregistrer le resultat dans un fichier gcoe de sortie
save_file("fichier_sortie.gcode",np.concatenate(np_array_sliced))


