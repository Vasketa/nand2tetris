"""This module contains the constants and patterns used throughout the code."""
import re

COMMON_REGISTERS = 16

SPECIAL_SYMBOL_ADDRESS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
}

PATTERNS = {
    "A_INSTRUCTION": r"^@(.+)",
    "SPECIAL_REG": r"^R(\d+)",
    "LABEL": r"^\((.+)\)",
    "SP": r"^SP$",
    "LCL": r"^LCL$",
    "ARG": r"^ARG$",
    "THIS": r"^THIS$",
    "THAT": r"^THAT$",
    "SCREEN": r"^SCREEN$",
    "KBD": r"^KBD$",
}

SPECIAL_SYMBOL_PATTERN = re.compile(
    "{}|{}|{}|{}|{}|{}|{}".format(
        PATTERNS["SP"],
        PATTERNS["LCL"],
        PATTERNS["ARG"],
        PATTERNS["THIS"],
        PATTERNS["THAT"],
        PATTERNS["SCREEN"],
        PATTERNS["KBD"],
    )
)

BIN_CODES = {
    "A_INSTRUCTION": "0",
    "C_INSTRUCTION": "1",
    "C_INSTRUCTION_UNUSED_BITS": "11",
}

COMP_PATTERN_TO_BITS = {
    "": "000000",
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "M": "110000",
    "!D": "001101",
    "!A": "110001",
    "!M": "110001",
    "-D": "001111",
    "-A": "110011",
    "-M": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "M+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "M-1": "110010",
    "D+A": "000010",
    "A+D": "000010",
    "D+M": "000010",
    "M+D": "000010",
    "D-A": "010011",
    "D-M": "010011",
    "A-D": "000111",
    "M-D": "000111",
    "D&A": "000000",
    "A&D": "000000",
    "D&M": "000000",
    "M&D": "000000",
    "D|A": "010101",
    "A|D": "010101",
    "D|M": "010101",
    "M|D": "010101",
}

# aBIT 'chooses' if the operation is carried with the
# contents of the A Register of M register
COMP_PATTERN_TO_aBIT = {
    "": "0",
    "0": "0",
    "1": "0",
    "-1": "0",
    "D": "0",
    "A": "0",
    "M": "1",
    "!D": "0",
    "!A": "0",
    "!M": "1",
    "-D": "0",
    "-A": "0",
    "-M": "1",
    "D+1": "0",
    "A+1": "0",
    "M+1": "1",
    "D-1": "0",
    "A-1": "0",
    "M-1": "1",
    "D+A": "0",
    "A+D": "0",
    "D+M": "1",
    "M+D": "1",
    "D-A": "0",
    "D-M": "1",
    "A-D": "0",
    "M-D": "1",
    "D&A": "0",
    "A&D": "0",
    "D&M": "1",
    "M&D": "1",
    "D|A": "0",
    "A|D": "0",
    "D|M": "1",
    "M|D": "1",
}

DESTINATION_PATTERN_TO_BITS = {
    "": "000",
    "M": "001",  # RAM[A]
    "D": "010",  # D register
    "MD": "011",  # D register and RAM[A]
    "A": "100",  # A register
    "AM": "101",  # A register and RAM[A]
    "AD": "110",  # A register and D register
    "AMD": "111",  # A register, D register, and RAM[A]
}

JUMP_PATTERN_TO_BITS = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}
