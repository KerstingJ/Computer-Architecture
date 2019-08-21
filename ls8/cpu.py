"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = {}
        for i in range(8):
            self.reg[i] = 0
        self.PC = 0
        self.SP = 0
        self.IR = 0b00000000
        self.MAR = 0b00000000
        self.MDR = 0b00000000
        self.FL = 0b00000000
        self.CMD = {
            0b10100000: self.ADD,
            0b10101000: self.AND,
            0b01010000: self.CALL,
            0b10100111: self.CMP,
            0b01100110: self.DEC,
            0b10100011: self.DIV,
            0b00000001: self.HLT,
            0b01100101: self.INC,
            0b01010010: self.INT,
            0b00010011: self.IRET,
            0b01010101: self.JEQ,
            0b01011010: self.JGE,
            0b01010111: self.JGT,
            0b01011001: self.JLE,
            0b01011000: self.JLT,
            0b01010100: self.JMP,
            0b01010110: self.JNE,
            0b10000011: self.LD,
            0b10000010: self.LDI,
            0b10100100: self.MOD,
            0b10100010: self.MUL,
            0b00000000: self.NOP,
            0b01101001: self.NOT,
            0b10101010: self.OR,
            0b01000110: self.POP,
            0b01001000: self.PRA,
            0b01000111: self.PRN,
            0b01000101: self.PUSH,
            0b00010001: self.RET,
            0b10101100: self.SHL,
            0b10101101: self.SHR,
            0b10000100: self.ST,
            0b10100001: self.SUB,
            0b10101011: self.XOR
        }

    def ram_read(self, address):
        return self.ram[address]

    def ram_write(self, address, value):
        self.ram[address] = value

    def load(self, program):
        """Load a program into memory."""
        address = 0

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def ADD(self):
        pass

    def AND(self):
        pass

    def CALL(self):
        pass

    def CMP(self):
        pass

    def DEC(self):
        pass

    def DIV(self):
        pass

    def HLT(self):
        sys.exit()

    def INC(self):
        pass

    def INT(self):
        pass

    def IRET(self):
        pass

    def JEQ(self):
        pass

    def JGE(self):
        pass

    def JGT(self):
        pass

    def JLE(self):
        pass

    def JLT(self):
        pass

    def JMP(self):
        pass

    def JNE(self):
        pass

    def LD(self):
        pass

    def LDI(self):
        reg = self.ram_read(self.PC + 1)
        self.reg[reg] = self.ram_read(self.PC + 2)
        # store second arg in register
        # print(f"set R{self.ram_read(self.PC + 1)} to {self.ram_read(self.PC + 2)}")
        self.PC += 2

    def MOD(self):
        pass

    def MUL(self):
        # MUL
        # multiple register A by register b
        # store new value in register A
        reg_a = self.reg[self.ram_read(self.PC + 1)]
        reg_b = self.reg[self.ram_read(self.PC + 2)]
        self.reg[self.ram_read(self.PC + 1)] = reg_a * reg_b
        self.PC += 2

    def NOP(self):
        pass

    def NOT(self):
        pass

    def OR(self):
        pass

    def POP(self):
        pass

    def PRA(self):
        pass

    def PRN(self):
        print(self.reg[self.ram_read(self.PC + 1)])
        self.PC += 1

    def PUSH(self):
        pass

    def RET(self):
        pass

    def SHL(self):
        pass

    def SHR(self):
        pass

    def ST(self):
        pass

    def SUB(self):
        pass

    def XOR(self):
        pass

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
        self.PC = 0  # point to beginning of RAM
        self.SP = len(self.ram) - 1  # point to end of RAM

        while True:
            # Get the next Instruction
            self.IR = self.ram_read(self.PC)

            if self.IR in self.CMD.keys():
                command = self.CMD[self.IR]
                command()
            else:
                print(f"could not recognize command: {self.IR}")
                self.trace()

            self.PC += 1
