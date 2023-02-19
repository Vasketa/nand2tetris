"""VM Translator main script. Translates VM code into Hack assembly code."""
import argparse
from pathlib import Path
from typing import List, TextIO
from glob import glob
from collections import namedtuple

from VMTranslatorUtils import (
    read_file,
    parse_folder_name_from_argument,
    write_to_output,
    get_start_code_asm,
    get_jump_to_main_asm
)

from CommandTranslations import get_asm_code_from_command


#TODO: HOW TO JUMP TO MAIN
#TODO: HOW TO INDEX FILE
def load_files(File_tuple, vm_files_list):
    vm_files = []
    for vm_file_path in vm_files_list:
        with open(vm_file_path) as f:
            file_lines = read_file(f)
            vm_files.append(File_tuple(file_lines, Path(vm_file_path).stem))
    return vm_files

def get_index_to_file_code(vm_files):
    sum_lines = 0
    file_start_line_indexes = [sum_lines]
    for index in range(len(vm_files) - 1):
        sum_lines += len(vm_files[index].code)
        file_start_line_indexes.append(sum_lines)

    file_names = [vm_file.file_name for vm_file in vm_files]

    # File size to file stem
    file_range_to_file_name = list(
        zip(file_start_line_indexes, file_names)
    )
    return file_range_to_file_name

def join_code_from_files(vm_files) -> List:
    file_codes = [
        "\n".join(list_of_strings)
        for list_of_strings in [file.code for file in vm_files]
    ]

    return file_codes

if __name__ == "__main__":
    folder_name = parse_folder_name_from_argument()

    file_lines = []

    # Read all files
    # Declaring named tuple
    File_tuple = namedtuple('File', ['code', 'file_name'])

    vm_files_path = Path(folder_name) / "*.vm"
    vm_files_list = glob(str(vm_files_path))
    vm_files = load_files(File_tuple, vm_files_list)

    # Make index of when files start and end
    file_range_to_file_name = get_index_to_file_code(vm_files) 

    # Join files
    code_from_files = []
    for file in vm_files:
        for line in file.code:
            code_from_files.append(line)

    assembly_code = []
    assembly_code.append(get_start_code_asm())
    assembly_code.append(get_jump_to_main_asm())
    for current_line, line in enumerate(code_from_files):
        tokens = line.split(" ")
        assembly_code.append(get_asm_code_from_command(tokens, file_range_to_file_name, current_line))

    assembly_code_as_str = "".join(assembly_code)

    write_to_output(folder_name, assembly_code_as_str)
