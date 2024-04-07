def simple_cipher(encrypted, k):
    #Set String Alpahabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #Create empty string for decrypt message
    decrypted = ''
    for char in encrypted:
        position = alphabet.index(char) #Find the position of charactors
        new_position = (position - k) % len(alphabet) #Find a new position
        decrypted += alphabet[new_position] #Use a new position to get alphabet
    return decrypted
encrypted_message = 'VTAOG'
shift_key = 2
# Decrypt the message
decrypted_message = simple_cipher(encrypted_message, shift_key)
# Print the decrypted message
print(decrypted_message)






