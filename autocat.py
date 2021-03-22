#!/src/anaconda3/bin/python

import os
import shutil


def auto_categorize(path, categories):
    in_path_files = os.listdir(path)
    for file in in_path_files:
        # I only want files, not folders
        if '.' in file and os.path.isdir(path + '/' + file) == False:
            # Checking the extension
            extension = '.' + file.split('.')[-1]
            # Useful for "unknown" ext
            cnt = 0
            # Looping through the categories
            for i in range(0, len(categories.keys())):
                # Taking the current key and value
                key = list(categories.keys())[i]
                value = list(categories.values())[i]
                #print(key, value, extension)

                # If none of the cat suits us --> others folder
                if cnt == len(categories.keys())-1:
                    print((extension, list(categories.keys())[-1]))
                    source = path + '/' + file
                    destination = path + '/' + 'others'
                    if not os.path.exists(path + '/' + 'others'):
                        os.mkdir(path + '/' + 'others')
                    try:
                        move = shutil.move(source, destination)
                    except shutil.Error:
                        continue
                    break
                cnt += 1
                # If we match the cat
                if extension in value:
                    print((extension, key))
                    source = path + '/' + file
                    destination = path + '/' + key
                    # Create the folder if not present
                    if not os.path.exists(path + '/' + key):
                        os.mkdir(path + '/' + key)
                    # Move the file to the respective cat folder
                    try:
                        move = shutil.move(source, destination)
                    except shutil.Error:
                        continue
                    break
                
        else:  
            #print((file, 'folder'))
            continue
    


cats = {'scripts':['.py', '.ipy', '.ipynb', '.java'], 
        'pdfs':['.pdf'], 
        'executables':['.exe', '.msi','.sh','.jar','.AppImage','.deb'], 
        'photos':['.jpg', '.jpeg','.gif','.png','.raw'], 
        'videos':['.mp4', '.avi','.mpeg'], 
        'archives':['.zip', '.tar','.tar.bz2','.tar.gz','.rar','.7z'],
        'music':['.mp3','.flac','.wav'],
        'docs':['.doc','.docx','.xlsx','.xls','.txt','.pptx','odt'],
        'others':[]}

#print(cats.values())
test_path = '/home/devilteo911/Downloads'
#print(auto_categorize(test_path, cats))

# Infinite loop to keep alive the service
while True:
    auto_categorize(test_path, cats)
