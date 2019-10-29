"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import os





def get_fixed_filename(filename):
    
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():

    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)




demo_walk()
