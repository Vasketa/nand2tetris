@256
D=A
@SP
M=D
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_EQ_0
D;JEQ
@0
D=!A
@RET_ADDRESS_EQ_0
0;JMP
(RET_ADDRESS_EQ_0)
@SP
A=M
M=!D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_EQ_1
D;JEQ
@0
D=!A
@RET_ADDRESS_EQ_1
0;JMP
(RET_ADDRESS_EQ_1)
@SP
A=M
M=!D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_EQ_2
D;JEQ
@0
D=!A
@RET_ADDRESS_EQ_2
0;JMP
(RET_ADDRESS_EQ_2)
@SP
A=M
M=!D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_LT_0
M=D
D=0
M;JLT
@0
D=!A
@RET_ADDRESS_LT_0
0;JMP
(RET_ADDRESS_LT_0)
@SP
A=M
M=!D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_LT_1
M=D
D=0
M;JLT
@0
D=!A
@RET_ADDRESS_LT_1
0;JMP
(RET_ADDRESS_LT_1)
@SP
A=M
M=!D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_LT_2
M=D
D=0
M;JLT
@0
D=!A
@RET_ADDRESS_LT_2
0;JMP
(RET_ADDRESS_LT_2)
@SP
A=M
M=!D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_GT_0
M=D
D=0
M;JGT
@0
D=!A
@RET_ADDRESS_GT_0
0;JMP
(RET_ADDRESS_GT_0)
@SP
A=M
M=!D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_GT_1
M=D
D=0
M;JGT
@0
D=!A
@RET_ADDRESS_GT_1
0;JMP
(RET_ADDRESS_GT_1)
@SP
A=M
M=!D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@RET_ADDRESS_GT_2
M=D
D=0
M;JGT
@0
D=!A
@RET_ADDRESS_GT_2
0;JMP
(RET_ADDRESS_GT_2)
@SP
A=M
M=!D
@SP
M=M+1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=M+D
@SP
A=M
M=D
@SP
M=M+1
@112
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=D-M
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
M=-M
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=M&D
@SP
A=M
M=D
@SP
M=M+1
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@SP
AM=M-1
D=M
@R13
D=M|D
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
M=!M
@SP
M=M+1
