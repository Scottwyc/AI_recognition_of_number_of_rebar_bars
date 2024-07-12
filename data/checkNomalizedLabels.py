# check nomalized labels

import os
import shutil
import cv2

def checkNomalizedLabels():
   
    label_files = os.listdir('./Label_normalized_center')

    for label_file in label_files:
        # check those labels for each image are correctly normalized
        img_Name = label_file.split('.')[0]

        img = cv2.imread(f'./train640/{img_Name}.jpg')

        # visualize the image
        cv2.imshow('image', img)

        with open(f'./Label_normalized/{label_file}', 'r') as f:

            lines = f.readlines()
            for line in lines:
                pos = line.split(' ')[1:]

                for p in pos:
                    if float(p) < 0 or float(p) > 1:
                        print('Error! The label file is not nomalized!')
                        print('Label file:', label_file)
                        print('Line:', line)


                # get x1, y1, x2, y2 from xc, yc, w, h
                xc = float(pos[0])
                yc = float(pos[1])
                w = float(pos[2])
                h = float(pos[3])

                x1 = int((xc - w / 2) * 640)
                y1 = int((yc - h / 2) * 640)
                x2 = int((xc + w / 2) * 640)
                y2 = int((yc + h / 2) * 640)

                # x1 = int(float(pos[0]) * 640)
                # y1 = int(float(pos[1]) * 640)
                # x2 = int(float(pos[2]) * 640)
                # y2 = int(float(pos[3]) * 640)
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()        


if __name__ == '__main__':
    checkNomalizedLabels()
    print('Done!')
