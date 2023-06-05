#!/src/anaconda3/bin/python

import os
import shutil


def auto_categorize(path, categories):
    for file_ in os.listdir(path):
        # Checking the extension
        extension = '.' + file_.split('.')[-1]

        # I only want files, not folders
        if '.' not in file_ or os.path.isdir(path + '/' + file_):  
            #print((file_, 'folder'))
            continue

        has_category = False
        # Looping through the categories
        for k, v in categories.items():
            if has_category:
                break
            if extension in v:
                cat_found(path, file_, k)
                has_category = True

        if not has_category:
            cat_not_found(path, file_)
        


def cat_not_found(path, file_):
    source = path + '/' + file_
    destination = path + '/' + 'others'
    if not os.path.exists(path + '/' + 'others'):
        os.mkdir(path + '/' + 'others')
    return shutil.move(source, destination)

def cat_found(path, file_, key):
    source = path + '/' + file_
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
        'docs':['.doc','.docx','.xlsx','.xls','.txt','.pptx','odt']}

#print(cats.values())
test_path = "C:\\Users\\matte\\Downloads\\aaa" if os.name == 'nt' else '/home/devilteo911/Downloads/aaa'

def main(*args):
    auto_categorize(test_path, cats)

# Infinite loop to keep alive the service
if __name__ == '__main__':
    while True:
        main()
