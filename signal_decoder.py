#!/usr/bin/env python3
# signal_decoder.py
# Coordinate grid decoder for Archive-7 transmissions
# Supports: English, Russian, Ukrainian, digits, URL symbols, special chars

GRID = {
    # === ROW 1: A-I ===
    11:'A', 12:'B', 13:'C', 14:'D', 15:'E', 16:'F', 17:'G', 18:'H', 19:'I',
    # === ROW 2: J-R ===
    21:'J', 22:'K', 23:'L', 24:'M', 25:'N', 26:'O', 27:'P', 28:'Q', 29:'R',
    # === ROW 3: S-Z, 0 ===
    31:'S', 32:'T', 33:'U', 34:'V', 35:'W', 36:'X', 37:'Y', 38:'Z', 39:'0',
    # === ROW 4: 1-9 ===
    41:'1', 42:'2', 43:'3', 44:'4', 45:'5', 46:'6', 47:'7', 48:'8', 49:'9',
    # === ROW 5: . - _ / : @ ? ! + ===
    51:'.', 52:'-', 53:'_', 54:'/', 55:':', 56:'@', 57:'?', 58:'!', 59:'+',
    # === ROW 6: = & % # * ( ) [ ] ===
    61:'=', 62:'&', 63:'%', 64:'#', 65:'*', 66:'(', 67:')', 68:'[', 69:']',
    # === ROW 7: А-З (RU) ===
    71:'А', 72:'Б', 73:'В', 74:'Г', 75:'Д', 76:'Е', 77:'Ё', 78:'Ж', 79:'З',
    # === ROW 8: И-Р (RU) ===
    81:'И', 82:'Й', 83:'К', 84:'Л', 85:'М', 86:'Н', 87:'О', 88:'П', 89:'Р',
    # === ROW 9: С-Щ (RU) ===
    91:'С', 92:'Т', 93:'У', 94:'Ф', 95:'Х', 96:'Ц', 97:'Ч', 98:'Ш', 99:'Щ',
    # === ROW 10: Ъ-Я, space, Ї, Є ===
    101:'Ъ', 102:'Ы', 103:'Ь', 104:'Э', 105:'Ю', 106:'Я', 107:' ', 108:'Ї', 109:'Є',
    # === ROW 11: І, Ґ, і, ґ, ё, < > " ' ===
    111:'І', 112:'Ґ', 113:'і', 114:'ґ', 115:'ё', 116:'<', 117:'>', 118:'"', 119:"'",
    # === ROW 12: , ; { } | \ ~ ` ^ ===
    121:',', 122:';', 123:'{', 124:'}', 125:'|', 126:'\\', 127:'~', 128:'`', 129:'^',
}

def decode(coords_str):
    result = ""
    for c in coords_str.split():
        if c.strip() == '??':
            result += '?'
        else:
            num = int(c.strip())
            result += GRID.get(num, '?')
    return result

if __name__ == "__main__":
    print("=" * 50)
    print("  ARCHIVE-7 // COORDINATE DECODER")
    print("  Enter coordinates separated by spaces")
    print("=" * 50)

    user_input = input("\n> ").strip()
    decoded = decode(user_input)
    print(f"\n  DECODED: {decoded}")
    print("=" * 50)
