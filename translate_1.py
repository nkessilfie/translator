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
        french_word = french_word.lower()
        for key in fre_dict.keys():
            if french_word == key:
                print(key, ':', fre_dict[key])
                break
            else:
                print('word not in dictionary')
                break


    elif option == 2:
        with open('engToSpan.txt', 'r') as spa:
            spa_dict = eval(spa.read())

        print('English to Spanish')
        spanish_word = input('Enter the english word: ')
        spanish_word = spanish_word.lower()
        for key in spa_dict.keys():
            if spanish_word == key:
                print(key, ':', spa_dict[key])
                break
            else:
                print('word not in dictionary')
                break

    elif option == 3:
        with open('engToPidg.txt', 'r') as pidg:
            pidg_dict = eval(pidg.read())

        print('English to Pidgin')
        pidgin_word = input('Enter the english word: ')
        pidgin_word = pidgin_word.lower()
        for key in pidg_dict.keys():
            if pidgin_word == key:
                print(key, ':', pidg_dict[key])
                break
            else:
                print('word not in dictionary')
                break

    else:
        print('Invalid input')

except ValueError:
    print('Unknown entry')

# except:
#    print('An error has occurred')
