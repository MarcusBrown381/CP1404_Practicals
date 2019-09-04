def main():
    import random
    quick_pick_no = int(input("How many quick picks?: "))
    while quick_pick_no < 0:
        print("Enter a number above zero!")
        quick_pick_no = int(input("How many quick picks?: "))
    for i in range(quick_pick_no):
        quick_pick_list = []
        for e in range(6):
            number = random.randint(1, 45)
            while number in quick_pick_list:
                number = random.randint(1, 45)
            quick_pick_list.append(number)
        quick_pick_list.sort()
        print(quick_pick_list)



main()
