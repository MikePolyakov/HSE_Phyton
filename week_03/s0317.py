# Удаление символа
'''
Дана строка. Удалите из этой строки все символы @.
'''
s = input()
s_new = ''
while s.find('@') != -1:
    s_new = s_new + s[0:s.find('@')]
    s = s[(s.find('@') + 1):(len(s) + 1)]
s_new = s_new + s
print(s_new)
