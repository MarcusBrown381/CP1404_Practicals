import os


def main():
    category_dict = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_type = filename.split('.')[-1]
        if file_type not in category_dict:
            new_category = input("What category would you like to sort {} files into?".format(file_type))
            category_dict[file_type] = new_category
            try:
                os.mkdir(new_category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(category_dict[file_type], filename))


main()
