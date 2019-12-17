with open('input.txt') as input_file:
    code = input_file.read().replace('\n', '')

program = code.split(',')
position = 0
op_code = 0

while op_code != '99':
    op_code = program[position]
    if op_code == '1':
        program[int(program[position + 3])] = int(program[int(program[position + 1])]) + int(program[int(program[position + 2])])
    if op_code == '2':
        program[int(program[position + 3])] = int(program[int(program[position + 1])]) * int(program[int(program[position + 2])])
    position += 4

print(program[0])
