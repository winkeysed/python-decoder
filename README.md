# python-decoder

Tools for encoding and decoding coordinate-based transmissions.

Part of the Faded Lands project. Not intended for general use.

---

## Files

| File | Purpose |
|------|---------|
| `signal_decoder.py` | Decodes coordinate strings to text |
| `signal_encoder.py` | Encodes text to coordinate strings |

---

## Grid

12 rows, 9 columns. 108 characters total.

```
Row 1:  A B C D E F G H I
Row 2:  J K L M N O P Q R
Row 3:  S T U V W X Y Z 0
Row 4:  1 2 3 4 5 6 7 8 9
Row 5:  . - _ / : @ ? ! +
Row 6:  = & % # * ( ) [ ]
Row 7:  А Б В Г Д Е Ё Ж З
Row 8:  И Й К Л М Н О П Р
Row 9:  С Т У Ф Х Ц Ч Ш Щ
Row 10: Ъ Ы Ь Э Ю Я [sp] Ї Є
Row 11: І Ґ і ґ ё < > " '
Row 12: , ; { } | \ ~ ` ^
```

First digit = row. Second (and third if needed) = column.

Example: `23` = L, `107` = [space], `76` = Е

---

## Usage

Decode:
```
$ python signal_decoder.py
> 23 32 13 51 44 45
  DECODED: JTC.YZ
```

Encode:
```
$ python signal_encoder.py
> hello
  ENCODED: 18 15 23 23 26
```

---

## Requirements

Python 3.6+. No dependencies.

---

## Context

These tools were built for the Faded Lands Minecraft server project. The coordinate cipher is used to encode URLs and messages found in-game as collectible fragments. Players gather the fragments, decode them, and follow the resulting links.

The grid was expanded from 7x6 to 12x9 to support Russian, Ukrainian, and additional symbols needed for URL encoding.

---

## License

MIT
