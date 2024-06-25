def double_char(str):
    doubled_str = ''
    for char in str:
        doubled_str += char * 2
    return doubled_str

#double_char('AAbb') → 'AAAAbbbb'