// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

    @R2     // sets RAM[2] to 0 initially
    M=0

    @R0     // if RAM[0]==0 end program
    D=M     
    @END
    D;JEQ

    @R1     // if RAM[1]==0 end program
    D=M
    @END
    D;JEQ


    (SUM)
    @R0     // store RAM[0] in D
    D=M

    @R2     // add 1*RAM[0] to RAM[2]
    M=M+D   // at the end of the loop we have RAM[0]*(initial value of RAM[1]) in RAM[2]
    
    @R1     // subtract 1 from RAM[1]
    M=M-1
    D=M

    @SUM
    D;JGT   // back to the loop if RAM[1] > 0

    (END)   // infinite never-ending eternal loop
    @END
    0;JMP