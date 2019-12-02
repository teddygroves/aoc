from typing import List


def operate(loi: List[int], pos=0):
    "Do the main task."
    output = loi
    opcode = loi[pos]
    if opcode == 99:
        return output
    input_pos_one, input_pos_two, result_pos = loi[pos+1], loi[pos+2], loi[pos+3]
    input_one, input_two = loi[input_pos_one], loi[input_pos_two] 
    if opcode == 1:
        result = input_one + input_two 
    elif opcode == 2:
        result = input_one * input_two 
    else:
        raise ValueError("Unknown opcode: " + str(opcode))
    output[result_pos] = result
    new_pos = pos + 4
    return operate(output, new_pos)

def get_data():
    with open('input.txt', 'r') as f:
        return list(map(int, f.read().split(',')))


def process_data(data: List[int], noun: int, verb: int):
    """Once you have a working computer, the first step is to restore the gravity
    assist program (your puzzle input) to the "1202 program alarm" state it had
    just before the last computer caught fire. To do this, before running the
    program, replace position 1 with the value 12 and replace position 2 with
    the value 2.
    """
    out = data.copy()
    out[1] = noun
    out[2] = verb
    return out

def do_task_1():
    data_raw = get_data()
    data = process_data(data_raw, 12, 2)
    output = operate(data)
    print("Answer to task 1: " + str(output[0]))


def do_task_2():
    data_raw = get_data()
    for noun in range(100):
        for verb in range(100):
            data = process_data(data_raw, noun, verb)
            output = operate(data)
            if output[0] == 19690720:
                print("Noun: " + str(noun))
                print("Verb: " + str(verb))
                print("Answer to task 1: " + str(100 * noun + verb))

if __name__ == '__main__':
    do_task_1()
    do_task_2()
    

