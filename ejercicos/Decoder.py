"""

In this exercise, you will develop a function named decode(message_file). 
This function should read an encoded message from a .txt file and return its decoded version as a string.

Note that you can write your code using any language and IDE you want (Python is preferred if possible, but not mandatory).

Your function must be able to process an input file with the following format:

3 love
6 computers
2 dogs
4 cats
1 I
5 you
In this file, each line contains a number followed by a word. 
The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. 
The pyramid increases by one number per line, like so:

  1
 2 3
4 5 6
The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). 
You should ignore all the other words. So for the example input file above, the message words are:

1: I
3: love
6: computers
and your function should return the string "I love computers".

la ruta y el archivo es el siguiente
C:\message.txt

"""

def decode(message_file):
    try:
        with open("C:\coding_qual_input.txt", 'r') as file: # Assuming the file is in the Downloads folder
            lines = file.readlines()
    except FileNotFoundError:
        return "File not found."

    decoded_words = []
    current_index = 0

    for line in lines:
        parts = line.split()
        if len(parts) == 2:
            word = parts[1]
            current_index = int(parts[0])
            decoded_words.append((current_index, word))

    decoded_words.sort()  # Sort the words based on the index
    words = list(map(lambda x: x[1], decoded_words))
    #decoded_message = ' '.join(word for _, word in decoded_words)

    return words

def create_pyramid():
    words = decode("coding_qual_input.txt")
    pyramid = []
    current_index = 1
    current_level_words = []

    for word in words:
        current_level_words.append(word)
        if len(current_level_words) == current_index:
            pyramid.append(' '.join(current_level_words))
            current_level_words = []
            current_index += 1
    
    palabras_finales = [frase.split()[-1] for frase in pyramid]

    oracion_final = ' '.join(palabras_finales)

    return oracion_final

# Example usage:
#result = decode("coding_qual_input.txt")
result = create_pyramid()

if result:
    print("Decoded Message:", result)
else:
    print("Error:", result)