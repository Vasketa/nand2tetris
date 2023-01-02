// This file is not a part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/FillGood.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// This file was made to refactor and improve runtime when compared to Fill.asm

// RAM[0] will store a number relative to the current address
// RAM[1] will store if the screen is either black or white
// RAM[2] will store the color the screen will change to


    @R1     // stores that the screen is initially white
    M=0

    (KBD_LISTENER)
    @8191   // stores the number of the last row of the screen on RAM[0]
    D=A
    @R0
    M=D
    @SCREEN
    D=A
    @R0
    M=M+D   // stores the actual last row of screen on RAM[0], taht is, SCREEN + 8191

    @KBD    // reads keyboard input, stores it in D
    D=M;
    
    @SET_WHITE     // if no key is pressed, set the 'ink' to white
    D;JEQ

    @SET_BLACK     // else, sets the 'ink' to black
    0;JMP

    (SET_WHITE)    // set the 'ink' to white
    @R2
    M=0
    @R1
    D=M
    @PAINT
    D;JNE          // jumps to paint only if the screen is not already white
    
    @KBD_LISTENER // skips set black
    0;JMP

    (SET_BLACK)     // set the 'ink' to black
    @R2
    M=-1
    @R1
    D=M
    @PAINT
    D;JEQ           // jumps to paint only if the screen is not already black

    (PAINT) // fills the screen with the set 'ink' from last address to first address
    @R2
    D=M     // stores the 'ink' in D
    @R0
    A=M     // sets the address to get painted
    M=D     // paints the address
    @R1
    M=D     // changes the current stored color of the screen

    @R0
    M=M-1
    D=M
    @SCREEN
    D=D-A
    @PAINT
    D;JGE

    @KBD_LISTENER   // infinite never-ending eternal loop
    0;JMP