import pytest
import skrypt

def test_display(capsys):
    args = ["a","b","c"]
    skrypt.display(args, False)
    captured = capsys.readouterr()
    assert captured.out == "a\nb\nc\n"

def test_run(capsys):
    args = ["f", "b", "l", "r", "f", "f"]
    skrypt.run(args,skrypt.move_descriptions)
    captured = capsys.readouterr()
    assert captured.out == "Zwierzak idzie do przodu\nZwierzak idzie do tyłu\nZwierzak skręca w lewo\
\nZwierzak skręca w prawo\nZwierzak idzie do przodu\nZwierzak idzie do przodu\n"
