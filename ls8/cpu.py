"""CPU functionality."""

import sys

DEBUGGING = False

# so I don't have to comment and uncomment prints


def debug(message):
    if DEBUGGING:
        print(message)


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = {}
        for i in range(8):
            self.reg[i] = 0
        self.PC = 0
        self.SP = 7
        self.RH = 0
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

        self.RH = address

    def ADD(self):
        debug(f"ADD R{self.ram_read(self.PC+1)}, R{self.ram_read(self.PC+2)}")

        self.reg[self.ram_read(
            self.PC+1)] = self.reg[self.ram_read(self.PC+1)] + self.reg[self.ram_read(self.PC+2)]
        self.PC += 3
        pass

    def AND(self):
        debug("calling ADD")
        self.PC += 1
        pass

    def CALL(self):
        debug(f"CALL R{self.ram_read(self.PC + 1)}")
        """
        Call a subroutine from an address stored in register
        address of the next instruction is pushed onto the stack
        set pc to address stored in given register
        jump to that location and run the first command
        then move pc to loc popped from stack 

        CALL r0

        """

        # push PC+2 onto the stack to retrieve later
        self.reg[self.SP] -= 1
        self.ram_write(self.reg[self.SP], self.PC + 2)
        # debug(f"pushed {self.PC + 2} to stack")

        # get subroutine from given register
        self.PC = self.reg[self.ram_read(self.PC + 1)]

        pass

    def CMP(self):
        debug("calling CMP")
        self.PC += 1
        pass

    def DEC(self):
        debug("calling DEC")
        self.PC += 1
        pass

    def DIV(self):
        debug("calling DIV")
        self.PC += 1
        pass

    def HLT(self):
        debug("calling HLT")
        self.PC += 1
        sys.exit()

    def INC(self):
        debug("calling INC")
        self.PC += 1
        pass

    def INT(self):
        debug("calling INT")
        self.PC += 1
        pass

    def IRET(self):
        debug("calling IRET")
        self.PC += 1
        pass

    def JEQ(self):
        debug("calling JEQ")
        self.PC += 1
        pass

    def JGE(self):
        debug("calling JGE")
        self.PC += 1
        pass

    def JGT(self):
        debug("calling JGT")
        self.PC += 1
        pass

    def JLE(self):
        debug("calling JLE")
        self.PC += 1
        pass

    def JLT(self):
        debug("calling JLT")
        self.PC += 1
        pass

    def JMP(self):
        debug("calling JMP")
        self.PC += 1
        pass

    def JNE(self):
        debug("calling JNE")
        self.PC += 1
        pass

    def LD(self):
        debug("calling LD")
        self.PC += 1
        pass

    def LDI(self):
        debug(f"LDI R{self.ram_read(self.PC + 1)}, {self.ram_read(self.PC + 2)}")
        reg = self.ram_read(self.PC + 1)
        self.reg[reg] = self.ram_read(self.PC + 2)
        self.PC += 3

    def MOD(self):
        debug("calling MOD")
        self.PC += 1
        pass

    def MUL(self):
        debug(
            f"MUL R{self.ram_read(self.PC + 1)}, R{self.ram_read(self.PC + 2)}")
        # MUL
        # multiple register A by register b
        # store new value in register A
        reg_a = self.reg[self.ram_read(self.PC + 1)]
        reg_b = self.reg[self.ram_read(self.PC + 2)]
        self.reg[self.ram_read(self.PC + 1)] = reg_a * reg_b
        self.PC += 3

    def NOP(self):
        debug("calling NOP")
        self.PC += 1
        pass

    def NOT(self):
        debug("calling NOT")
        self.PC += 1
        pass

    def OR(self):
        debug("calling OR")
        self.PC += 1
        pass

    def POP(self):
        debug(f"POP R{self.ram_read(self.PC + 1)}")
        # get register id from ram
        reg = self.ram_read(self.PC + 1)
        # set registers value to last value on stack
        self.reg[reg] = self.ram_read(self.reg[self.SP])
        # increment stack
        self.reg[self.SP] += 1
        # increment PC to pass memory spaces ready by program
        self.PC += 2

    def PRA(self):
        debug("calling PRA")
        self.PC += 1
        pass

    def PRN(self):
        debug("calling PRN")
        debug(f"printing register {self.ram_read(self.PC + 1)}")
        print(self.reg[self.ram_read(self.PC + 1)])
        self.PC += 2

    def PUSH(self):
        debug("calling PUSH")
        # decrement stack pointer by 1
        self.reg[self.SP] -= 1

        # check that stack is not overflowing into heap
        if self.reg[self.SP] == self.PC:
            print("Stack Overflow")
            self.trace()
            sys.exit(1)

        # set register to next value in ram
        reg = self.ram_read(self.PC + 1)
        # write to address of SP value of reg
        self.ram_write(self.reg[self.SP], self.reg[reg])

        self.PC += 2

    def RET(self):
        debug("calling RET")
        # set PC to location popped from stack
        self.PC = self.ram_read(self.reg[self.SP])
        self.reg[self.SP] += 1

    def SHL(self):
        debug("calling SHL")
        self.PC += 1
        pass

    def SHR(self):
        debug("calling SHR")
        self.PC += 1
        pass

    def ST(self):
        debug("calling ST")
        self.PC += 1
        pass

    def SUB(self):
        debug("calling SUB")
        self.PC += 1
        pass

    def XOR(self):
        debug("calling XOR")
        self.PC += 1
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
        sys.exit(1)

    def run(self):
        debug("calling run")
        """Run the CPU."""
        self.PC = 0  # point to beginning of RAM
        self.reg[self.SP] = -1  # point to end of RAM

        while True:
            # Get the next Instruction
            self.IR = self.ram_read(self.PC)

            if self.IR in self.CMD.keys():
                self.CMD[self.IR]()
            else:
                print(f"could not recognize command: {self.IR}")
                self.trace()
