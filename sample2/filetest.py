
from datetime import datetime


# 写文件
with open("../test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！\n")
    out_file.write('今天是 ')
    out_file.write(datetime.now().strftime('%Y-%m-%d'))
 
# Read a file
with open("../test.txt", "rt") as in_file:
    text = in_file.read()
 
print(text)