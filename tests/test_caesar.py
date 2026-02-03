import caesar


def test_caesar_encrypt_basic():
    assert caesar.caesar("Hello, World!", 3) == "Khoor, Zruog!"


def test_caesar_decrypt_basic():
    assert caesar.caesar("Khoor, Zruog!", -3) == "Hello, World!"


def test_caesar_shift_wraps():
    assert caesar.caesar("ABC", 29) == "DEF"


def test_main_rejects_text_and_file(tmp_path, capsys):
    file_path = tmp_path / "input.txt"
    file_path.write_text("abc", encoding="utf-8")

    code = caesar.main(
        ["encrypt", "abc", "--shift", "1", "--file", str(file_path)]
    )
    captured = capsys.readouterr()

    assert code == 2
    assert "either text or --file" in captured.err


def test_main_file_io(tmp_path):
    input_path = tmp_path / "input.txt"
    output_path = tmp_path / "output.txt"
    input_path.write_text("abc xyz", encoding="utf-8")

    code = caesar.main(
        [
            "encrypt",
            "--shift",
            "2",
            "--file",
            str(input_path),
            "--output",
            str(output_path),
        ]
    )

    assert code == 0
    assert output_path.read_text(encoding="utf-8") == "cde zab"
