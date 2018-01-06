lucky_num = 6
while True:
    input_number = int(input("Input a number(1~10):"))
    if input_number == lucky_num:
        print("You guess is true!")
        break
    elif input_number > lucky_num:
        print("You guess is bigger")
    else:
        print("You guess is smaller")
