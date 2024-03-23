
import random, string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special


    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

new_pwd = generate_password(min_length, has_number, has_special)
print("The generated password is :", new_pwd)












#    alphabet = letters + digits + special_chars
#    pwd = ''
#    pw_strong = False

#    while not pw_strong:
#        pwd = ''
#        for i in range(pw_length):
#            pwd += ''.join(secrets.choice(alphabet))

#        if (any(char in special_chars for char in pwd) and
#                sum(char in digits for char in pwd) >= 2):
#            pw_strong = True

#    return pwd


# if __name__ == '__main__':
#    print(create_pw())