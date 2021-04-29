#!/usr/bin/env python3
# student number 19019021
import sys

"""
COMP0015 Stegsnow
"""

CHARACTER_LENGTH = 7    # Length of a binary character
ZERO = '0'              # Character representing zero         ``
ONE = '1'              # Character representing one

CHAR_TO_BINARY = { # binary representation of ASCII characters
    'a': '1100001', 
    'b': '1100010',
    'c': '1100011',
    'd': '1100100', 
    'e': '1100101',
    'f': '1100110',
    'g': '1100111',
    'h': '1101000',
    'i': '1101001',
    'j': '1101010',
    'k': '1101011',
    'l': '1101100',
    'm': '1101101',
    'n': '1101110',
    'o': '1101111',
    'p': '1110000',
    'q': '1110001',
    'r': '1110010',
    's': '1110011',
    't': '1110100',
    'u': '1110101',
    'v': '1110110',
    'w': '1110111',
    'x': '1111000',
    'y': '1111001',
    'z': '1111010',
    ' ': '1111011'
}

BINARY_TO_CHAR = { # binary string to ascii characters
    '1100001': 'a', 
    '1100010': 'b',
    '1100011': 'c',
    '1100100': 'd', 
    '1100101': 'e',
    '1100110': 'f',
    '1100111': 'g',
    '1101000': 'h',
    '1101001': 'i',
    '1101010': 'j',
    '1101011': 'k',
    '1101100': 'l',
    '1101101': 'm',
    '1101110': 'n',
    '1101111': 'o',
    '1110000': 'p',
    '1110001': 'q',
    '1110010': 'r',
    '1110011': 's',
    '1110100': 't',
    '1110101': 'u',
    '1110110': 'v',
    '1110111': 'w',
    '1111000': 'x',
    '1111001': 'y',
    '1111010': 'z',
    '1111011': ' '
}

def split(word):
    return list(word)


def encode_secret_message(message, infile, outfile, zero, one):
    """Encode the secret message in input file file, write the file containing
    the secret message to the outfile.           
 
    Args:
        zero (str): Character representing a zero.
        one (str): Character representing a one.
        message (str): Message to be embedded in infile.
        infile (str): Input file name.
        outfile (str): Output file name.
    """

    list_secret = [] #for storing secret message input
    list_input = [] #for storing txt file lines

    #Processing Secret message

    for x in range(len(message)):
        word = CHAR_TO_BINARY[message[x]]
        swithed_word = ''
        for x in range(len(word)):
            swithed_word += encode(word[x], ZERO, ONE)
        list_secret.append(swithed_word)

    #Reading file

    with open(infile, 'r') as file:
        for line in file:
            lines = line.rstrip()
            #take out \n symbols that would appear without this function
            read = lines.split("\n")
            list_input.append(read)
    file.close()
    #Combining
    minimum = min(len(list_input), len(list_secret))
    for x in range(minimum):
        list_input[x].append(list_secret[x])
    
    f = open("secret.txt", 'w')
    for row in list_input: 
        row = ', '.join(map(str, row))
        row = row.replace(',', '')
        row = row.strip(',')
        f.write('%s\n' % row)
    pass


def encode(binary_letter, zero_char, one_char):
    """Make the message invisible. Substitute the zeroes and ones in binary 
        letter for your chosen characters, typically tab and space.

    Args:
        binary_letter (str): a sequence of zeroes and ones representing an ascii character.
        zero_char (str): The character with which the zeroes should be replaced.
        one_char (str): The character with which the ones should be replaced.

    Returns:
        str: Represents the letter.
    """

    return binary_letter.replace('0', zero_char).replace('1', one_char)


def decode(binary_letter, zero_char, one_char):
    """Make the message visible. Substitute the characters representing zeroes and ones in the binary 
        letter for the characters '0' and '1'.

    Args:
        encoded_char (str): a sequence of zeroes and ones.
        zero_char (str): The character to be replaced with zeroes.
        one_char (str): The character to be replaced with ones.

    Returns:
        str: Represents the letter.
    """

    return binary_letter.replace(zero_char, '0').replace(one_char, '1')

def get_key(val):
    for key, value in BINARY_TO_CHAR.items():
        if val == key:
            return value
    

def decode_secret_message(infile, zero, one):
    """Print the decoded message in the file infile

    Args:
        infile (str): file name
        zero_char (str): The character with which the zeroes should be replaced.
        one_char (str): The character with which the ones should be replaced.
    """    
    word = ''
    message = ''
    last_chars = []
    with open(infile, 'r',) as file:        
        for line in file:
            last_chars.append(line.rstrip('\n')[-7:])
    for chars in last_chars:
        if zero and one in chars:
            chars = decode(chars, zero, one)
            word = ' '.join([BINARY_TO_CHAR[chars]])
            message += word
    print (message)
    pass


def main():
    # DO NOT EDIT THIS CODE

    zero = ZERO 
    one = ONE

    args = sys.argv[1:]                      
    if len(args) != 1 and len(args) != 4:
        print(f'usage: \n\tto encode a message: python stegsnow.py -m "message" infile outfile\
            \n\tto decode a message: python stegsnow.py infile')
        return
 
    # Parse message, infile, outfile from command line, giving a helpful
    # error message if this fails.

    try:
        if len(args) == 1:
            encoded_file = args[0]
        elif len(args) == 4:
            message = args[1]
            plaintext_file = args[2]
            output_file = args[3]
        else:
            raise ValueError
    except Exception:
        print("Error parsing options from command line: " + ' '.join(args))
        return

    if args[0] == '-m':
        encode_secret_message(message, plaintext_file, output_file, zero, one)
    else:
        decode_secret_message(encoded_file, zero, one)
    

if __name__ == "__main__":
    main()