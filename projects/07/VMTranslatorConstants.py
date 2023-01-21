from enum import Enum

STACK_START = 256
GENERAL_PURPOSE_REGISTER = 13
TEMP_BASE_ADDRESS = 5

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
    FUNCTION_COMMAND = "Function"
    CALL_COMMAND = "Call"
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

