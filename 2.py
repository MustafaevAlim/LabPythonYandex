alphabet = ' 0123456789' # Рабочий алфавит

print('00, ,<,01')
state_counter = 1
for i in alphabet[1:]:
    print(f'{state_counter},{i},<,{state_counter}')
print(f'{state_counter}, ,>,{state_counter}')
state_counter += 1
copy_state = state_counter
shift_state = state_counter + 1
state_counter += 2

for i in alphabet[1:]:
    print(f'{copy_state},{i}, ,{state_counter}')
    print(f'{state_counter},{i}, ,{state_counter + 1}')
    state_counter += 1
    for j in alphabet[1:]:
        print(f'{state_counter}, {i},>,{state_counter}')
    print(f'{state_counter}, ,{i},{state_counter + 1}')
    state_counter += 1
    for j in alphabet[1:]:
        print(f'{state_counter}, {i},<,{state_counter}')
    print(f'{state_counter}, , ,{state_counter + 1}')
    state_counter += 1
    for j in alphabet[1:]:
        print(f'{state_counter}, {i},<,{state_counter}')
    print(f'{state_counter}, ,{i},{state_counter + 1}')

state_counter += 1
print(f'{copy_state},{i},>,{state_counter}')

for i in alphabet[1:]:
    print(f'{shift_state},{i},>,{copy_state}')

