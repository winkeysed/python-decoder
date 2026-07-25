# signal-decoder

A small python script for decoding coordinate-based transmissions.

## What it does

Takes a string of two-digit numbers, maps each to a character on a 7x7 grid, and outputs the decoded text.

## Grid layout

|     | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
|-----|-----|-----|-----|-----|-----|-----|-----|
| **1** | A   | B   | C   | D   | E   | F   | G   |
| **2** | H   | I   | J   | K   | L   | M   | N   |
| **3** | O   | P   | Q   | R   | S   | T   | U   |
| **4** | V   | W   | X   | Y   | Z   | 0   | 1   |
| **5** | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| **6** | 9   | .   | -   | _   | /   | :   | @   |

## Usage

```bash
python signal_decoder.py
```

Then paste the coordinate string when prompted.

## Example

Input:
```
> 23 32 13 51 44 45
```

Output:
```
  DECODED: JPCYZ
```

## Requirements

Python 3.6+

No external dependencies.

## License

MIT
