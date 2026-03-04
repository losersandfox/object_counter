import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import ErrorWindow
import SubEditWindow
from PyQt5.QtWidgets import QDialog


def connected_component_labeling(image_path, type, value = 5):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if not image_path:
        error_window = ErrorWindow.ErrorWindow("请输入图片路径")
        error_window.exec_()
        return False 
    
    if not os.path.exists(image_path):
        error_window = ErrorWindow.ErrorWindow("图片路径不存在")
        error_window.exec_()
        return False
    
    bw_type = 0
    if(type[0] == 0):
        bw_type = cv2.THRESH_BINARY
    elif(type[0] == 1):
        bw_type = cv2.THRESH_BINARY_INV
    else:
        error_window = ErrorWindow.ErrorWindow("请选择黑白是否反转")
        error_window.exec_()
        return False
    
    binary = None

    if(type[1] == 0):
        _, binary = cv2.threshold(img, 0, 255, bw_type + cv2.THRESH_OTSU)
    elif(type[1] == 1):
        sub_edit_window = SubEditWindow.SubEditWindow("自适应阈值内核值")
        # 使用exec_()的返回值判断用户是点击了确定还是取消
        if sub_edit_window.exec_() == QDialog.Accepted:  # 或使用1/QDialog.DialogCode.Accepted
            value = sub_edit_window.getText()
            # 确保value是有效的正奇数
            if value > 0 and value % 2 == 1:
                binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, bw_type, value, 2)
            else:
                error_window = ErrorWindow.ErrorWindow("必须为奇数")
                error_window.exec_()
                return False
        else:
                
            return False 
    else:
        error_window = ErrorWindow.ErrorWindow("请选择二值化类型")
        error_window.exec_()
        return None
    if(type[2] == 1):
        sub_edit_window = SubEditWindow.SubEditWindow("高斯模糊内核值")
        
        if sub_edit_window.exec_() == QDialog.Accepted: 
            value = sub_edit_window.getText()

            if value > 0 and value % 2 == 1:
                binary = cv2.GaussianBlur(binary, (value, value), 0)
            else:
                error_window = ErrorWindow.ErrorWindow("必须为奇数")
                error_window.exec_()
                return False 
        else:
                
            return False 

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)
    
    output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    
    for i in range(1, num_labels): 

        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
        center_x = int(centroids[i][0])
        center_y = int(centroids[i][1])
        cv2.circle(output, (center_x, center_y), 2, (0, 255, 0), -1)
        
        cv2.putText(output, f'No.{i}', (x, y-5), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

    plt.figure(figsize=(12, 4))
    
    plt.subplot(131)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(binary, cmap='gray')
    plt.title('Binary Image')
    plt.axis('off')
    
    plt.subplot(133)
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
    plt.title(f'Labeled Image, the number: {num_labels-1}')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
    return True
