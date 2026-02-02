while True:
    num = int(input())
    if num < 25:
        print('Higher')
        continue
    elif num > 25:
        print("Lower")
        continue
    elif num == 25:
        print("Good")
        break