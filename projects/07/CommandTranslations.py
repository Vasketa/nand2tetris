"""This module generates the assembly code given a VM command"""
from typing import List, Tuple, Literal
#from typing_extensions import Literal
from pathlib import Path

from VMTranslatorConstants import (TEMP_BASE_ADDRESS, GENERAL_PURPOSE_REGISTER, HANDLE_RETURN_REGISTER,
                                   Commands, MemorySegments)
from VMTranslatorUtils import join_commands

count_equal = -1
count_greater_than = -1
count_lesser_than = -1
count_call = -1
current_function = ""

def get_asm_code_from_command(tokens: List[str], file_range_to_file_name: List[Tuple[int, str]], current_line: int) -> str:
    vm_command = tokens[0]

    file_stem = ""
    for file_start_index, file_name in reversed(file_range_to_file_name):
        if current_line >= file_start_index:
            file_stem = file_name
            break

    global count_equal
    global count_greater_than
    global count_lesser_than
    global current_function
    global count_call

    if vm_command == Commands.PUSH_COMMAND.value:
        return get_push_command_asm(tokens, file_stem)
    elif vm_command == Commands.POP_COMMAND.value:
        return get_pop_command_asm(tokens, file_stem)
    elif vm_command == Commands.ADD_COMMAND.value:
        return get_add_asm()
    elif vm_command == Commands.SUBTRACT_COMMAND.value:
        return get_sub_asm()
    elif vm_command == Commands.NEGATIVE_COMMAND.value:
        return get_neg_asm()
    elif vm_command == Commands.EQUAL_COMMAND.value:
        count_equal += 1
        return get_eq_asm()
    elif vm_command == Commands.GREATER_THAN_COMMAND.value:
        count_greater_than += 1
        return get_gt_asm()
    elif vm_command == Commands.LESSER_THAN_COMMAND.value:
        count_lesser_than += 1
        return get_lt_asm()
    elif vm_command == Commands.AND_COMMAND.value:
        return get_and_asm()
    elif vm_command == Commands.OR_COMMAND.value:
        return get_or_asm()
    elif vm_command == Commands.LOGICAL_NOT_COMMAND.value:
        return get_not_asm()
    elif vm_command == Commands.LABEL_COMMAND.value:
        return get_label_asm(tokens)
    elif vm_command == Commands.GOTO_COMMAND.value:
        return get_goto_asm(tokens, file_stem)
    elif vm_command == Commands.IF_GOTO_COMMAND.value:
        return get_ifgoto_asm(tokens, file_stem)
    elif vm_command == Commands.FUNCTION_COMMAND.value:
        return get_function_asm(tokens, file_stem)
    elif vm_command == Commands.CALL_COMMAND.value:
        count_call += 1
        return get_call_asm(tokens, file_stem)
    elif vm_command == Commands.RETURN_COMMAND.value:
        return get_return_asm(tokens)



def get_push_command_asm(tokens: List[str], file_stem: str) -> str:
    """Get the assembly code for a push command."""
    segment = tokens[1]
    index = tokens[2]

    if segment == MemorySegments.CONSTANT.value:
        return get_push_constant_asm(index)
    elif segment == MemorySegments.STATIC.value:
        return get_push_static_asm(index, file_stem)
    elif segment == MemorySegments.POINTER.value:
        return get_push_pointer_asm(index)
    elif segment == MemorySegments.THIS.value:
        return get_push_this_asm(index)
    elif segment == MemorySegments.THAT.value:
        return get_push_that_asm(index)
    elif segment == MemorySegments.LOCAL.value:
        return get_push_local_asm(index)
    elif segment == MemorySegments.ARGUMENT.value:
        return get_push_argument_asm(index)
    elif segment == MemorySegments.TEMP.value:
        return get_push_temp_asm(index)
    else:
        print(f"[PUSH COMMAND EXCEPTION, SEGMENT = {segment}]")
        exit(2)

def get_push_constant_asm(index: str) -> str:
    """Get the assembly code for the push constant command."""
    asm_commands = [
        f"@{index}",
        "D=A", # Store the constant in D
        "@SP",
        "A=M",  
        "M=D", # Store the constant in the stack
        "@SP",
        "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_push_static_asm(index: str, file_stem: str) -> str:
    """Get the assembly code for the push static command."""
    asm_commands = [
        f"@{file_stem}.{index}", #Access Static variable
        "D=M", # Store the value in D
        "@SP",
        "A=M",  
        "M=D", # Store the value in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        ]
    return join_commands(asm_commands)

def get_push_pointer_asm(index: Literal["0","1"]) -> str:
    """Get the assembly code for the push pointer command."""
    asm_commands = [         
        # Access the pointer in the RAM (pointer 0 -> RAM[3], pointer 1 -> RAM[4])
        f"@R{int(index)+3}",
        "D=M", # Store the value in D
        "@SP",
        "A=M",  
        "M=D", # Store the value in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        ]
    return join_commands(asm_commands)

def get_push_this_asm(index: str) -> str:
    """Get the assembly code for the push this command."""
    asm_commands = [         
        f"@{index}",
        "D=A", # Store the index in D
        "@THIS",
        "A=M+D", # Select this(i)
        "D=M", # Store this(i) in D
        "@SP",
        "A=M",  
        "M=D", # Store the value in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        ]
    return join_commands(asm_commands)

def get_push_that_asm(index: str) -> str:
    """Get the assembly code for the push that command."""
    asm_commands = [         
        f"@{index}",
        "D=A", # Store the index in D
        "@THAT",
        "A=M+D", # Select that(i)
        "D=M", # Store that(i) in D
        "@SP",
        "A=M",  
        "M=D", # Store the value in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        ]
    return join_commands(asm_commands)
    
def get_push_local_asm(index: str) -> str:
    """Get the assembly code for the push local command."""
    asm_commands = [         
        f"@{index}",
        "D=A", # Store the index in D
        "@LCL",
        "A=M+D", # Select local(i)
        "D=M", # Store local(i) in D
        "@SP",
        "A=M",  
        "M=D", # Store the value in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        ]
    return join_commands(asm_commands)

def get_push_argument_asm(index: str) -> str:
    """Get the assembly code for the push argument command."""
    asm_commands = [         
        f"@{index}",
        "D=A", # Store the index in D
        "@ARG",
        "A=M+D", # Select argument(i)
        "D=M", # Store argument(i) in D
        "@SP",
        "A=M",  
        "M=D", # Store the value in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        ]
    return join_commands(asm_commands)

def get_push_temp_asm(index: str) -> str:
    """Get the assembly code for the push temp command."""
    asm_commands = [         
        f"@{index}",
        "D=A", # Store the index in D
        f"@{TEMP_BASE_ADDRESS}",
        "A=A+D", # Select temp(i)
        "D=M", # Store temp(i) in D
        "@SP",
        "A=M",  
        "M=D", # Store the value in the stack
        "@SP",
        "M=M+1", # Update stack pointer
        ]
    return join_commands(asm_commands)    

def get_pop_command_asm(tokens: List[str], file_stem: str) -> str:
    """Get the assembly code for a pop command."""
    segment = tokens[1]
    index = tokens[2]

    if segment == MemorySegments.STATIC.value:
        return get_pop_static_asm(index, file_stem)
    elif segment == MemorySegments.POINTER.value:
        return get_pop_pointer_asm(index)
    elif segment == MemorySegments.THIS.value:
        return get_pop_this_asm(index)
    elif segment == MemorySegments.THAT.value:
        return get_pop_that_asm(index)
    elif segment == MemorySegments.LOCAL.value:
        return get_pop_local_asm(index)
    elif segment == MemorySegments.ARGUMENT.value:
        return get_pop_argument_asm(index)
    elif segment == MemorySegments.TEMP.value:
        return get_pop_temp_asm(index)
    else:
        print(f"[POP COMMAND EXCEPTION, SEGMENT = {segment}]")
        exit(3)
    
def get_pop_static_asm(index: str, file_stem: str) -> str:
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointe
        "D=M", # Store the stack_top in D
        f"@{file_stem}.{index}",
        "M=D", # Store the value in static i
    ]
    return join_commands(asm_commands)

def get_pop_pointer_asm(index: Literal["0","1"]) -> str:
    """Get the assembly code for the pop pointer command."""
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the stack_top in D
        f"@R{int(index)+3}",
        "M=D", # Store the value in pointer i
    ]
    return join_commands(asm_commands)

def get_pop_this_asm(index: str) -> str:
    """Get the assembly code for the pop this command."""
    asm_commands = [
        f"@{index}",
        "D=A",
        "@THIS",
        "D=D+M", # Store the address of this(i) in D 
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the address of this(i) in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the stack_top in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "A=M", # Select this(i)
        "M=D", # Store the value in this(i)
    ]
    return join_commands(asm_commands)

def get_pop_that_asm(index: str) -> str:
    """Get the assembly code for the pop that command."""
    asm_commands = [
        f"@{index}",
        "D=A",
        "@THAT",
        "D=D+M", # Store the address of that(i) in D 
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the address of that(i) in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the stack_top in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "A=M", # Select that(i)
        "M=D", # Store the value in that(i)
    ]
    return join_commands(asm_commands)

def get_pop_local_asm(index: str) -> str:
    """Get the assembly code for the pop local command."""
    asm_commands = [
        f"@{index}",
        "D=A",
        "@LCL",
        "D=D+M", # Store the address of local(i) in D 
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the address of local(i) in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the stack_top in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "A=M", # Select local(i)
        "M=D", # Store the value in local(i)
    ]
    return join_commands(asm_commands)

def get_pop_argument_asm(index: str) -> str:
    """Get the assembly code for the pop argument command."""
    asm_commands = [
        f"@{index}",
        "D=A",
        "@ARG",
        "D=D+M", # Store the address of argument(i) in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the address of argument(i) in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the stack_top in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "A=M", # Select argument(i)
        "M=D", # Store the value in argument(i)
    ]
    return join_commands(asm_commands)

def get_pop_temp_asm(index: str) -> str:
    """Get the assembly code for the pop temp command."""
    asm_commands = [
        f"@{index}",
        "D=A",
        f"@{TEMP_BASE_ADDRESS}",
        "D=D+A", # Store the address of temp(i) in D 
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the address of temp(i) in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the stack_top in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "A=M", # Select temp(i)
        "M=D", # Store the value in temp(i)
    ]
    return join_commands(asm_commands)

def get_add_asm() -> str:
    """Get the assembly code for the add command."""
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 1st argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the 1st argument in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 2nd argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "D=M+D", # Sum the two numbers and store the result in D
        "@SP",
        "A=M",
        "M=D", # Store the result in the stack
        "@SP",
        "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_sub_asm() -> str:
    """Get the assembly code for the sub command."""
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 1st argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the 1st argument in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 2nd argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "D=D-M", # Subtract the numbers and store the result in D (2nd - 1st)
        "@SP",
        "A=M",  
        "M=D", # Store the result in the stack
        "@SP",
        "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_neg_asm() -> str:
    """Get the assembly code for the neg command."""
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "M=-M", # Store -(value) in the stack
        "@SP",
        "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_eq_asm() -> str:
    """Get the assembly code for the eq command."""
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 1st argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the 1st argument in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 2nd argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "D=D-M", # Subtract the numbers and store in D (2nd - 1st)
        f"@RET_ADDRESS_EQ_{count_equal}", 
        "D;JEQ", # If they're equal, goto return_addr (D=0)
        "@0",
        "D=!A", # If they're not equal (D=-1)
        f"@RET_ADDRESS_EQ_{count_equal}",
        "0;JMP", # goto return_addr (D=-1)
        f"(RET_ADDRESS_EQ_{count_equal})", # Set return_addr
        "@SP",
        "A=M",
        "M=!D", # Swap values so that true=-1, false=0
        "@SP",
        "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_gt_asm() -> str:
    """Get the assembly code for the gt command."""
    asm_commands = [
    "@SP",
    "AM=M-1", # Update and select stack pointer
    "D=M", # Store the 1st argument in D
    f"@R{GENERAL_PURPOSE_REGISTER}",
    "M=D", # Store the 1st argument in GEN_P_REG
    "@SP",
    "AM=M-1", # Update and select stack pointer
    "D=M", # Store the 2nd argument in D
    f"@R{GENERAL_PURPOSE_REGISTER}",
    "D=D-M", # Subtract the numbers and store in D (2nd - 1st)
    f"@RET_ADDRESS_GT_{count_greater_than}",
    "M=D",
    "D=0", 
    "M;JGT", # Se 2nd>1st, goto return_addr (D=0)
    "@0",
    "D=!A", # Se 2nd<1st (D=-1)
    f"@RET_ADDRESS_GT_{count_greater_than}",
    "0;JMP", # goto return_addr (D=-1)
    f"(RET_ADDRESS_GT_{count_greater_than})", # Set return_addr
    "@SP",
    "A=M",
    "M=!D", # Swap values so that true=-1, false=0
    "@SP",
    "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_lt_asm() -> str:
    """Get the assembly code for the lt command."""
    asm_commands = [
    "@SP",
    "AM=M-1", # Update and select stack pointer
    "D=M", # Store the 1st argument in D
    f"@R{GENERAL_PURPOSE_REGISTER}",
    "M=D", # Store the 1st argument in GEN_P_REG
    "@SP",
    "AM=M-1", # Update and select stack pointer
    "D=M", # Store the 2nd argument in D
    f"@R{GENERAL_PURPOSE_REGISTER}",
    "D=D-M", # Subtract the numbers and store in D (2nd - 1st)
    f"@RET_ADDRESS_LT_{count_lesser_than}",
    "M=D",
    "D=0", 
    "M;JLT", # If 2nd<1st, goto return_addr (D=0)
    "@0",
    "D=!A", # If 2nd>1st (D=-1)
    f"@RET_ADDRESS_LT_{count_lesser_than}",
    "0;JMP", # goto return_addr (D=-1)
    f"(RET_ADDRESS_LT_{count_lesser_than})",  # Set return_addr
    "@SP",
    "A=M",
    "M=!D", # Swap values so that true=-1, false=0
    "@SP",
    "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_and_asm() -> str:
    """Get the assembly code for the and command."""
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 1st argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the 1st argument in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 2nd argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "D=M&D", # Store the bitwise and in D
        "@SP",
        "A=M",  
        "M=D", # Store the bitwise and in the stack
        "@SP",
        "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_or_asm() -> str:
    """Get the assembly code for the or command."""
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 1st argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=D", # Store the 1st argument in GEN_P_REG
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store the 2nd argument in D
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "D=M|D", # Store the bitwise or in D
        "@SP",
        "A=M",  
        "M=D", # Store the bitwise or in the stack
        "@SP",
        "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_not_asm() -> str:
    """Get the assembly code for the not command."""
    asm_commands =[
    "@SP",
    "AM=M-1", # Update and select stack pointer
    "M=!M", # Store !(value) in the stack
    "@SP",
    "M=M+1", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_label_asm(tokens: List[str]) -> str:
    """Get the assembly code for the label command."""
    label_name = tokens[1]
    return f"({current_function}${label_name})\n"

def get_goto_asm(tokens: List[str], file_stem: str) -> str:
    """Get the assembly code for the goto command."""
    label_name = tokens[1]
    asm_commands = []
    asm_commands = [
        f"@{current_function}${label_name}",
        "0;JMP", # Unconditional jump to a label
    ]
    return join_commands(asm_commands)

def get_ifgoto_asm(tokens: List[str], file_stem: str) -> str:
    """Get the assembly code for the if-goto command."""
    label_name = tokens[1]
    asm_commands = [
        "@SP",
        "AM=M-1", # Update and select stack pointer
        "D=M", # Store condition in D
        f"@{current_function}${label_name}",
        "D;JNE", # Jump to label if condition != false
    ]
    return join_commands(asm_commands)

def get_function_asm(tokens: List[str], file_stem: str) -> str:
    """Get the assembly code for the function command."""
    global current_function
    function_name = tokens[1]
    local_length = tokens[2]
    current_function = function_name
    asm_commands = [
        f"({current_function})", # Set entry label
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=0", # Clear GEN_P_REG
        f"@{local_length}",
        "D=A", # Save local_length in D
        f"@{current_function}_CLEARED_LCL",
        "D;JEQ", # Jump to cleared_LCL if local_length == 0
        f"({current_function}_CLEAR_LCL)",
        "D=0", 
        "@SP",
        "A=M",
        "M=D", # Push 0 to stack
        "@SP",
        "M=M+1", # Update stack pointer
        "@1", # Loop counter
        "D=A",
        f"@R{GENERAL_PURPOSE_REGISTER}",
        "M=M+D", # Increment *GEN_P_REG
        "D=M",
        f"@{local_length}",
        "D=D-A",
        f"@{current_function}_CLEAR_LCL",
        "D;JNE", # Back to loop while *GEN_P_REG - local_length != 0
        f"({current_function}_CLEARED_LCL)",
        f"@{local_length}",
        "D=A", # Save the length of LCL segment in D
        "@SP",
        "M=M+D", # Update stack pointer
    ]
    return join_commands(asm_commands)

def get_call_asm(tokens: List[str], file_stem: str) -> str:
    """Get the assembly code for the call command."""
    function_name = tokens[1]
    argument_length = tokens[2]
    asm_commands = [
        f"@RET_ADDRESS_CALL_{function_name}_{count_call}",
        "D=A",
        "@SP", # Save return address address in D
        "A=M",
        "M=D", # Save return adress in the stack
        "@SP",
        "M=M+1", # Update stack pointer
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
        "MD=M+1", # Update stack pointer and save it in D
        "@5",
        "D=D-A", # D = (SP address) - 5
        f"@{argument_length}",
        "D=D-A", # D = (SP address) - 5 - len(arguments)
        "@ARG",
        "M=D", # Set new ARG address
        "@SP",
        "D=M", # Save stack address in D
        "@LCL",
        "M=D", # Set new local segment (LCL = SP)
        f"@{function_name}",
        "0;JMP",
        f"(RET_ADDRESS_CALL_{function_name}_{count_call})", # Set return address
    ]
    return join_commands(asm_commands)

def get_return_asm(tokens: List[str]) -> str:
    asm_commands = [
        "@5",
        "D=A",
        "@LCL",
        "A=M-D", # Return address = *(LCL - 5)
        "D=M", # Save return address in D
        f"@R{HANDLE_RETURN_REGISTER}",
        "M=D", # *HANDLE_RETURN_REGISTER = return address
        "@SP",
        "A=M-1",
        "D=M", # Store return value in D 
        "@ARG",
        "A=M",
        "M=D", # Replace ARG[0] with the return value
        "@ARG",
        "D=M", # Store ARG address in D
        "@SP", 
        "M=D+1", # Set SP address = ARG address + 1
        "@LCL",
        "A=M-1",
        "D=M", # Save caller's (THAT address) in D
        "@THAT",
        "M=D", # Save caller's (THAT address) in THAT
        "@2",
        "D=A",
        "@LCL",
        "A=M-D",
        "D=M", # Save caller's (THIS address) in D
        "@THIS",
        "M=D", # Save caller's (THIS address) in THIS
        "@3",
        "D=A",
        "@LCL",
        "A=M-D",
        "D=M", # Save caller's (ARG address) in D
        "@ARG",
        "M=D", # Save caller's (ARG address) in ARG
        "@4",
        "D=A",
        "@LCL",
        "A=M-D",
        "D=M", # Save caller's (LCL address) in D
        "@LCL",
        "M=D", # Save caller's (LCL address) in LCL
        f"@R{HANDLE_RETURN_REGISTER}",
        "A=M", 
        "0;JMP", # goto function return address
    ]
    return join_commands(asm_commands)