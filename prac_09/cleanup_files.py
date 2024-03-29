import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        shutil.move(filename, 'temp/' + new_name)

# TODO: Finish this bit
def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
#   Tried a few things. No idea how to do this bit.
#    character_list = []
#    for character in enumerate(new_name):
#        character_list.append(character[-1])
# How to check two values against each other while looping???
#        if character_list[character].islower() and character_list[character + 1].isupper() in character_list:
# Replace space between lower-case letter and upper-case letter with "_".


    return new_name


def demo_walk():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


main()
