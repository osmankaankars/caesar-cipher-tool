# Caesar Cipher Tool (CLI)

Basit bir Caesar Cipher CLI araci. Metni belirtilen kaydirma degeriyle sifreler veya cozer.

## Surum

Mevcut surum: `0.1.0`

## Kurulum

Python 3 yeterlidir. Dosyayi calistirilabilir yapmak icin:

```bash
chmod +x caesar.py
```

Paket olarak kurmak (pipx):

```bash
pipx install .
```

Alternatif olarak:

```bash
python -m pip install .
```

## Kullanim

Metin arguman olarak:

```bash
./caesar.py encrypt --shift 3 "Hello, World!"
./caesar.py decrypt --shift 3 "Khoor, Zruog!"
```

pipx ile kurulduysa:

```bash
caesar encrypt --shift 3 "Hello, World!"
caesar decrypt --shift 3 "Khoor, Zruog!"
```

stdin ile:

```bash
echo "Attack at dawn" | ./caesar.py encrypt -s 5
```

Dosyadan okuyup dosyaya yazma:

```bash
./caesar.py encrypt -s 7 -f input.txt -o output.txt
```

## Notlar

- Buyuk/kucuk harf korunur.
- Harf olmayan karakterler aynen birakilir.
- Shift degeri mod 26 ile normalize edilir.

## Lisans

MIT
