from typing import Iterable, List, Tuple


class StringParser:
    @staticmethod
    def parse(string: str, allowed_characters: Iterable[str]) -> Tuple[str, str, str]:
        """
        Разбирает строку в формате 'key<op>value', где <op> — допустимый разделитель.

        Args:
            string: Входная строка (например, "age>30")
            allowed_characters: Список допустимых разделителей (например, ['>', '=', '<'])

        Returns:
           Кортеж из ключа, оператора и значения, например ("age", ">", "30").

        Raises:
            ValueError: Если список разделителей пуст.
            ValueError: Если не удалось однозначно разделить строку.
            ValueError: Если ключ или значение пустые.
        """
        if not allowed_characters:
            raise ValueError("Не переданы допустимые разделители")

        for char in allowed_characters:
            count = string.count(char)
            if count == 1:
                name, value = string.split(char)
                name, value = name.strip(), value.strip()
                if not name or not value:
                    raise ValueError(f"Вы передали некорректную строку в качестве условия: '{string}'")
                return name, char, value
            elif count > 1:
                raise ValueError(
                    f"Невозможно однозначно разделить строку: '{string}'. "
                    f"Содержит более одного символа-разделителя '{char}'"
                )
        raise ValueError(f"Не найден ни один допустимый разделитель в строке: '{string}'")
