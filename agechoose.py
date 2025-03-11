def classify_age(num):
    while True:
        num = int(input('Type your age to know your age group. '))
        if num >= 0 and num <= 12:
            print('You are a Child')
        elif num >= 13 and num <= 19:
            print('You are a Teen')
        elif num >= 20 and num <= 64:
            print('You are an Adult')
        elif num >= 65:
            print('You are a Senior')
        else:
            print('Invalid input! Please enter your real age. ')
        
classify_age(90)