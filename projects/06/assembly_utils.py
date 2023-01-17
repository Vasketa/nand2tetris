"""Utility functions for the assembler."""
import argparse
from pathlib import Path
from typing import Dict, List, Set, TextIO, Tuple

from a_instruction import (
    is_A_instruction,
    is_label,
    is_numeric_address,
    is_special_register,
    is_special_symbol,
)


def write_to_output(file_name: str, bin_code: List[str]) -> None:
    """Write the binary code to a file.

    The file is written with the same name as the input file but ending suffix of .hack.
    """
    hack_file_name = Path(file_name).with_suffix(".hack")
    print(f"Output file: {hack_file_name}")
    with open(hack_file_name, "w") as f:
        f.write("\n".join([bin_line for bin_line in bin_code]))
        f.write("\n")


def parse_asm_file_from_argument() -> str:
    """Parse the assembly file name from the command line arguments."""
    parser = argparse.ArgumentParser(
        prog="Hack Assembler",
        description="Converts Hack assembly code into binary form",
    )

    parser.add_argument("asm_file")
    args = parser.parse_args()

    file_name = args.asm_file
    return file_name


def read_assembly_file(f: TextIO) -> List[str]:
    """Read the assembly file and return a list of lines.

    Ignores commented and empty lines and only returns lines of code containing
    assembly.
    """
    file_lines = []
    for line in f.readlines():
        line = line.strip()
        if line.startswith("//") or not line:
            continue
        else:
            file_lines.append(line)
    return file_lines


def get_labels_and_variables(
    assembly_lines: List[str],
) -> Tuple[Set[str], Dict[str, int], Dict[str, int]]:
    """Get all labels and variables in the assembly code.

    Identify if the symbols in the code are labels or variables, returning their
    respective index in the end. This is needed to correctly address their memory
    locations afterward.
    """
    labels, variables = [], []
    label_to_index = {}

    all_texts = []

    for index, line in enumerate(assembly_lines):
        if (
            not (a_instruction := is_A_instruction(line))
            or is_special_register(a_instruction)
            or is_numeric_address(a_instruction)
            or is_special_symbol(a_instruction)
        ) and not is_label(line):
            continue
        else:
            if label := is_label(line):
                labels.append(label)
                label_to_index[label] = calculate_label_offset(labels, index)
            elif a_instruction := is_A_instruction(line):
                all_texts.append(a_instruction)

    labels_set = set(labels)
    variables = get_variables(all_texts, labels_set)
    var_to_index = generate_var_to_index(variables)
    return labels_set, var_to_index, label_to_index


def calculate_label_offset(labels: List, index: int) -> int:
    """Calculate label - offset of deleted labels."""
    return index - (len(labels) - 1)


def generate_var_to_index(variables: List[str]) -> Dict[str, int]:
    """Create a map from variable to its index."""
    var_to_index = {}
    for index, var in enumerate(variables):
        var_to_index[var] = index
    return var_to_index


def get_variables(all_symbols: List[str], labels_set: Set[str]) -> List[str]:
    """Return a list of non-repeated variables.

    The variables are returned in the correct order of their appearance in the code.
    """
    seen_variables = set()
    variables = []

    for symbol in all_symbols:
        if symbol not in labels_set:
            if symbol in seen_variables:
                continue
            seen_variables.add(symbol)
            variables.append(symbol)
    return variables
