
import sys
import re
from pathlib import Path


# ==========================================
# 1. PREDEFINED SYMBOL TABLE
# ==========================================

PREDEFINED_SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576
}

for i in range(16):
    PREDEFINED_SYMBOLS[f"R{i}"] = i


# ==========================================
# 2. COMPUTATION TABLE
# ==========================================

COMP_TABLE = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "M": "1110000",
    "!D": "0001101",
    "!A": "0110001",
    "!M": "1110001",
    "-D": "0001111",
    "-A": "0110011",
    "-M": "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}


# ==========================================
# 3. JUMP TABLE
# ==========================================

JUMP_TABLE = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}


# ==========================================
# 4. DESTINATION TABLE
# ==========================================

DEST_BITS = {
    "A": "100",
    "D": "010",
    "M": "001"
}


# ==========================================
# 5. CLEAN ASSEMBLY FILE
# ==========================================

def clean_lines(filename):

    instructions = []

    with open(filename, "r") as file:

        for line_number, line in enumerate(file, start=1):

            line = line.split("//")[0]
            line = line.strip()
            line = line.replace(" ", "")
            line = line.replace("\t", "")

            if line:
                instructions.append((line, line_number))

    return instructions


# ==========================================
# 6. FIRST PASS - HANDLE LABELS
# ==========================================

def first_pass(instructions):

    symbols = PREDEFINED_SYMBOLS.copy()
    rom_address = 0

    for instruction, line_number in instructions:

        if instruction.startswith("(") and instruction.endswith(")"):

            label = instruction[1:-1]

            if not re.fullmatch(r"[A-Za-z_.$:][A-Za-z0-9_.$:]*", label):
                raise ValueError(
                    f"Invalid label at line {line_number}: {label}"
                )

            if label in symbols:
                raise ValueError(
                    f"Duplicate or reserved label at line {line_number}: {label}"
                )

            symbols[label] = rom_address

        else:

            if instruction.startswith("(") or instruction.endswith(")"):
                raise ValueError(
                    f"Invalid label syntax at line {line_number}"
                )

            rom_address += 1

    return symbols


# ==========================================
# 7. TRANSLATE A-INSTRUCTION
# ==========================================

def translate_a_instruction(instruction, symbols, next_variable):

    symbol = instruction[1:]

    if not symbol:
        raise ValueError("Empty A-instruction")

    if symbol.isdigit():

        address = int(symbol)

    else:

        if not re.fullmatch(r"[A-Za-z_.$:][A-Za-z0-9_.$:]*", symbol):
            raise ValueError(f"Invalid symbol: {symbol}")

        if symbol not in symbols:

            symbols[symbol] = next_variable[0]
            next_variable[0] += 1

        address = symbols[symbol]

    if address < 0 or address > 32767:
        raise ValueError(f"Address out of range: {address}")

    return format(address, "016b")


# ==========================================
# 8. TRANSLATE C-INSTRUCTION
# ==========================================

def translate_c_instruction(instruction):

    dest = "000"
    jump = "000"

    # Separate destination
    if "=" in instruction:

        if instruction.count("=") != 1:
            raise ValueError(f"Invalid destination: {instruction}")

        dest_part, instruction = instruction.split("=")

        if not dest_part or any(c not in DEST_BITS for c in dest_part):
            raise ValueError(f"Invalid destination: {dest_part}")

        if len(set(dest_part)) != len(dest_part):
            raise ValueError(f"Repeated destination: {dest_part}")

        dest_value = 0

        for register in dest_part:
            dest_value |= int(DEST_BITS[register], 2)

        dest = format(dest_value, "03b")

    # Separate jump
    if ";" in instruction:

        if instruction.count(";") != 1:
            raise ValueError(f"Invalid jump: {instruction}")

        instruction, jump_part = instruction.split(";")

        if jump_part not in JUMP_TABLE or not instruction:
            raise ValueError(f"Invalid jump instruction: {jump_part}")

        jump = JUMP_TABLE[jump_part]

    # Translate computation
    if instruction not in COMP_TABLE:
        raise ValueError(f"Invalid computation: {instruction}")

    comp = COMP_TABLE[instruction]

    return "111" + comp + dest + jump


# ==========================================
# 9. SECOND PASS - GENERATE MACHINE CODE
# ==========================================

def second_pass(instructions, symbols):

    machine_code = []
    next_variable = [16]

    for instruction, line_number in instructions:

        try:

            if instruction.startswith("("):
                continue

            elif instruction.startswith("@"):

                binary = translate_a_instruction(
                    instruction, symbols, next_variable
                )

            else:

                binary = translate_c_instruction(instruction)

            machine_code.append(binary)

        except (ValueError, KeyError) as error:

            raise ValueError(
                f"Error at assembly line {line_number}: {error}"
            ) from error

    return machine_code


# ==========================================
# 10. MAIN ASSEMBLER FUNCTION
# ==========================================

def assemble(input_file):

    input_path = Path(input_file)

    if not input_path.exists():
        raise FileNotFoundError(
            f"Assembly file not found: {input_path}"
        )

    if input_path.suffix.lower() != ".asm":
        raise ValueError("Input file must have .asm extension")

    print("\nStarting Hack Assembler...")
    print("Input:", input_path)

    # Read and clean file
    instructions = clean_lines(input_path)

    # First pass
    symbols = first_pass(instructions)

    print("First pass completed.")

    # Second pass
    machine_code = second_pass(instructions, symbols)

    print("Second pass completed.")

    # Generate output file
    output_file = input_path.with_suffix(".hack")

    with open(output_file, "w") as file:

        file.write("\n".join(machine_code))

        if machine_code:
            file.write("\n")

    print("\nAssembly successful!")
    print("Total instructions:", len(machine_code))
    print("Output file:", output_file)


# ==========================================
# 11. PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: python assembler.py filename.asm")

    else:

        try:

            assemble(sys.argv[1])

        except Exception as error:

            print("\nASSEMBLER ERROR:")
            print(error)
            sys.exit(1)
