# Caesar Cipher Tool (CLI)

[![CI](https://github.com/osmankaankars/caesar-cipher-tool/actions/workflows/tests.yml/badge.svg)](https://github.com/osmankaankars/caesar-cipher-tool/actions/workflows/tests.yml)
[![Release](https://img.shields.io/github/v/release/osmankaankars/caesar-cipher-tool?display_name=tag)](https://github.com/osmankaankars/caesar-cipher-tool/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple Caesar Cipher CLI that encrypts or decrypts text with a shift.

## Version

Current version: `0.1.0`

## Installation

Python 3.8+ is required.

Make the script executable:

```bash
chmod +x caesar.py
```

Install as a package (pipx):

```bash
pipx install .
```

Alternative:

```bash
python -m pip install .
```

## Usage

Text argument:

```bash
./caesar.py encrypt --shift 3 "Hello, World!"
./caesar.py decrypt --shift 3 "Khoor, Zruog!"
```

If installed with pipx:

```bash
caesar encrypt --shift 3 "Hello, World!"
caesar decrypt --shift 3 "Khoor, Zruog!"
```

From stdin:

```bash
echo "Attack at dawn" | ./caesar.py encrypt -s 5
```

File input/output:

```bash
./caesar.py encrypt -s 7 -f input.txt -o output.txt
```

## Testing

```bash
python -m pytest
```

## Notes

- Preserves letter case.
- Non-letter characters are left unchanged.
- Shift is normalized mod 26.

## License

MIT
