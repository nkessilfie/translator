home = input('----Tap enter to begin translating to a language of your choice----')
print("------------------------- Let's Begin ----------------------------- \n"
      "1. ---------English to French---------\n"
      "2. ---------English to Spanish--------\n"
      "3. ---------English to Pidgin---------")

try:
    option = int(input('Choose your option: '))

    if option == 1:
        with open('engToFre.txt', 'r') as fre:
            fre_dict = eval(fre.read())

        print('English to French')
        french_word = input('Enter the english word: ')
        for key in fre_dict.keys():
            if french_word == key:
                print(key, ':', fre_dict[key])

    elif option == 2:
        print('English to Spanish')

    elif option == 3:
        print('English to Pidgin')

    else:
        print('Invalid input')

except:
    print('An error has occurred')
