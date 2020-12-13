import sys

class GameConsole:
    def __init__(self):
        self.clear()

    def clear(self):
        self.acc = 0
        self.ip = 0
        self.executed_insts = set()
        self.program = []  # items are (opcode, argument)

    def parse_program(self, lines):
        for line in lines:
            opcode, arg_str = line.split()
            arg = int(arg_str)
            self.program.append((opcode, arg))

    def run(self):
        while self.ip < len(self.program) and self.ip not in self.executed_insts:
            opcode, arg = self.program[self.ip]
            self.executed_insts.add(self.ip)
            if opcode == 'acc':
                self.acc += arg
                self.ip += 1
            elif opcode == 'jmp':
                self.ip += arg
            elif opcode == 'nop':
                self.ip += 1
            else:
                raise RuntimeError(f"Unrecognized opcode {inst[0]} at IP {self.ip}")
        print(f"Output: {self.acc}")

    def run_program(self, program):
        self.parse_program(program)
        self.run()
        self.clear()

def main():
    console = GameConsole()
    console.run_program(sys.stdin)

if __name__ == "__main__":
    main()
