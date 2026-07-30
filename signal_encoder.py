#!/usr/bin/env python3
# signal_encoder.py
# Coordinate grid encoder for Archive-7 transmissions
# Supports: English, Russian, Ukrainian, digits, URL symbols, special chars

GRID = {
    # === ROW 1: A-I ===
    'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
    # === ROW 2: J-R ===
    'J': 21, 'K': 22, 'L': 23, 'M': 24, 'N': 25, 'O': 26, 'P': 27, 'Q': 28, 'R': 29,
    # === ROW 3: S-Z, 0 ===
    'S': 31, 'T': 32, 'U': 33, 'V': 34, 'W': 35, 'X': 36, 'Y': 37, 'Z': 38, '0': 39,
    # === ROW 4: 1-9 ===
    '1': 41, '2': 42, '3': 43, '4': 44, '5': 45, '6': 46, '7': 47, '8': 48, '9': 49,
    # === ROW 5: . - _ / : @ ? ! + ===
    '.': 51, '-': 52, '_': 53, '/': 54, ':': 55, '@': 56, '?': 57, '!': 58, '+': 59,
    # === ROW 6: = & % # * ( ) [ ] ===
    '=': 61, '&': 62, '%': 63, '#': 64, '*': 65, '(': 66, ')': 67, '[': 68, ']': 69,
    # === ROW 7: А-З (RU) ===
    'А': 71, 'Б': 72, 'В': 73, 'Г': 74, 'Д': 75, 'Е': 76, 'Ё': 77, 'Ж': 78, 'З': 79,
    # === ROW 8: И-Р (RU) ===
    'И': 81, 'Й': 82, 'К': 83, 'Л': 84, 'М': 85, 'Н': 86, 'О': 87, 'П': 88, 'Р': 89,
    # === ROW 9: С-Щ (RU) ===
    'С': 91, 'Т': 92, 'У': 93, 'Ф': 94, 'Х': 95, 'Ц': 96, 'Ч': 97, 'Ш': 98, 'Щ': 99,
    # === ROW 10: Ъ-Я, space, Ї, Є ===
    'Ъ': 101, 'Ы': 102, 'Ь': 103, 'Э': 104, 'Ю': 105, 'Я': 106, ' ': 107, 'Ї': 108, 'Є': 109,
    # === ROW 11: І, Ґ, і, ґ, ё, < > " ' ===
    'І': 111, 'Ґ': 112, 'і': 113, 'ґ': 114, 'ё': 115, '<': 116, '>': 117, '"': 118, "'": 119,
    # === ROW 12: , ; { } | \ ~ ` ^ ===
    ',': 121, ';': 122, '{': 123, '}': 124, '|': 125, '\\': 126, '~': 127, '`': 128, '^': 129,
}

def encode(text):
    result = []
    for char in text:
        # Try exact match first, then uppercase
        code = GRID.get(char)
        if code is None:
            code = GRID.get(char.upper())
        if code is not None:
            result.append(str(code))
        else:
            result.append('??')
    return ' '.join(result)

if __name__ == "__main__":
    print("=" * 50)
    print("  ARCHIVE-7 // COORDINATE ENCODER")
    print("  Supports: EN / RU / UA / digits / symbols")
    print("=" * 50)

    user_input = input("\n> ").strip()
    encoded = encode(user_input)
    print(f"\n  ENCODED: {encoded}")
    print("=" * 50)
