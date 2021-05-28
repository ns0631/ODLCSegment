import os, random

total = 0

ignored_files = ''

for dir in ['train', 'test', 'valid']:
    image_path = f'./{dir}/images/'
    text_path = f'./{dir}/labels/'
    files = os.listdir(image_path)
    num = len(files) // 2
    for i in range(num):
        file = random.choice(files)
        files.remove(file)
        ignored_files += image_path + file + '\n'
        ignored_files += text_path + file[:-3] + 'txt\n'
        total += 1

print(total)

h = open('.gitignore', 'w')
h.write(ignored_files[:-1])
h.close()
