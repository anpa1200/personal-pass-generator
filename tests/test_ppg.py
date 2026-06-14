"""Tests for PPG (Personal Pass Generator) logic."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PPG_personal_pass_generator import (
    generate_additional_values,
    generate_passwords,
    run_from_words,
    to_leet_speak,
)


def test_to_leet_speak():
    values = ["test", "hello"]
    to_leet_speak(values)
    assert "test" in values
    assert "hello" in values
    # Leet variants appended (e->3, s->$, t->7, etc.)
    assert any("7" in v and "$" in v for v in values)  # test -> 73$7
    assert any("0" in v for v in values)  # hello -> #3ll0


def test_generate_additional_values():
    add = generate_additional_values(2)
    assert "0" in add
    assert "a" in add
    assert "!" in add
    assert "00" in add
    assert "aa" in add
    assert "aaa" not in add


def test_generate_passwords_basic_only():
    basic = ["alice", "bob"]
    additional = generate_additional_values()
    pw = generate_passwords(basic, additional, add_symbols=False, min_len=1, max_len=20)
    assert "alice" in pw
    assert "bob" in pw
    # With only 2 basic values, no bval1+bval2 pairs are added (need >3)
    assert len(pw) >= 2


def test_generate_passwords_length_filter():
    basic = ["a", "ab", "abc", "abcd"]
    additional = []
    pw = generate_passwords(basic, additional, add_symbols=False, min_len=2, max_len=3)
    assert "a" not in pw
    assert "ab" in pw
    assert "abc" in pw
    assert "abcd" not in pw


def test_run_from_words(tmp_path):
    output = tmp_path / "nested" / "wordlist.txt"
    run_from_words(["alice", "acme"], output, 4, 12, leet=True, symbols=False, max_affix_length=1)

    generated = output.read_text(encoding="utf-8").splitlines()
    assert "alice" in generated
    assert "Alice" in generated
    assert "@l!(3" in generated
