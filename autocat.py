#!/src/anaconda3/bin/python

import os
import shutil
import time


def auto_categorize(path, categories):
    for file in os.listdir(path):
        # Useful for "unknown" ext
        cnt = 0
        # Checking the extension
        extension = '.' + file.split('.')[-1]

        # I only want files, not folders
        if '.' not in file or os.path.isdir(path + '/' + file) != False:  
            #print((file, 'folder'))
            continue

        # Looping through the categories
        for i in range(len(categories.keys())):
            # Taking the current key and value
            key = list(categories.keys())[i]
            value = list(categories.values())[i]
            #print(key, value, extension)

            # If none of the cat suits us --> others folder
            if cnt == len(categories.keys())-1:
                print((time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),extension, list(categories.keys())[-1]))
                try:
                    cat_not_found(path, file)
                except shutil.Error:
                    continue
                break
            cnt += 1
            # If we match the cat
            if extension in value:
                print((time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),extension, key))
                try:
                    cat_found(path, file, key)
                except shutil.Error:
                    continue
                break


def cat_not_found(path, file):
    source = path + '/' + file
    destination = path + '/' + 'others'
    if not os.path.exists(path + '/' + 'others'):
        os.mkdir(path + '/' + 'others')
    return shutil.move(source, destination)

def cat_found(path, file, key):
    source = path + '/' + file
    destination = path + '/' + key
    # Create the folder if not present
    if not os.path.exists(path + '/' + key):
        os.mkdir(path + '/' + key)
    # Move the file to the respective cat folder
    return shutil.move(source, destination)


cats = {'scripts':['.py', '.ipy', '.ipynb', '.java','.json'], 
        'pdfs':['.pdf'], 
        'executables':['.exe', '.msi','.sh','.jar','.AppImage','.deb','.bat'], 
        'photos':['.jpg', '.jpeg','.gif','.png','.raw'], 
        'videos':['.mp4', '.avi','.mpeg'], 
        'archives':['.zip', '.tar','.tar.bz2','.tar.gz','.rar','.7z','.gz','.tgz'],
        'music':['.mp3','.flac','.wav'],
        'docs':['.doc','.docx','.xlsx','.xls','.txt','.pptx','odt'],
        'others':[]}

#print(cats.values())
test_path = "C:\\Users\\Matteo\\Downloads" if os.name == 'nt' else '/home/devilteo911/Downloads'
#print(auto_categorize(test_path, cats))

# Infinite loop to keep alive the service
if __name__ == '__main__':
    while True:
        auto_categorize(test_path, cats)
