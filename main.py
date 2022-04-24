# Jeu du pendu

def word_choice():
    _input = input('Choisissez un mot : ')
    return _input


def print_pendu(score):
    print(" ==========Y= ") if score >= 6 else None
    print(" ||/       |  ") if score >= 5 else None
    print(" ||        0  ") if score >= 4 else None
    print(" ||       /|\ ") if score >= 3 else None
    print(" ||       /|  ") if score >= 2 else None
    print("/||           ") if score >= 1 else None


def ask_check_input():
    while True:
        try:
            letter = input("Quelle lettre ? ").lower()
            if len(letter) != 1:
                print("Vous devez mettre qu'une seule lettre !")
            elif not letter.isalpha():
                print("ce n'est pas une lettre")
            else:
                return letter
        except ValueError:
            print("Ce n'est pas jouable")


if __name__ == '__main__':
    score = 0
    word_to_find = word_choice()
    list_to_find = ["_" for x in range(len(word_to_find))]
    list_to_find[0] = word_to_find[0]
    list_to_find[-1] = word_to_find[-1]

    while True:
        print(''.join(list_to_find))
        letter_input = ask_check_input()
        if letter_input in list_to_find[1:-1]:
            print(f"Tu as déjà donné la lettre {letter_input}")
        else:
            if letter_input in word_to_find[1:-1]:
                for i, c in enumerate(word_to_find):
                    if c == letter_input:
                        list_to_find[i] = c
                print("Bravo il y avait bien cette lettre !")
            else:
                print(f"Nan la lettre {letter_input} n'est pas présente :/")
                score += 1
                print_pendu(score)
                if score == 6:
                    print("Tu es pendu :/")
                    break
        if "_" not in list_to_find:
            print(f"Félicitation tu as trouvé le mot : {word_to_find} !")
            break
