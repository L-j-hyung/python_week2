with open('output.txt','w')as file:
    file.write('hello world')
    file.wrire("This is an output file.\n")

with open('output.txt','a')as file:
    file.write("appending this file.\n")
