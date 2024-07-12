# to get the img name in ./select_train  or ./select_val
# and select label file from ./Label_normalized with the same name
# and copy them to ./select_train_label or ./select_val_label

import os
import shutil

def get_label():
    Newfoldername = 'select_val_label'
    if not os.path.exists(f'./{Newfoldername}'):
        os.makedirs(f'./{Newfoldername}')
    else:
        shutil.rmtree(f'./{Newfoldername}')
        os.makedirs(f'./{Newfoldername}')   

    original_folder = './select_val'
    img_names = os.listdir(f'./{original_folder}')
    for img_name in img_names:
        img = img_name.split('.')[0]
        shutil.copyfile(f'./Label_normalized/{img}.txt', f'./{Newfoldername}/{img}.txt')
    return

if __name__ == '__main__':
    get_label()
    print('Done!')

