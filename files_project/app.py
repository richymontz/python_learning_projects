file = open('data.txt', 'r')
file_content = file.read()
file.close()

print(file_content)

name = input('Enter your name: ')
file_writing = open('data.txt', 'w')
file_writing.write(name)

file_writing.close()
