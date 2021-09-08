"""
Testprogram för kravställda funktioner i Inlämningsuppgift1 "Lösenordsvalidering"
Carina Nilsson, 2021-08-18
"""
import sys
from validate_password import validate_pwd

VALID_LIST = ['filiP123!', 'C*or1n2elia']
INVALID_LIST = ['T0w@', 'enizlcebrmtwertyuio@P123', 'Oth!lia', 'moHammed123',
                'naLah@', 'LENNART$123',  '', '*arwen123']


def function_present(func_name):
    """Tests that reqired function is present"""
    present = False
    if func_name in globals():
        present = True
    return present


def return_value_check(value):
    """Tests that the function returns a value"""
    if value is None:
        print("Din funktion returnerar ingenting")
        sys.exit(1)


def test_main():
    """Main test script"""
    function = 'validate_pwd'
    if not function_present(function):
        print(f"Funktionen {function} finns inte!")
        sys.exit(1)
    else:
        print(f"Funktionen {function} är implementerad. OK\n")

    for word in INVALID_LIST:
        print(f"Test with '{word}'.....")
        valid = validate_pwd(word)
        return_value_check(valid)
        if valid is not False:
            print(
                f"Fel: Din funktion underkänner inte det felaktiga lösenordet '{word}'")
            sys.exit(1)
        else:
            print("OK")
    print()

    for word in VALID_LIST:
        print(f"Test with '{word}'.....", end='')
        valid = validate_pwd(word)
        return_value_check(valid)
        if valid is not True:
            print(
                "Fel: Din funktion godkänner inte det korrekta lösenordet")
            sys.exit(1)
        else:
            print("OK")

    print("\nDin valideringsfunktion passerar alla tester.")


if __name__ == "__main__":
    test_main()
