import random
from words import words
import string



def get_valid_word(words):
    word = random.choice(words) # escoge una palabra, del array de palabras, al azar 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set (word) # las letras de la palabra a acertar
    alphabet = set (string.ascii_uppercase)
    used_letters = set() # letras acertadas por el jugador

    lives = 6


    while len(word_letters) > 0 and lives > 0: 
    # mientras tengamos letras por acertar tengamos vidas


        print('Tienes ', lives,'vidas y has usado estas letras: ',' '.join(used_letters))
        #letras usadas

        word_list = [letter if letter in used_letters else '-' for letter in word]
        # indicamos los aciertos y las letras que faltan ( P-LABR-  )
        print('Palabra a acertar: ',' '.join(word_list))

        user_letter = input('Adivina una letra: ').upper()
        # solicitando letra al jugador




        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                # si acierta se elimina la letra

            else:
                lives = lives - 1 # si no acierta la letra, pierde una vida
                print ('La letra no está en la palabra.')

        elif user_letter in used_letters:
            print('Ya usaste esa letra. Por favor, inténtalo de nuevo.')
        else:
            print('Caracter inválido. Por favor, inténtalo de nuevo.')

    # Aquí finaliza el bucle while si hemos acertado todas las letras o hayamos perdido todas las vidas
    if lives == 0:
        print('Lo siento, has muerto. La palabra era ', word)
    else:
        print('Bien!. Has acertado la palabra ', word)

hangman()


