from base.command_abs import Command
from base.string_parser import StringParser
from base.table import Table


class FilterCommand(Command):
    """Фильтрует строки таблицы по условию"""

    def __init__(self) -> None:
        self.command_name: str = "where"
        self.allowed_characters: str = "><="
        self.__operations: dict[str, str] = {
            ">": "__gt__",
            "<": "__lt__",
            "=": "__eq__",
        }

    def execute(self, table: Table, string: str) -> Table:
        """
        Фильтрует строки, удовлетворяющие условию
        Args:
            table: Исходная таблица
            string: Условие фильтрации (например, "age>30")
        Returns:
            Новая таблица с отфильтрованными строками
        Raises:
            ValueError: Если указано несуществующее поле или тип значения не подходит.
        """
        name, op, value = StringParser.parse(string, self.allowed_characters)

        if name not in table:
            raise ValueError(f"Нет поля '{name}' в таблице. Доступные: {table.head}")

        position: int = table.head.index(name)
        method_name: str = self.__operations[op] # Имя метода соответствующие знаку, например '=' - '__eq__'

        # Пробуем типизировать value, так как типизированны значения в столбце
        try:
            typed_value = table.types[position](value)
        except Exception as e:
            raise ValueError(f"Ошибка преобразования значения '{value}' в тип столбца '{name}': {e}")

        new_table: Table = Table()
        new_table.head = table.head

        # Добавляем строки, если соблюдается условие фильтрации, например cell_value.__eq__(typed_value)
        for row in table.rows:
            cell_value = row[position]
            if getattr(cell_value, method_name)(typed_value):
                new_table.add_row(row)

        return new_table

    @property
    def name(self) -> str:
        return self.command_name
