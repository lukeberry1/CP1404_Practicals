import os

def main():

    os.chdir("FilesToSort")
    files = os.listdir(".")

    for filename in files:
        if os.path.isdir(filename):
            continue
        file_type = filename.split(".")[-1]
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass

        os.rename(filename, "{}/{}".format(file_type, filename))
main()