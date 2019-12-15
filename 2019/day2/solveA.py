import sys



def run_program(program, noun, verb):
    memory = program.copy()
    memory[1] = noun
    memory[2] = verb
    pc = 0

    while True:
        opcode = memory[pc]
        if opcode == 99:
            break
        ptr1 = memory[pc+1]
        ptr2 = memory[pc+2]
        dst = memory[pc+3]

        if opcode == 1:
            memory[dst] = memory[ptr1] + memory[ptr2]
        elif opcode == 2:
            memory[dst] = memory[ptr1] * memory[ptr2]
        else:
            raise ValueError("Unexpected opcode: " + str(opcode))

        pc += 4

    return memory[0]


    

def main():
    memory = [int(x) for x in "".join(sys.stdin.readlines()).split(",")]
    print(run_program(memory, 12, 2))





if __name__ == '__main__':
    main()
