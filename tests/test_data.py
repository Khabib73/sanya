from pathlib import Path
from typing import Final

_DICTIONARY_PATH: Final = (
    Path(__file__).parent.parent
    / 'src'
    / 'sanya'
    / 'data'
    / 'dictionary_ru.txt'
)


def test_duplicate_words():
    """Check that the dictionary doesn't have duplicate words."""
    seen: set[str] = set()
    duplicates: list[str] = []
    with Path(_DICTIONARY_PATH).open(encoding='utf-8') as wrong_words:
        for word in wrong_words:
            if word in seen:
                duplicates.append(word)
            seen.add(word)

    # TODO: can this be made more informative?
    assert not duplicates
