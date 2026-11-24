# Nand2Tetris Capstone Project
## Make the Computer Draw a Box

**Course:** Nand2Tetris – I (ETCCNT301)  
**University:** K.R. Mangalam University  
**School:** School of Engineering & Technology  
**Student Name:** Pravindra Singh  
**Roll Number:** 2501730132  
**Personal Number (K):** 32  

---

## 1. Project Overview

This repository contains my Nand2Tetris Capstone Project, which focuses on understanding computer architecture, Hack assembly language, and the internal working of a computer system.

The project is divided into three major parts:

- **Part A – Computer Construction:** Implementation and testing of CPU, Memory, and Computer chips using HDL.
- **Part B – Hack Assembler:** Development of a two-pass assembler in Python to translate Hack assembly instructions into 16-bit binary machine code.
- **Part C – Make the Computer Draw a Box:** Development of a Hack assembly program that draws a black rectangular box on the screen while a keyboard key is pressed and clears it when the key is released.

---

## 2. Project Structure

```text
Nand2Tetris_Capstone/
│
├── Part_A_Computer/
│   ├── CPU.hdl
│   ├── Memory.hdl
│   ├── Computer.hdl
│   └── Screenshots/
│
├── Part_B_Assembler/
│   ├── assembler.py
│   ├── verify_hack.py
│   ├── README.md
│   ├── test_files/
│   │   ├── Add.asm
│   │   ├── Add.hack
│   │   ├── Max.asm
│   │   ├── Max.hack
│   │   ├── Rect.asm
│   │   ├── Rect.hack
│   │   ├── Pong.asm
│   │   └── Pong.hack
│   └── Screenshots/
│
├── Part_C_Box/
│   ├── Box.asm
│   ├── Box.hack
│   └── Screenshots/
│
├── Screenshots/
│
└── README.md
```

---

## 3. Part A – Computer Construction

In this part, the main components of the Hack computer were implemented using Hardware Description Language (HDL).

### Components Implemented

- **CPU.hdl:** Implements the central processing unit.
- **Memory.hdl:** Implements the computer memory interface.
- **Computer.hdl:** Connects the CPU and Memory to form the complete computer.

### Testing

The following official test scripts were used:

- CPU.tst
- Memory.tst
- ComputerAdd.tst
- ComputerMax.tst
- ComputerRect.tst

**Result:** The Computer tests were completed successfully.

---

## 4. Part B – Python Hack Assembler

A Hack assembler was developed using Python. It converts Hack assembly language (`.asm`) files into binary machine code (`.hack`).

### Features

1. Two-pass assembly process.
2. Removal of comments and unnecessary whitespace.
3. Label detection and symbol-table management.
4. Translation of A-instructions and C-instructions.
5. Support for predefined Hack symbols.
6. Automatic variable allocation starting from RAM address 16.
7. Generation of 16-bit binary machine instructions.
8. Duplicate-label warning feature.

### Test Programs

| Program | Instructions Generated |
|---|---:|
| Add.asm | 6 |
| Max.asm | 16 |
| Rect.asm | 25 |
| Pong.asm | 27,483 |

### Verification

All four programs were assembled and their generated machine-code files were compared with the official Nand2Tetris assembler.

**Result:** All four comparisons were successful.

### Technologies Used

- Python
- Hack Assembly Language
- Nand2Tetris Online IDE

---

## 5. Part C – Make the Computer Draw a Box

The objective of this part was to create a rectangular box on the Hack computer screen using assembly language.

### Box Specifications

| Parameter | Value |
|---|---|
| Personal Number (K) | 32 |
| Starting Row | 32 |
| Height | 20 rows |
| Width | 16 pixels |
| Starting Address | SCREEN + (32 × 32) |
| Starting Memory Address | 17408 |

### Working

- The program continuously checks the keyboard input.
- When a key is pressed, the program draws a black rectangular box.
- When the key is released, the program clears the rectangular area.
- The program continuously repeats this process.

### Files

- `Box.asm` – Hack assembly source code.
- `Box.hack` – Generated machine code.

### Result

The program was assembled using the Python assembler and executed in the Nand2Tetris CPU Emulator.

The box appeared when a key was pressed and disappeared when the key was released.

---

## 6. Technologies and Tools Used

| Technology / Tool | Purpose |
|---|---|
| HDL | Hardware chip implementation |
| Python | Hack assembler development |
| Hack Assembly | Low-level programming |
| Nand2Tetris Online IDE | HDL and assembler testing |
| CPU Emulator | Executing the Box program |
| Git | Version control |
| GitHub | Project hosting and submission |

---

## 7. How to Run the Python Assembler

### Requirements

- Python 3 installed on your computer.
- Hack assembly source file (`.asm`).

### Steps

1. Open Command Prompt.
2. Navigate to the Part B folder.
3. Run the assembler with the source file.

Example:

```bash
cd Part_B_Assembler
python assembler.py test_files/Add.asm
```

The assembler generates the corresponding `.hack` file.

### Run the Box Program

From the project directory:

```bash
cd Part_C_Box
python ..\Part_B_Assembler\assembler.py Box.asm
```

Open the generated `Box.hack` file in the Nand2Tetris CPU Emulator to execute the program.

---

## 8. Learning Outcomes

Through this project, I learned:

- Fundamentals of computer architecture.
- Implementation of CPU and memory using HDL.
- Working of the Hack computer platform.
- Assembly language programming.
- Two-pass assembler design.
- Symbol tables and memory addressing.
- Conversion of assembly instructions into binary machine code.
- Testing and debugging hardware and software components.
- Using Git and GitHub for project management.

---

## 9. Conclusion

This capstone project provided practical experience with the internal working of a computer system, from hardware construction to assembly language programming.

By implementing HDL components, developing a Python-based assembler, and creating a screen-drawing program, I gained a better understanding of how hardware and software work together in a computer system.

---

**Project Repository:**  
https://github.com/pravindrasingh6002-star/Nand2Tetris_Capstone

**Developed by:** Pravindra Singh  
**K.R. Mangalam University**
# Nand2Tetris_Capstone
