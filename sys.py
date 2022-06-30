#!/usr/bin/python3

import click
from pyparsing import col
from System_info import System_info
from ImgPrinter import ImgPrinter


@click.command()
@click.option('--info', help='system information wanted.')
@click.argument('show')
def execute(info, show):
    try:
        system = System_info()
        printer = ImgPrinter()
        if info == "system":
            printer.print_list(system.system_info().split('\n'), 'system.jpg',)
        elif info == "cpu":
            printer.print_list(system.cpu_info().split(
                '\n'), 'cpu.jpg', color='red')
        elif info == "memory":
            printer.print_list(system.memory_info().split(
                '\n'), 'memory.jpg', height=310, color='blue')
        elif info == "disk":
            printer.print_list(system.disk_info().split(
                '\n'), 'disk.jpg', height=330, color='magenta')
        else:
            raise ValueError("Unsupported Info Type!")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    execute()
