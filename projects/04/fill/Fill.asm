// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


    (KBD_LISTENER)
    @8191   // stores last row of screen number on RAM[0]
    D=A
    @R0
    M=D

    @KBD    // reads keyboard input, stores it in D
    D=M;
    
    @PAINT_IT_WHITE     // if no key is pressed, goto paint it white label
    D;JEQ

    @PAINT_IT_BLACK     // else, goto paint it black label
    0;JMP


    (PAINT_IT_WHITE) // fills the screen with white pixels (0) from last address to first address
    @SCREEN
    D=A
    @R0
    D=D+M;  // stores current address to paint
    A=D
    M=0    // sets the 'ink' to white
    @R0
    M=M-1
    D=M
    @PAINT_IT_WHITE
    D;JGE
    
    @KBD_LISTENER   // skips paint it black
    0;JMP

    (PAINT_IT_BLACK) // fills the screen with black pixels (1) from last address to first address
    @SCREEN
    D=A
    @R0
    D=D+M;      // store current address to paint
    A=D
    M=-1        // sets the 'ink' to black since -1 = %B1111111111111111
    @R0
    M=M-1       // decreases the counter (address)
    D=M
    @PAINT_IT_BLACK
    D;JGE

    @KBD_LISTENER   // infinite never-ending eternal loop
    0;JMP