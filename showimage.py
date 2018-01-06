import cv2
import os,sys
import xml.etree.ElementTree as ET
import numpy as np
def show_image_index(file_index,box):

    path='/home/wty/PyTestCode'
    im_file=os.path.join(path,file_index+'.png')
    print(im_file)
    #read image
    img=cv2.imread(im_file)
    cv2.namedWindow("image")

    kind=box['gt_classes']
    for i in range(0,len(box['boxes'])):

        #kind=line.split(',')[1]
        xmin=box['boxes'][i][0]
        ymin=box['boxes'][i][1]
        xmax=box['boxes'][i][2]
        ymax=box['boxes'][i][3]
        cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,255),3,0)
        #using defalut font type
        font=cv2.FONT_HERSHEY_SIMPLEX
        #将文字框加入到图片中，):文本起位置，1.2：字体大小  (0,255,0):color   2:粗细
        cv2.putText(img,kind[i], (xmin,ymin-9), font,0.6, (0,255,0),2)

    #save image
    #cv2.imwrite('result1.jpg',img, [int( cv2.IMWRITE_JPEG_QUALITY), 95])

    #show image
    cv2.imshow("image",img)
    cv2.waitKey (0)

def load_pascal_annotation(index):  # 得到第index张图片的Ground Truth的bbox

    #Load image and bounding boxes info from XML file

    cls = {'0':'__background__',  # always index 0
                     '1':'state1', '2':'state2', '3':'state3', '4':'state4',
                     '5':'state5', '6':'state6'}

    path ='/home/wty/PyTestCode'
    filename = os.path.join(path, index + '.xml')
    tree = ET.parse(filename)
    objs = tree.findall('student')

    num_objs = len(objs)

    boxes = np.zeros((num_objs, 4), dtype=np.uint16)
    gt_classes =[]




    # Load object bounding boxes into a data frame.
    for ix, obj in enumerate(objs):
        bbox = obj.find('bndbox')
        # Make pixel indexes 0-based
        x1 = float(bbox.find('xmin').text) - 1
        y1 = float(bbox.find('ymin').text) - 1
        x2 = float(bbox.find('xmax').text) - 1
        y2 = float(bbox.find('ymax').text) - 1
        cls1 = cls[obj.find('state').text.lower().strip()]
        print(cls1)
        gt_classes.append(cls1)
        boxes[ix, :] = [x1, y1, x2, y2]


    #print(gt_classes)

    return {'boxes': boxes,
            'gt_classes': gt_classes,}

#box=load_pascal_annotation('000001')
#show_image_index('000001',box)
