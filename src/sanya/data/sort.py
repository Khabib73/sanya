from pathlib import Path
from typing import Final

_DICTIONARY_PATH: Final = Path(__file__).parent / 'dictionary_ru.txt'

_RUSSIAN_ALPHABET: Final = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def _create_alphabet() -> dict[str, list[str]]:
    return {letter: [] for letter in _RUSSIAN_ALPHABET}


def _fill_alphabet_with_words(
    alphabet_words: dict[str, list[str]],
) -> dict[str, list[str]]:
    with Path(_DICTIONARY_PATH).open(encoding='utf-8') as wrong_words:
        for word in wrong_words:
            clean_word = word.strip('\n')
            first_letter = clean_word[0]
            alphabet_words[first_letter].append(clean_word)
    return alphabet_words


def _sort_words(alphabet_words: dict[str, list[str]]) -> dict[str, list[str]]:
    sorted_alphabet_words = {}

    for letter, words in alphabet_words.items():
        sorted_alphabet_words[letter] = sorted(words)

    return sorted_alphabet_words


def _rewrite_words(sorted_words: dict[str, list[str]]) -> None:
    with Path(_DICTIONARY_PATH).open('w', encoding='utf-8') as clean_file:
        clean_file.writelines(
            f'{word}\n' for words in sorted_words.values() for word in words
        )


def _main() -> None:
    _rewrite_words(_sort_words(_fill_alphabet_with_words(_create_alphabet())))


if __name__ == '__main__':
    _main()
