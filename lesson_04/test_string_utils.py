import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    # Проверка корректного преобразования первой буквы в заглавную
    ("skypro", "Skypro"),
    # Проверка корректного преобразования первой буквы в заглавную с пробелами
    ("hello world", "Hello world"),


    # Проверка корректного преобразования для строки с цифрами
    ("number10", "Number10"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # Проверка строки, начинающейся с цифр
    ("123abc", "123abc"),
    # Проверка обработки пустой строки
    ("", ""),
    # Проверка строки, состоящей только из пробелов
    ("   ", "   "),
    # Проверка строки, начинающейся с символа
    ("!start", "!start"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    # Проверка удаления одного пробела в начале строки
    (" cat", "cat"),
    # Проверка удаления нескольких пробелов в начале строки
    ("    home", "home"),
    # Проверка удаления пробелов в начале строки с пробелами внутри строки
    ("   hello world", "hello world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    # Проверка обработки пустой строки
    ("", ""),
    # Проверка строки, состоящей только из пробелов
    ("   ", ""),
    # Проверка строки без пробелов в начале
    ("no_whitespace", "no_whitespace"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    # Проверка наличия символа в начале строки
    ("Test", "T", True),
    # Проверка наличия символа в середине строки
    ("SkyPro", "y", True),
    # Проверка наличия символа в строке с цифрами
    ("12345", "2", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    # Проверка отсутствия символа в строке
    ("Test", "Z", False),
    # Проверка обработки пустой строки
    ("", "a", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    # Проверка удаления символа из строки
    ("Rose", "e", "Ros"),
    # Проверка удаления подстроки из строки
    ("SkyPro", "Pro", "Sky"),
    # Проверка удаления символа из строки с цифрами
    ("123123", "2", "1313"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    # Проверка отсутствия изменений при отсутствии символа в строке
    ("Line", "A", "Line"),
    # Проверка обработки пустой строки
    ("", "a", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
