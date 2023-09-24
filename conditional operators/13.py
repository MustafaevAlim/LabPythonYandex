elf = int(input())
dwarf = int(input())
human = int(input())

if elf % 10 == dwarf % 10 == human % 10:
    print(elf % 10)
elif elf // 10 == dwarf // 10 == human // 10:
    print(elf // 10)
    