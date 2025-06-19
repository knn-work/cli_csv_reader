from base.command_abs import Command
from base.string_parser import StringParser
from base.table import Table


class AggregateCommand(Command):
    """Выполняет агрегацию: avg, min или max по одному из столбцов."""

    def __init__(self):
        self.command_name = "aggregate"
        self.allowed_characters: str = "="
        self.__operations = {
            "avg": self.__avg,
            "min": self.__min,
            "max": self.__max,
        }

    def execute(self, table: Table, string: str) -> Table:
        """
        Выполняет агрегацию по указанному столбцу.
        Args:
            table: Исходная таблица.
            string: Выражение типа column=func, где func — avg/min/max.
        Returns:
            Таблица с одной строкой и одной колонкой (результатом агрегации).
        Raises:
            ValueError: Если поле или операция не поддерживаются.
        """
        name, _, func = StringParser.parse(string, self.allowed_characters)

        if name not in table:
            raise ValueError(f"Нет поля '{name}' в таблице. Доступные: {table.head}")
        if func not in self.__operations:
            raise ValueError(f"Неподдерживаемая агрегация '{func}'. Доступные: {list(self.__operations)}")

        position = table.head.index(name)
        method = self.__operations[func]

        result = method(table, position)

        new_table: Table = Table()
        new_table.head = [func]
        new_table.add_row([result])
        return new_table

    @staticmethod
    def __avg(table: Table, position: int) -> float:
        values = [row[position] for row in table.rows]
        return sum(values) / len(values)

    @staticmethod
    def __min(table: Table, position: int) -> float:
        return min(row[position] for row in table.rows)

    @staticmethod
    def __max(table: Table, position: int) -> float:
        return max(row[position] for row in table.rows)

    @property
    def name(self) -> str:
        return self.command_name
