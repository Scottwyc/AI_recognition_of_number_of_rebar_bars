import cv2
import os
 
 
def txtShow(img,txt,save=True):
    image = cv2.imread(img)
    height,width = image.shape[:2]      # 获取原始图像的高和宽
 
    # 读取classes类别信息
    # with open('./my_yolo_dataset/my_data_label.txt','r') as f:
    #     classes = f.read().splitlines()
    # ['Leconte', 'Boerner', 'linnaeus', 'armandi', 'coleoptera', 'acuminatus', 'Linnaeus']

    classes = ['bar']
 
    # 读取yolo格式标注的txt信息
    with open(txt,'r') as f:
        labels = f.read().splitlines()
    # ['0 0.403646 0.485491 0.103423 0.110863', '1 0.658482 0.425595 0.09375 0.099702', '2 0.482515 0.603795 0.061756 0.045387', '3 0.594122 0.610863 0.063244 0.052083', '4 0.496652 0.387649 0.064732 0.049107']


    for i in labels:
        cl, x_centre, y_centre, w, h = i.split(' ')  
 
        # 需要将数据类型转换成数字型
        cl, x_centre, y_centre, w, h = int(cl), float(x_centre), float(y_centre), float(w),float(h)
        name = classes[cl]      # 根据classes文件获取真实目标
        xmin = x_centre - w/2
        ymin = y_centre - h/2
        xmax = x_centre + w/2
        ymax = y_centre + h/2

        # cl, xmin, ymin, xmax, ymax =  i.split(' ')
        # cl, xmin, ymin, xmax, ymax = int(cl), float(xmin), float(ymin), float(xmax),float(ymax)
        # name = classes[int(cl)]      # class name

        cv2.rectangle(image, (int(xmin*width), int(ymin*height)), (int(xmax*width), int(ymax*height)), color=(255, 0, 0), thickness=1)  # 绘制矩形框
        cv2.putText(image, name, (int(xmin*width), int(ymin*height) - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.3, thickness=1, color=(0, 0, 255))

 
    # 保存图像
    if save:
        cv2.imwrite('result.png', image)
 
    # 展示图像
    cv2.imshow('test', image)
    cv2.waitKey()
    cv2.destroyAllWindows()
 
 
if __name__=='__main__':

    courrent_path = os.getcwd()
    pathbase = os.path.abspath(os.path.join(courrent_path, "./own_data/images/train208"))

    for file in os.listdir('./own_data/images/train208'):
        print(file)
        img_path = os.path.join(pathbase, file)     # 传入图片
        print(img_path)
    
        label_path = img_path.replace('images','labels')
        label_path = label_path.replace('.jpg','.txt')  
        print(label_path)     
    
        txtShow(img=img_path,txt=label_path,save=False)