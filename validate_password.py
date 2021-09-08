import random
"""
Note:
Om prgammet hade varit i ett större system hade inte funktionen validate_pwd skrivit ut en massa saker till konsolen.
Funktionen hade istället retunerat en dictionary som innehåller om lösenordet är giltigt eller inte och som
innehåller vilken anledning till varför lösenordet inte är giltigt. Men eftersom funktionen validate_pwd måste retunera
ett boolean värde, för att codeGrade ska kunna testa funktionen, går det inte att retunera en dictionary.

Att lösa problemet trodde jag inte skulle tå så lång tid då jag har programmerat mycket i python innan.
Jag trodde först det kanske skulle ta 30-60 min att skriva och renskriva koden. Men när jag började
koda programmet ville jag generallisera problemet genom att kunna ända lite på passwordpolicyn. 
Detta visade sig att ta längre tid än förväntat. Det slutade med att ta ungerfär 2-3 timmar komma på 
hur man skulle implementera, skriva och sedan renskriva koden så att det blev ett bra passwordpolicy system.

"""
# Password Policy
MINIMUM_PASSWORD_LENGTH = 6
MAXIMUM_PASSWORD_LENGTH = 16
NUMBER_AMOUNT = 1
SPECIAL_AMOUNT = 1
SMALL_LETTERS_AMOUNT = 1
LARGE_LETTERS_AMOUNT = 2
SPECIAL_CHARACTERS = "!@*$"

def test_password_policy():
    policy_sum = (NUMBER_AMOUNT + SPECIAL_AMOUNT + SMALL_LETTERS_AMOUNT + LARGE_LETTERS_AMOUNT)

    if MINIMUM_PASSWORD_LENGTH > MAXIMUM_PASSWORD_LENGTH:
        return False

    if policy_sum > MINIMUM_PASSWORD_LENGTH:
        return False
    
    return True

def contains(password, charset, minumum_count = 1):
    """
    Function that takes a password and looks if the password contains a specified ammount of the symbols
    that exists in the charset variable. 
    """
    if minumum_count < 1:
        True

    for character in password:
        if character in charset:
            minumum_count -= 1
            if minumum_count == 0:
                return True
    
    return False


def validate_pwd(password):
    """The function takes in a password and checks if it follows the password policy above"""

    # Checks to see if password policy is valid
    result = test_password_policy()
    if not result:
        print("Not valid password policy")
        return False

    if len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Invalid Password: Password must contain at least {} characters".format(MINIMUM_PASSWORD_LENGTH))
        return False

    elif len(password) > MAXIMUM_PASSWORD_LENGTH:
        print("Invalid Password: Password can only contain a mamimum of {} characters".format(MAXIMUM_PASSWORD_LENGTH))
        return False
    
    contains_number = contains(password, "1234567890", NUMBER_AMOUNT)
    if not contains_number:
        print("Invalid Password: Password must contain at least {} numbers".format(NUMBER_AMOUNT))
        return False

    contains_special = contains(password, SPECIAL_CHARACTERS, SPECIAL_AMOUNT)
    if not contains_special:
        print("Invalid Password: Password must contain at least {} special characters".format(SPECIAL_AMOUNT))
        return False

    contains_small_letter = contains(password, "abcdefghijklmnopqrstuvwxyz", SMALL_LETTERS_AMOUNT)
    if not contains_small_letter:
        print("Invalid Password: Password must at least contain {} small letters".format(SMALL_LETTERS_AMOUNT))
        return False

    contains_large_letter = contains(password, "ABCDEFGHIJKLMNOPQRSTUWVXYZ", LARGE_LETTERS_AMOUNT)
    if not contains_large_letter:
        print("Invalid Password: Password must at least contain {} capital letters".format(LARGE_LETTERS_AMOUNT))
        return False
    
    return True
    

def generate_pwd():
    """Generates a valid password based on the password policy above"""


    password_length = random.randint(MINIMUM_PASSWORD_LENGTH, MAXIMUM_PASSWORD_LENGTH)
    space_left = password_length

    amount_of_numbers = random.randint(NUMBER_AMOUNT, space_left-(SPECIAL_AMOUNT+SMALL_LETTERS_AMOUNT+LARGE_LETTERS_AMOUNT))
    space_left -= amount_of_numbers

    amount_of_specials = random.randint(SPECIAL_AMOUNT, space_left-(SMALL_LETTERS_AMOUNT+LARGE_LETTERS_AMOUNT))
    space_left -= amount_of_specials

    amount_of_small_letters = random.randint(SMALL_LETTERS_AMOUNT, space_left-(LARGE_LETTERS_AMOUNT))
    space_left -= amount_of_small_letters
     
    amount_of_large_letters = random.randint(LARGE_LETTERS_AMOUNT, space_left)
    space_left -= amount_of_large_letters

    amount_of_small_letters += space_left
    del space_left

    password_contense = {
        "large_letter":amount_of_large_letters,
        "small_letter":amount_of_small_letters,
        "number":amount_of_numbers,
        "special":amount_of_specials
        }

    final_password = ""

    for i in range(password_length):

        keys_to_pop = []
        for key in password_contense:
            if password_contense[key] <= 0:
                keys_to_pop.append(key)
        
        for key in keys_to_pop:
            password_contense.pop(key)


        choice = random.choice(list(password_contense.keys()))

        if choice == "large_letter":
            password_contense["large_letter"] -= 1
            final_password += random.choice(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

        elif choice == "small_letter":
            password_contense["small_letter"] -= 1
            final_password += random.choice(list("abcdefghijklmnopqrstuvwxyz"))

        elif choice == "number":
            password_contense["number"] -= 1
            final_password += random.choice(list("1234567890"))

        elif choice == "special":
            password_contense["special"] -= 1
            final_password += random.choice(list(SPECIAL_CHARACTERS))
    
    return final_password






        

def main():
    valid_password = False

    while not valid_password:
        print("\n")
        password = input("Input a password that you want to use\nor type 0 for a computer generated password: ")
        
        if password == "0":
            password = generate_pwd()
            print("Generated Password: ", end="")
        
        valid_password = validate_pwd(password)
        
    print("{} is a valid password \nExiting...".format(password))

        


if __name__ == "__main__":
    main()