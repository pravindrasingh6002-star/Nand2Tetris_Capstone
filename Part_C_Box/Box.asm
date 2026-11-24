
// Nand2Tetris Capstone - Part C
// Draw a 16-pixel-wide, 20-row-high box.
// Starting row = 32
// Box appears while a key is pressed.

(LOOP)
    @KBD
    D=M
    @DRAW
    D;JGT
    @CLEAR
    0;JMP

// Draw the black box
(DRAW)
    @17408
    D=A
    @address
    M=D

    @20
    D=A
    @counter
    M=D

(DRAW_LOOP)
    @address
    A=M
    M=-1

    @address
    D=M
    @32
    D=D+A
    @address
    M=D

    @counter
    MD=M-1
    @DRAW_LOOP
    D;JGT

    @LOOP
    0;JMP

// Clear the box when no key is pressed
(CLEAR)
    @17408
    D=A
    @address
    M=D

    @20
    D=A
    @counter
    M=D

(CLEAR_LOOP)
    @address
    A=M
    M=0

    @address
    D=M
    @32
    D=D+A
    @address
    M=D

    @counter
    MD=M-1
    @CLEAR_LOOP
    D;JGT

    @LOOP
    0;JMP
