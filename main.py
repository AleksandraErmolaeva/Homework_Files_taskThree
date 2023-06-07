

import os


path_to_folder = r"C:\Users\alexa\Desktop\HomeWork\task_three\files"
directory = os.listdir(path_to_folder)

file_list = []
for file in directory:    
    with open(os.path.join(path_to_folder, file), encoding = 'utf-8') as f:
        file_list.append(f.readlines())

id = 0
for list in file_list:
    list.insert(0, len(list))
    list.insert(0, directory[id])
    id += 1
        
file_list.sort(key=lambda x:len(x))
print(file_list)

with open ('result.txt', 'w', encoding = 'utf-8') as result_file:
        for result in file_list:
            result_file.write(str(result[0]) + '\n' + str(result[1]) + '\n' + ''.join(result[2:]) + '\n')

  
       