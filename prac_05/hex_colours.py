def main():
    hex_colours = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "azure": "#f0ffff",
                   "beige": "#f5f5dc", "black": "#000000", "blue": "#0000ff", "brown": "#a52a2a", "burlywood": "#deb887",
                   "cadetblue": "#5f9ea0"}

    query = input("Look up a colour's hexadecimal value: ").lower()
    while query != hex_colours:
        print("The code for \"{}\" is {}".format(query,
                                                 hex_colours.get(query)))
        query = input("Look up a colour's hexadecimal value: ").lower()


main()
