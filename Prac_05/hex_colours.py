HEX_COLOURS = {"Alice Blue": "0f8ff", "Antique White": "faebd7", "Antique White 1": "ffefdb",
               "Antique White 2": "eedfcc", "Antique White 3": "cdc0b0", "Antique White 4": "8b8378",
               "aqua marine 1": "7fffd4", "aqua marine 2": "76eec6", "aqua marine 4": "458b74", "azure 1": "f0ffff"}

colour = input("Enter colour: ").upper()
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "index is", HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()
