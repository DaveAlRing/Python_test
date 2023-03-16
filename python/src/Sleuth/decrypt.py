print("Hello, Contosoville!")

town = "Contosoville"
print( "The town I am looking for is " + town )

def chant( phrase ):
    print( phrase + phrase + phrase )

chant( "Contosoville!" )

def lasso_letter(letter, shift_amount):

    alphabet_size = 26
    a_ascii = ord("a")
    letter_code = ord(letter.lower())
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphabet_size)
    decoded_letter = chr(true_letter_code)

    return decoded_letter

def lasso_word(word, shift_amount):

    decoded_word = ""

    for letter in word:
        decoded_letter = lasso_letter(letter, shift_amount)
        decoded_word = decoded_word + decoded_letter

    return decoded_word

print(lasso_word("Ncevy", 13))
print(lasso_word("gpvsui", 25))
print(lasso_word("ugflgkg", -18))
print(lasso_word("p", -2))