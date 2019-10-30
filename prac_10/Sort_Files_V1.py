import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_type = filename.split('.')[-1]
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass
        print("{}/{}/{}".format(filename, file_type, filename))
        os.rename(filename, "{}/{}".format(file_type, filename))


main()
