def intcode_interpreter(memory):
    memory[1] = 12
    memory[2] = 2
    pc = 0
    while memory[pc] != 99:
        op = memory[pc]
        a = memory[memory[pc + 1]]
        b = memory[memory[pc + 2]]
        c = memory[pc + 3]
        if op == 1:
            memory[c] = a + b
        elif op == 2:
            memory[c] = a * b
        else:
            print("Error: unknown opcode")
            return
        pc += 4
    return memory[0]

with open("input", "r") as f:
    memory = list(map(int, f.read().strip().split(",")))

print(intcode_interpreter(memory))

