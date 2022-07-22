def countdown(i):
    print(i)
    if int(i) <= 1:
        return
    else:
        countdown(int(i)-1)

countdown(input('Введи число: '))