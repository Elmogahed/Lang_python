import fileinput
# file = open('file.txt', 'x',encoding='utf-8')
# file = open('file.txt', 'r',encoding='utf-8')

file = open(r"D:\Ahmed\Hsoub\دورة الذكاء الاصطناعي\1_أساسيات بايثون\4_التعامل مع الملفات النصية\file.txt", 'w')
file.write("Hello this text is written by Python\n")
file.write("Python is a greet Programming langauge\n")
file.close()

with open('file.txt', 'a') as f: 
    f.write('This is new line')

with open('file.txt', 'r') as file:
    # print(file.read()) 
    # print(file.read(40)) 
    # print(file.readline()) 
    # print(file.readline()) 
    # print(file.readline(14)) 
    # for line in file: 
    #     print(line, end='')
    print(file.readlines())
    

with open('file.txt', 'r') as reader, open('file2.txt', 'w') as writer: 
    read_lines = reader.read()
    writer.write(read_lines)

with fileinput.input(files=('file.txt', 'file2.txt')) as files: 
    index = 1
    for line in files: 
        if fileinput.isfirstline(): 
            print(f'\n--- Reading {fileinput.filename()} -----')
            index = 1
        print(f'{index} - {line}', end='')
        index += 1
