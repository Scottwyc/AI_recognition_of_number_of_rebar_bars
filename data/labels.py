
# to transform position information to label information
# read in the position information from train_labels.csv
# and output into txt file
# same ID for one txt file

import numpy as np
import pandas as pd
import os
import shutil

def get_labels():
    # Read in the position information
    labels = pd.read_csv('train_labels.csv')

    Newfoldername = 'Label_normalized_center'

    # Create a new folder to store the txt files (overwriting existing files or creating new ones)
    if not os.path.exists(f'./{Newfoldername}'):
        os.makedirs(f'./{Newfoldername}')
    else:
        shutil.rmtree(f'./{Newfoldername}')
        os.makedirs(f'./{Newfoldername}')
    
    # Group by 'ID' to handle items with the same ID
    grouped_labels = labels.groupby('ID')
    
    # Traverse all the groups
    for id, group in grouped_labels:

        # filter 2 ID, they are rotated
        if id == '13641B22.jpg' or id == 'AEF131E0.jpg':
            continue

        img = id.split('.')[0]
        # Create a new txt file for each ID
        with open(f'./{Newfoldername}/{img}.txt', 'w') as f:  # Use 'w' to overwrite existing files or create new
            for _, row in group.iterrows():
                # print(row)
                # print(row['Detection'])
                f.write('0 ')  # it is the index of the class

                # transform the position to normalized position
                # original size:2666*2000 
                # position into [0,1] 
                x1,y1,x2,y2 = row['Detection'].split(' ')
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)

                if  y1 > 2000 or y2 > 2000:
                    print('Error! The position is out of range!')
                    print('ID:', id)                    
                    print(x1,y1,x2,y2)

                    # swap x and y
                    temp = x1
                    x1 = y1
                    y1 = temp
                    temp = x2
                    x2 = y2
                    y2 = temp

                    print("After swap:")
                    print(x1,y1,x2,y2)

                x1 = x1 / 2666.0
                y1 = y1 / 2000.0
                x2 = x2 / 2666.0
                y2 = y2 / 2000.0      

                # get center and width and height
                x_center = (x1 + x2) / 2
                y_center = (y1 + y2) / 2
                width = x2 - x1
                height = y2 - y1

                f.write(str(x_center) + ' '+ str(y_center) + ' '+ str(width) + ' '+ str(height) + '\n')
                    
                # f.write(str(x1) + ' '+ str(y1) + ' '+ str(x2) + ' '+ str(y2) + '\n')
    return

                


if __name__ == '__main__':
    get_labels()
    print('Done!')


