#
import numpy as np

GCODE_FILE = "ProjetA.gcode"
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


# Function receives the speed (starting and ending) for phase A and B from the entry
# Function creates 2 tuples with variation values of each phase
def treat_speed_inputs():
    global speed_start_A, speed_end_A, speed_start_B, speed_end_B
    global speed_variation_A, speed_variation_B
    speed_start_A = int(input("Enter the starting speed for phase A: "))
    speed_end_A = int(input("Enter the ending speed for phase A: "))
    speed_start_B = int(input("Enter the starting speed for phase B: "))
    speed_end_B = int(input("Enter the ending speed for phase B: "))
    speed_variation_A = np.linspace(speed_start_A, speed_end_A, num=PHASE_A_QUANTITY, endpoint=False)
    speed_variation_B = np.linspace(speed_start_B, speed_end_B, num=PHASE_B_QUANTITY)


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

# just a line to put the breakpoint in case if we needed. Erase at the end of the project
test = 1
