def modern_print(string):
    if string not in used_lines:
        print(string)
    used_lines.add(string)


used_lines = set()

