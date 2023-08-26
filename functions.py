morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def encode(original_str):
    result = ''
    for i in original_str:
        result += morse_code_dict[i.upper()] + ' '
    return result


def decode(original_str):
    result = ''
    current_letter = ''
    for i in original_str:
        if i == '/':
            result += ' '
        elif i != ' ':
            current_letter += i
        else:
            try:
                result += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(current_letter)]
            except ValueError:
                pass
            current_letter = ''
    try:
        result += list(morse_code_dict.keys())[list(morse_code_dict.values()).index(current_letter)]
    except ValueError:
        pass
    return result
