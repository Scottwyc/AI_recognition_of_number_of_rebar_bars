import os
import cv2

def file_iter(path, old_name, new_name):
    for fname in os.listdir(path):
        file_path = os.path.join(path, fname)
        if os.path.isfile(file_path):
            img = cv2.imread(file_path)
            img_scale = cv2.resize(img, (640, 640))
            save_path = file_path.replace(old_name, new_name)
            cv2.imwrite(save_path, img_scale)


if __name__ == '__main__':
    os.makedirs('./train640', exist_ok=True)
    os.makedirs('./test640', exist_ok=True)

    file_iter('./train_dataset', 'train_dataset', 'train640')
    file_iter('./test_dataset', 'test_dataset', 'test640')

