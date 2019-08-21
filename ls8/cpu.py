"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = {}
        for i in range(8):
            self.reg[f"R{i}"] = 0
        self.PC = 0
        self.IR = "00000000"
        self.MAR = "00000000"
        self.MDR = "00000000"
        self.FL = "00000000"
        self.INS = {
            "ADD": "10100000",
            "AND": "10101000",
            "CALL": "01010000",
            "CMP": "10100111",
            "DEC": "01100110",
            "DIV": "10100011",
            "HLT": "00000001",
            "INC": "01100101",
            "INT": "01010010",
            "IRET": "00010011",
            "JEQ": "01010101",
            "JGE": "01011010",
            "JGT": "01010111",
            "JLE": "01011001",
            "JLT": "01011000",
            "JMP": "01010100",
            "JNE": "01010110",
            "LD": "10000011",
            "LDI": "10000010",
            "MOD": "10100100",
            "MUL": "10100010",
            "NOP": "00000000",
            "NOT": "01101001",
            "OR": "10101010",
            "POP": "01000110",
            "PRA": "01001000",
            "PRN": "01000111",
            "PUSH": "01000101",
            "RET": "00010001",
            "SHL": "10101100",
            "SHR": "10101101",
            "ST": "10000100",
            "SUB": "10100001",
            "XOR": "10101011",
        }

    def ram_read(self, address):

        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def load(self, program):
        """Load a program into memory."""

        address = 0

        # # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     "10000010",  # LDI R0,8
        #     "00000000",
        #     "00001000",
        #     "01000111",  # PRN R0
        #     "00000000",
        #     "00000001",  # HLT
        # ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.PC,
            # self.fl,
            # self.ie,
            self.ram_read(self.PC),
            self.ram_read(self.PC + 1),
            self.ram_read(self.PC + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while True:
            # Get the next Instruction
            self.IR = self.ram_read(self.PC)

            if self.IR == self.INS["HLT"]:
                # HLT
                break
            elif self.IR == self.INS["LDI"]:
                # LDI
                # use 1st arg to grab register
                reg = int(self.ram_read(self.PC + 1), 2)
                self.reg[f"R{reg}"] = self.ram_read(self.PC + 2)
                # store second arg in register
                print(
                    f"set R{self.ram_read(self.PC + 1)} to {self.ram_read(self.PC + 2)}")
                self.PC += 2
            elif self.IR == self.INS["PRN"]:
                # PRN
                # print the value in the first argument
                print(self.reg[f"R{int(self.ram_read(self.PC + 1), 2)}"])
                self.PC += 1
            elif self.IR == self.INS["MUL"]:
                # MUL
                # multiple register A by register b
                # store new value in register A
                reg_a = self.reg[f"R{int(self.ram_read(self.PC + 1), 2)}"]
                reg_b = self.reg[f"R{int(self.ram_read(self.PC + 2), 2)}"]
                self.reg[f"R{int(self.ram_read(self.PC + 1), 2)}"] = \
                    int(reg_a, 2) * int(reg_b, 2)
                self.PC += 2
            else:
                print(f"could not recognize command: {self.IR}")

            self.PC += 1
