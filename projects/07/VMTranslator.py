"""VM Translator main script. Translates VM code into Hack assembly code."""
import argparse
from pathlib import Path
from typing import List, TextIO

from VMTranslatorUtils import (read_file, parse_file_name_from_argument,
                               write_to_output, get_start_code_asm)
from CommandTranslations import get_asm_code_from_command

if __name__ == "__main__":
    file_name = parse_file_name_from_argument()
    file_lines = []

    with open(file_name) as f:
        file_lines = read_file(f)

    assembly_code = []
    assembly_code.append(get_start_code_asm())
    for line in file_lines:
        tokens = line.split(" ")

        assembly_code.append(get_asm_code_from_command(tokens,file_name))

    assembly_code_as_str = "".join(assembly_code)

    write_to_output(file_name, assembly_code_as_str)