#

GCODE_FILE = "ProjetA.gcode"


# Choose from the given list words one random word and return it.
def choose_word(words):
    return random.choice(words)


# Open the file, read the content, close the file and return the content.
def read_file(_file_name):
    # read the content of the file in the list
    with open(_file_name, "r") as _file:
        _content = _file.readlines()
    # close the file
    _file.close()
    # return the content
    return _content


def modify_temperature(_phase_A_start, _phase_A_end, _phase_B_start, _phase_B_end):

    return False

#
# [F<rate>] The maximum movement rate of the move between the start and end point.
def modify_speed(_phase_A_percent, _phase_B_percent):

    return False


def modify_extruder(_phase_A_percent, _phase_B_percent):

    return False


def offset_position(_offset_X, _offset_Y):

    return False


gcode_content = read_file(GCODE_FILE)

