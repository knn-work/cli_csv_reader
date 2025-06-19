from base.command_abs import Command
from base.string_parser import StringParser
from base.table import Table


class OrderCommand(Command):
    """Сортирует строки по значению одного из столбцов."""

    def __init__(self):
        self.command_name = "order-by"
        self.allowed_characters = "="
        self.__operations = ["asc", "desc"]

    def execute(self, table: Table, string: str) -> Table:
        """
        Сортирует строки таблицы по одному из столбцов.
        Args:
            table: Исходная таблица.
            string: Строка вида column=asc или column=desc.
        Returns:
            Новая отсортированная таблица.
        Raises:
            ValueError: Если колонка не найдена или порядок не поддерживается.
        """
        name, _, order = StringParser.parse(string, self.allowed_characters)

        if name not in table:
            raise ValueError(f"Нет поля '{name}' в таблице. Доступные: {table.head}")
        if order not in self.__operations:
            raise ValueError(f"Неподдерживаемый порядок сортировки '{order}'. Ожидается: {self.__operations}")

        position: int = table.head.index(name)

        # Сортиров
        sorted_indexes: list[int] = sorted(range(len(table.rows)), key=lambda i: table.rows[i][position], reverse=order == "desc")

        new_table: Table = Table()
        new_table.head = table.head
        for i in sorted_indexes:
            new_table.add_row(table.rows[i])

        return new_table

    @property
    def name(self) -> str:
        return self.command_name
