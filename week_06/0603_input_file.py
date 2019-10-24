# Чтение до конца ввода
'''
В принципе, читать до конца ввода можно и из консоли.
Для этого нужно подключить библиотеку sys и использовать определенный в ней
файловый дескриптор stdin в качестве файла (например, для перебора строк
консоли можно написать for line in sys.stdin). Ввести признак конца файла в
консоли можно, нажав Ctrl+Z в Windows или Ctrl+D в Unix-системах.
В среде программирования такой способ может не работать.
Более подробно в этой теме: https://www.coursera.org/learn/python-osnovy-programmirovaniya/discussions/all/threads/DLrJXKbWEeiD2QqOJunOiA/replies/fJUPEK4gEeix7A7XXq2u1g.

Еще об одном способе работы с файлами с помощью конструкции with .. as ..,
что позволяет автоматически вызывать метод close(), можно почитать здесь:
http://book.pythontips.com/en/latest/open_function.html.
'''

inFile = open('input_01.txt', 'r', encoding='utf8')
outFile = open('output_01.txt', 'w', encoding='utf8')
'''
a = int(inFile.readline())
b = int(inFile.readline())
print(a + b)
'''
'''
lines = inFile.readlines()
print(lines)
'''
s = inFile.read()
print(s)


'''
for line in lines:
    print(line[-2::-1], file=outFile)
inFile.close()
outFile.close()

'''