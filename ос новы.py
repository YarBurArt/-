import os


#os.rename('D:/to.txt', 'D:/text.txt')

#ni = os.getpid() = id gpu
my_file = open("D:/text.txt","r") # w - запись , a - добавление, r - чтение
my_string = my_file.read()
#ni = os.name
#os.mkdir("folder") = new folder
#text_file = open("text.txt", "w") = new file and open file
#open("text.png", "w")
#os.remove("text.png")  = delete file
#my_file.write("hi") - запись в файл
print("Было прочитано:")
print(my_string)
print(os.stat("text.txt")) #file info
#size - размер, atime - последний доступ, mtime - последние изменение, ctime - время создания
#print(ni)
print("Размер файла:", os.stat("D:/text.txt").st_size)
my_file.close()









