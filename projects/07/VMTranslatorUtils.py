"""Utility functions for the VM Translator."""
import argparse
from pathlib import Path
from typing import List, TextIO

from VMTranslatorConstants import STACK_START

def read_file(f: TextIO) -> List[str]:
    """Read file and return a list of lines.

    Ignores commented and empty lines and only returns lines of code containing.
    """
    file_lines = []
    for line in f.readlines():
        line = line.strip()
        if line.startswith("//") or not line:
            continue
        else:
            file_lines.append(line)
    return file_lines

def parse_file_name_from_argument() -> str:
    """Parse the file name from the command line arguments."""
    parser = argparse.ArgumentParser(
        prog="VM File",
        description="VM File to translate",
    )

    parser.add_argument("vm_file")
    args = parser.parse_args()

    file_name = args.vm_file
    return file_name

def write_to_output(file_name: str, assembly_code: str) -> None:
    """Write the assembly code to a file.

    The file is written with the same name as the input file but ending suffix of .asm.
    """
    assembly_file = Path(file_name).with_suffix(".asm")
    print(f"Output file: {assembly_file}")
    with open(assembly_file, "w") as f:
        f.write(assembly_code)

def join_commands(commands: List[str]) -> str:
    """Join a list of commands into a single string."""
    return "\n".join(commands) + "\n"

def get_start_code_asm() -> str:
    """Get the assembly code for the start of the program.

    RAM[0] = 256
    """
    return join_commands([f"@{STACK_START}", "D=A", "@SP", "M=D"])
