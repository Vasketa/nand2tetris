from enum import Enum

TEMP_BASE_ADDRESS = 5
GENERAL_PURPOSE_REGISTER = 13
HANDLE_RETURN_REGISTER = 14
STACK_START = 256


class Commands(Enum):
    PUSH_COMMAND = "push"
    POP_COMMAND = "pop"
    ADD_COMMAND = "add"
    SUBTRACT_COMMAND = "sub"
    NEGATIVE_COMMAND = "neg"
    EQUAL_COMMAND = "eq"
    GREATER_THAN_COMMAND = "gt"
    LESSER_THAN_COMMAND = "lt"
    AND_COMMAND = "and"
    OR_COMMAND = "or"
    LOGICAL_NOT_COMMAND = "not"
    LABEL_COMMAND = "label"
    GOTO_COMMAND = "goto"
    IF_GOTO_COMMAND = "if-goto"
    FUNCTION_COMMAND = "function"
    CALL_COMMAND = "call"
    RETURN_COMMAND = "return"

class MemorySegments(Enum):
    LOCAL = "local"
    ARGUMENT = "argument"
    THIS = "this"
    THAT = "that"
    CONSTANT = "constant"
    STATIC = "static"
    TEMP = "temp"
    POINTER = "pointer"

