import os
def main():
    os.chdir("FilesToSort")
    category = {}
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue
        extension = filename.split('.')[-1]

        if extension not in category:
            new_category = input("what category will {} file be in".format(extension))
            category[extension] = new_category
            try:
                os.mkdir(new_category)
            except FileExistsError:
                pass

        os.rename(filename, "{}/{}".format(category[extension], filename))


main()