import sys
import math

hill_cipher_key = [[""],[""]]
hill_cipher_key_decode = [["",""],
                            ["",""]]

try:
    while len(hill_cipher_key[0]) != 2:
        hill_cipher_key[0].clear()
        hill_cipher_key[0] = input("Enter first row or 2x2 hill cipher key (seperate them using spaces): ").split(" ")
        hill_cipher_key[0] = list(map(int,hill_cipher_key[0]))
except:
    print("Illegal input")
    sys.exit()
try:
    while len(hill_cipher_key[1]) != 2:
        hill_cipher_key[1].clear()
        hill_cipher_key[1] = input("Enter second row or 2x2 hill cipher key (seperate them using spaces): ").split(" ")
        hill_cipher_key[1] = list(map(int,hill_cipher_key[1]))
except:
    print("Illegal Input")
    sys.exit()

process_type = input("(E)ncrypt\n(D)ecrypt\nWhat is the process? ")

if process_type == "E" :
    grouped_string = []
    mathematical_value_from_string = []
    result_encrypted_mathematical_value = []
    result_encrypted_string_value = []
    encrypted_text = ""
    plain_text_string = input("Enter plain text: ")
    processed_string = ''.join(e for e in plain_text_string if e.isalnum()).upper()
    if len(processed_string)%2 != 0:
        print("adding an A in the end to compensate for the character count (character should be even number)")
        processed_string += "A"

    for index in range(0, len(processed_string), 2):
        grouped_string.append(processed_string[index : index + 2])

    for index in range(0, len(grouped_string), 1):
        mathematical_value_from_string.append([ord(grouped_string[index][0]) - 65,ord(grouped_string[index][1]) - 65])

    for string_index in range(0, len(mathematical_value_from_string), 1):
        result_encrypted_mathematical_value.append([
            ((mathematical_value_from_string[string_index][0] * hill_cipher_key[0][0]) + (mathematical_value_from_string[string_index][1] * hill_cipher_key[0][1]))%26,
            ((mathematical_value_from_string[string_index][0] * hill_cipher_key[1][0]) + (mathematical_value_from_string[string_index][1] * hill_cipher_key[1][1]))%26
        ])
        
    for encrypted_index in range(0, len(result_encrypted_mathematical_value), 1):
        result_encrypted_string_value.append(
            chr(result_encrypted_mathematical_value[encrypted_index][0] + 65) + chr(result_encrypted_mathematical_value[encrypted_index][1] + 65)
        )

    for encrypted_index in range(0, len(result_encrypted_string_value), 1):
        encrypted_text += result_encrypted_string_value[encrypted_index]

    print("Encrypted text is: " + encrypted_text)
elif process_type == "D" :
    determinant = hill_cipher_key[0][0]*hill_cipher_key[1][1] - hill_cipher_key[1][0]*hill_cipher_key[0][1]
    hill_cipher_key_decode[1][1] = hill_cipher_key[0][0] * (1/determinant)
    hill_cipher_key_decode[1][0] = hill_cipher_key[1][0] * -1 * (1/determinant)
    hill_cipher_key_decode[0][1] = hill_cipher_key[0][1] * -1 * (1/determinant)
    hill_cipher_key_decode[0][0] = hill_cipher_key[1][1] * (1/determinant)
    grouped_string = []
    mathematical_value_from_string = []
    result_decrypted_mathematical_value = []
    result_decrypted_string_value = []
    decrypted_text = ""
    encrypted_text = input("Enter encrypted text: ")
    processed_string = ''.join(e for e in encrypted_text if e.isalnum()).upper()
    for index in range(0, len(processed_string), 2):
        grouped_string.append(processed_string[index : index + 2])
    for index in range(0, len(grouped_string), 1):
        mathematical_value_from_string.append([ord(grouped_string[index][0]) - 65,ord(grouped_string[index][1]) - 65])
    for string_index in range(0, len(mathematical_value_from_string), 1):
        result_decrypted_mathematical_value.append([
            ((mathematical_value_from_string[string_index][0] * hill_cipher_key_decode[0][0]) + (mathematical_value_from_string[string_index][1] * hill_cipher_key_decode[0][1]))%26,
            ((mathematical_value_from_string[string_index][0] * hill_cipher_key_decode[1][0]) + (mathematical_value_from_string[string_index][1] * hill_cipher_key_decode[1][1]))%26
        ])
    for decrypted_index in range(0, len(result_decrypted_mathematical_value), 1):
        result_decrypted_string_value.append(
            chr(math.ceil(result_decrypted_mathematical_value[decrypted_index][0]) + 65) + chr(math.ceil(result_decrypted_mathematical_value[decrypted_index][1]) + 65)
        )

    for decrypted_index in range(0, len(result_decrypted_string_value), 1):
        decrypted_text += result_decrypted_string_value[decrypted_index]

    print("Decrypted text is: " + decrypted_text)
else:
    print("wrong option")