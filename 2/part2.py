with open('input.txt') as input_file:
    code = input_file.read().replace('\n', '')

program = code.split(',')

def run(input_program):
    position = 0
    op_code = 0
    while op_code != '99':
        op_code = input_program[position]
        if op_code == '1':
            input_program[int(input_program[position + 3])] = int(input_program[int(input_program[position + 1])]) + int(input_program[int(input_program[position + 2])])
        if op_code == '2':
            input_program[int(input_program[position + 3])] = int(input_program[int(input_program[position + 1])]) * int(input_program[int(input_program[position + 2])])
        position += 4
    return input_program[0]

for noun in range(100):
    for verb in range(100):
        test_program = program.copy()
        test_program[1] = noun
        test_program[2] = verb
        result = run(test_program)
        if result == 19690720:
            print(100 * noun + verb)
