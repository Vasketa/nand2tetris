"""Utility functions for the VM Translator."""
import argparse
from pathlib import Path
from typing import List, TextIO
import re
from VMTranslatorConstants import STACK_START

def read_file(f: TextIO) -> List[str]:
    """Read file and return a list of lines.

    Ignores commented and empty lines and only returns lines of code containing.
    """
    file_lines = []
    for line in f.readlines():
        if line.startswith("//") or not line:
            continue
        else:
            match = re.match("(.+)\/\/|.+", line)
            parsed_string = line
            if match:
                if match.group(1):
                    parsed_string = match.group(1)
                else:
                    parsed_string = match.group(0)
            else:
                continue
            file_lines.append(parsed_string.strip())
    return file_lines

def parse_folder_name_from_argument() -> str:
    """Parse the folder name from the command line arguments."""
    parser = argparse.ArgumentParser(
        prog="VM folder",
        description="VM folder to translate",
    )

    parser.add_argument("vm_folder")
    args = parser.parse_args()

    folder_name = args.vm_folder
    return folder_name

def write_to_output(folder_name: str, assembly_code: str) -> None:
    """Write the assembly code to a file.

    The file is written with the same name as the input file but ending suffix of .asm.
    """
    output_file = Path(folder_name) / Path(folder_name).stem
    assembly_file = output_file.with_suffix(".asm")
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

def get_call_and_jump_to_init_asm() -> str:
    asm_commands = [
        "@0",
        "D=A",
        "@SP",
        "AM=M+1",
        "M=D", # push 0 to stack
        "@LCL",
        "D=M", # Save LCL address in D
        "@SP",
        "A=M",
        "M=D", # Save LCL address in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        "@ARG",
        "D=M", # Save ARG address in D
        "@SP",
        "A=M",
        "M=D", # Save ARG address in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        "@THIS",
        "D=M", # Save THIS address in D
        "@SP",
        "A=M",
        "M=D", # Save THIS address in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        "@THAT",
        "D=M", # Save THAT address in D
        "@SP",
        "A=M",
        "M=D", # Save THAT address in the stack
        "@SP",
        "M=M+1", # Update stack pointer and save it in D
        "@Sys.init",
        "0;JMP"
    ]
    return join_commands(asm_commands)
