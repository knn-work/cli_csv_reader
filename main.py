import argparse
from typing import List

from base.command_abs import Command
from base.table import Table
from commands.aggregate import AggregateCommand
from commands.file import FileCommand
from commands.filters import FilterCommand
from commands.order import OrderCommand


def main() -> None:
    """
    Парсит аргументы командной строки и последовательно применяет команды к таблице.
    """
    parser = argparse.ArgumentParser(
        prog='Workmate',
        description='CLI-инструмент для работы с табличными данными(CSV)',
    )

    commands: List[Command] = [
        FileCommand(),      # select
        FilterCommand(),    # where
        OrderCommand(),     # order by
        AggregateCommand(), # aggregate
    ]

    # Добавление аргументов команд
    for command in commands:
        parser.add_argument(
            f'--{command.name.replace("_", "-")}',
            dest=command.name,
            help=command.__doc__,
        )

    try:
        args = parser.parse_args()
    except Exception:
        print("Ошибка: указан несуществующий аргумент. Используйте --help для списка опций.")
        return

    if getattr(args, "file", None) is None:
        print("Ошибка: необходимо указать файл как параметр. \n\tПример: --file filename.csv")
        return

    if  getattr(args, "aggregate", None) is not None and getattr(args, "where", None) is not None:
        print("Ошибка: необходимо использовать либо только --aggregate либо --where, не одновременно")
        return

    table = Table()

    for command in commands:
        arg_value = getattr(args, command.name, None)
        if arg_value is None:
            continue
        table = command.execute(table, arg_value)

    print(table)


if __name__ == '__main__':
    main()
