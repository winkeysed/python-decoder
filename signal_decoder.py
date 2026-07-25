#!/usr/bin/env python3
# signal_decoder.py
# Coordinate grid decoder for Archive-7 transmissions

GRID = {
    11:'A', 12:'B', 13:'C', 14:'D', 15:'E', 16:'F', 17:'G',
    21:'H', 22:'I', 23:'J', 24:'K', 25:'L', 26:'M', 27:'N',
    31:'O', 32:'P', 33:'Q', 34:'R', 35:'S', 36:'T', 37:'U',
    41:'V', 42:'W', 43:'X', 44:'Y', 45:'Z', 46:'0', 47:'1',
    51:'2', 52:'3', 53:'4', 54:'5', 55:'6', 56:'7', 57:'8',
    61:'9', 62:'.', 63:'-', 64:'_', 65:'/', 66:':', 67:'@',
}

def decode(coords_str):
    result = ""
    for c in coords_str.split():
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
