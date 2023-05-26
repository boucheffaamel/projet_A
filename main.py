#
import numpy as np

GCODE_FILE = "ProjetA.gcode"
# Supposing that phase slices are constant
PHASE_A_QUANTITY = 10
PHASE_B_QUANTITY = 40

# global variables
phase_nb = 0
phase_list = None
temperature_list = None
temperature_variation_list = None


# Open the file, read the content, close the file and return the content.
def read_file(_file_name):
    # read the content of the file in the list
    with open(_file_name, "r") as _file:
        _content = _file.readlines()
    # close the file
    _file.close()
    # return the content
    return _content


# will save the final produced file
def save_file(_file_name):

    return False


def modify_temperature():

    return False

#
# [F<rate>] The maximum movement rate of the move between the start and end point.
def modify_speed():

    return False


def modify_extruder():

    return False


def offset_position(_offset_X, _offset_Y):

    return False


# Fonction receives the slices number in the file.
# Function asks for th enumber of the phases, also the quantities for each phase.
def treat_phase_inputs(_nb_slices):
    global phase_nb
    input_text = ""
    print(f"Total slices numbers are {_nb_slices}.")
    while (not input_text.isdigit() or int(input_text) <= 0 or int(input_text) > _nb_slices):
        input_text = (input("Enter the number of phases (less than slices): "))
    phase_nb = int(input_text)

    global phase_list
    phase_list = [0] * phase_nb
    phase_total = 0
    for i in range(phase_nb-1):
        input_text = ""
        while (not input_text.isdigit() or (phase_total + int(input_text) > _nb_slices)):
            input_text = (input(f"Enter the phase {i+1} quantity (no more than {_nb_slices -phase_total}): "))
        phase_list[i] = int(input_text)
        phase_total = phase_total + phase_list[i]
    # the last phase we detect automatically
    phase_list[phase_nb-1] = _nb_slices - phase_total

    print("Here is the result of the inputs")
    for i in range(phase_nb):
        print(f"Phase {i+1} with quantity {phase_list[i]}")

# Function receives the temperatures (starting and ending) for phase A and B from the entry
# Function creates 2 tuples with variation values of each phase
def treat_temperature_inputs():
    global phase_list, temperature_list, temperature_variation_list
    temperature_list = [0] * (phase_nb+1)
    for i in range(phase_nb):
        input_text = ""
        while (not input_text.isdigit()):
            input_text = (input(f"Enter the start temperature for phase {i+1}: "))
        temperature_list[i] = int(input_text)
    #
    input_text = ""
    while (not input_text.isdigit()):
        input_text = (input(f"Enter the end temperature for phase {phase_nb}: "))
    temperature_list[phase_nb] = int(input_text)

    print(f"Temperature variations by phases.")
    temperature_variation_list = [0] * phase_nb
    for i in range(phase_nb):
        if i < phase_nb - 1:
            temperature_variation_list[i] = np.linspace(temperature_list[i], temperature_list[i+1], num=phase_list[i], endpoint=False)
        else:
            temperature_variation_list[i] = np.linspace(temperature_list[i], temperature_list[i + 1], num=phase_list[i])
        print(f"[{temperature_variation_list[i][0]} - {temperature_variation_list[i][phase_list[i]-1]}]")


# Function receives the speed (starting and ending) for phase A and B from the entry
# Function creates 2 tuples with variation values of each phase
def treat_speed_inputs():
    global phase_list, speed_list, speed_variation_list
    speed_list = [0] * (phase_nb+1)
    for i in range(phase_nb):
        input_text = ""
        while (not input_text.isdigit()):
            input_text = (input(f"Enter the starting speed for phase {i+1}: "))
        speed_list[i] = int(input_text)
    #
    input_text = ""
    while (not input_text.isdigit()):
        input_text = (input(f"Enter the ending speed for phase {phase_nb}: "))
    speed_list[phase_nb] = int(input_text)

    print(f"speed variations by phases.")
    speed_variation_list = [0] * phase_nb
    for i in range(phase_nb):
        if i < phase_nb - 1:
            speed_variation_list[i] = np.linspace(speed_list[i], speed_list[i+1], num=phase_list[i], endpoint=False)
        else:
            speed_variation_list[i] = np.linspace(speed_list[i], speed_list[i + 1], num=phase_list[i])
        print(f"[{speed_variation_list[i][0]} - {speed_variation_list[i][phase_list[i]-1]}]")


# get raw data from gcode file
gcode_content = read_file(GCODE_FILE)
# transfer to np array
np_array = np.array(gcode_content)
# get the list of the indexes wher the layer is changed
np_array_slice_indexes = (np.where(np_array == ";AFTER_LAYER_CHANGE\n"))[0]
#np_array_slice_indexes = (np.where(np_array[:4] == "G1 Z"))[0]
# get the list of the slices
np_array_sliced = np.split(np_array, np_array_slice_indexes)

nb_slices = int(len(np_array_sliced)-1)
treat_phase_inputs(nb_slices)

# input treatments for temperature
treat_temperature_inputs()
# input treatments for speed
treat_speed_inputs()

# just a line to put the breakpoint in case if we needed. Erase at the end of the project
test = 1
