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

    def fix_and_run(self, lines):
        self.parse_program(lines)
        original_program = self.program.copy()

        for i in range(len(self.program)):
            self.program = original_program.copy()
            opcode, arg = self.program[i]
            if opcode == 'jmp':
                self.program[i] = ('nop', self.program[i][1])
            elif opcode == 'nop':
                self.program[i] = ('jmp', self.program[i][1])
            else:
                continue
            ret = self.run()
            if ret[0] == 0:
                print(f"Output: {ret[1]}")
                break
            self.clear()

    def run(self):
        while True:
            if self.ip == len(self.program): # problem says "immediately" after the end
                return (0, self.acc)
            if self.ip in self.executed_insts:
                return (-1, self.acc)
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

    def run_program(self, program):
        self.parse_program(program)
        ret = self.run()
        self.clear()
        return ret

def main():
    console = GameConsole()
    console.fix_and_run(sys.stdin)

if __name__ == "__main__":
    main()
