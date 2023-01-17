"""Module for generating binary code for C instructions."""

from typing import Tuple

from assembler_constants import (
    BIN_CODES,
    COMP_PATTERN_TO_BITS,
    DESTINATION_PATTERN_TO_BITS,
    JUMP_PATTERN_TO_BITS,
    COMP_PATTERN_TO_aBIT,
)


def generate_C_instruction_in_binary(assembly_line: str) -> str:
    """Translate a C instruction in Hack assembly into binary."""
    destination, compute, jump = tokenize_C_instruction(assembly_line)

    # 'chooses' if the operation is carried with the contents of the
    # A Register of M register
    a_bit = COMP_PATTERN_TO_aBIT[compute]
    computation_bits = COMP_PATTERN_TO_BITS[compute]
    destination_bits = DESTINATION_PATTERN_TO_BITS[destination]
    jump_bits = JUMP_PATTERN_TO_BITS[jump]

    C_instruction = (
        f"{BIN_CODES['C_INSTRUCTION']}{BIN_CODES['C_INSTRUCTION_UNUSED_BITS']}"
        f"{a_bit}{computation_bits}{destination_bits}{jump_bits}"
    )
    return C_instruction


def tokenize_C_instruction(assembly_line: str) -> Tuple[str, str, str]:
    """Tokenizes a C instruction into its destination, compute and jump parts.

    Description of the C instruction syntax:

    Symbolic syntax: "dest = comp ;" jump comp is mandatory.
    If "dest" is empty, the "=" is omitted;
    If "jump" is empty, the ";" is omitted

    Binary syntax: 1 1 1 a c c c c c c d d d j j j
    C instruction  _
    not used         ___
    comp bits            _____________
    dest bits                          _____
    jump bits                                _____

    Args:
        assembly_line (str): C instruction in assembly

    Returns:
        Tuple[str, str, str]: destination, compute and jump parts of the C instruction
    """
    destination_bits = ""
    compute_bits = ""
    jump_bits = ""

    if "=" in assembly_line:
        equals_index = assembly_line.index("=")
        destination_bits = assembly_line[:equals_index]
        assembly_line = assembly_line[equals_index + 1 :]

    if ";" in assembly_line:
        semicolon_index = assembly_line.index(";")
        jump_bits = assembly_line[semicolon_index + 1 :]
        assembly_line = assembly_line[:semicolon_index]

    compute_bits = assembly_line

    return destination_bits, compute_bits, jump_bits
