def main():
    import random
    quick_pick_no = int(input("How many quick picks do you wish to generate?: "))
    for i in range(1, quick_pick_no + 1):
        for e in range(1, 7):
            print(random.randint(1, 45))


main()
