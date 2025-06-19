import csv
import os

from base.command_abs import Command
from base.table import Table


class FileCommand(Command):
    command_name = "file"

    def execute(self, table: Table, file_path: str) -> Table:
        """
        Сортирует строки таблицы по одному из столбцов.
        Args:
            table: Исходная таблица.
            file_path: Строка путь до CSV файла.
        Returns:
            Заполненная таблица данными из CSV файла.
        Raises:
            ValueError: Если колонка не найдена или порядок не поддерживается.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with open(file_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)

            table.head = next(csv_reader)
            for row in csv_reader:
                table.add_row(row)
        return table

    @property
    def name(self) -> str:
        return self.command_name
