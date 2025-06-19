import csv
import os

from base.command_abs import Command
from base.table import Table


class FileCommand(Command):
    command_name = "file"

    def execute(self, table: Table, file_path: str) -> Table:
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
