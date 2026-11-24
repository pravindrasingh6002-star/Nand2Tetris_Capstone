# Nand2Tetris Capstone – Part B: Python Hack Assembler

## Project Overview

This project implements a Hack Assembler using Python as part of the Nand2Tetris Capstone Project (Part B).

The assembler converts Hack Assembly Language (`.asm`) programs into 16-bit binary machine code (`.hack`) that can be executed by the Hack Computer.

The project demonstrates the working principles of an assembler, including instruction translation, symbol management, label resolution, and machine-code generation.

## Objectives

- Develop a Hack Assembler using Python.
- Convert A-instructions into binary machine code.
- Convert C-instructions into binary machine code.
- Implement symbol table management.
- Resolve labels and variables.
- Generate valid 16-bit Hack machine instructions.
- Verify generated machine code using the Nand2Tetris Online IDE.

## Technologies Used

- **Programming Language:** Python
- **Code Editor:** Visual Studio Code
- **Platform:** Nand2Tetris Online IDE
- **Input Format:** `.asm`
- **Output Format:** `.hack`

## Project Structure

```text
Part_B_Assembler/
│
├── assembler.py
├── verify_hack.py
├── README.md
│
├── test_files/
│   ├── Add.asm
│   ├── Add.hack
│   ├── Max.asm
│   ├── Max.hack
│   ├── Rect.asm
│   ├── Rect.hack
│   ├── Pong.asm
│   └── Pong.hack
│
└── Screenshots/
    ├── 01_Assembler_Code.png
    ├── 02_Add_Comparison.png
    ├── 03_Max_Comparison.png
    ├── 04_Rect_Comparison.png
    ├── 05_Pong_Comparison.png
    ├── 06_Output_Files.png
    └── 07_Verification.png
```

## Features

### 1. Assembly File Processing
- Reads `.asm` files.
- Removes comments and unnecessary whitespace.
- Ignores blank lines.

### 2. A-Instruction Translation
- Converts numeric addresses into 16-bit binary.
- Handles symbolic addresses.
- Supports variable allocation.

### 3. C-Instruction Translation
- Converts computation instructions.
- Handles destination fields.
- Handles jump instructions.
- Generates the correct 16-bit instruction format.

### 4. Symbol Table Management
- Supports predefined symbols such as SP, LCL, ARG, THIS, THAT, SCREEN, and KBD.
- Supports R0–R15 registers.
- Resolves labels.
- Allocates variables starting from RAM address 16.

### 5. Machine Code Generation
- Generates `.hack` output files.
- Produces 16-bit binary instructions.
- Reports assembly errors.

## How to Run the Project

### Step 1: Open the Project

Open the `Part_B_Assembler` folder in Visual Studio Code.

### Step 2: Open Terminal

Navigate to the project directory:

```bash
cd Part_B_Assembler
```

### Step 3: Execute the Assembler

Run the following commands individually:

```bash
python assembler.py test_files/Add.asm

python assembler.py test_files/Max.asm

python assembler.py test_files/Rect.asm

python assembler.py test_files/Pong.asm
```

### Step 4: Verify Machine Code

Run the verification script:

```bash
python verify_hack.py
```

The script checks whether every generated instruction contains exactly 16 binary digits.

## Testing and Results

The assembler was tested using four standard Nand2Tetris assembly programs.

| Test Program | Instructions Generated | Result |
|---|---:|---|
| Add.asm | 6 | PASS |
| Max.asm | 16 | PASS |
| Rect.asm | 25 | PASS |
| Pong.asm | 27,483 | PASS |

All four programs were also compared against the official Nand2Tetris Online IDE assembler.

**Comparison Results:**
- Add.asm – Successful
- Max.asm – Successful
- Rect.asm – Successful
- Pong.asm – Successful

All four comparisons produced matching machine code.

## Learning Outcomes

Through this project, the following concepts were implemented and understood:

- Working principles of an assembler.
- Assembly language and machine-code conversion.
- Binary instruction representation.
- Symbol table implementation.
- Label resolution and variable allocation.
- Python file handling.
- Error handling and debugging.
- Testing and verification of machine code.

## Conclusion

The Nand2Tetris Part B project successfully implements a Python-based Hack Assembler capable of translating Hack Assembly programs into binary machine code.

The implementation was tested using Add, Max, Rect, and Pong programs. All four generated outputs passed the 16-bit binary validation and matched the official Nand2Tetris Online IDE assembler output.

This project provided practical experience in understanding the relationship between assembly language, machine instructions, and computer architecture.

---

**Project:** Nand2Tetris Capstone – Part B  
**Module:** Python Hack Assembler  
**Language:** Python  
**Status:** Completed and Verified