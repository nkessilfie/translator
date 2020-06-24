home = input('----Tap enter to begin translating to a language of your choice----')
print("------------------------- Let's Begin ----------------------------- \n"
      "1. ---------English to French---------\n"
      "2. ---------English to Spanish--------\n"
      "3. ---------English to Pidgin---------")

try:
    option = int(input('Choose your option: '))

    if option == 1:
        print('English to French')

    elif option == 2:
        print('English to Spanish')

    elif option == 3:
        print('English to Pidgin')

    else:
        print('Invalid input')

except:
    print('An error has occurred')
