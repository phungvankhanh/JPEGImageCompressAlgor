# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
#import math
#Ưf=math.floor(2.9)
def RGB2YUV( rgb ):
     
    m = np.array([[ 0.29900, -0.16874,  0.50000],
                 [0.58700, -0.33126, -0.41869],
                 [ 0.11400, 0.50000, -0.08131]])
     
    yuv = np.dot(rgb,m)
    yuv[:,:,1:]+=128.0
    return yuv

def YUV2RGB( yuv ):
      
    m = np.array([[ 1.0, 1.0, 1.0],
                 [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                 [ 1.4019975662231445, -0.7141380310058594 , 0.00001542569043522235] ])
    
    rgb = np.dot(yuv,m)
    rgb[:,:,0]-=179.45477266423404
    rgb[:,:,1]+=135.45870971679688
    rgb[:,:,2]-=226.8183044444304
    return rgb


i = Image.open("C:/Users/khanh/Desktop/Multimedia/test.jpg")

#i = i.convert("P")
a = np.asarray(i)
a.setflags(write=1)
###################################################################################
###### TASK DONE:   +   Đọc file ảnh jpeg or jpg và chuyển sang array và xử lý    #
#                   +   chuyển đổi RGB sang YUV và ngược lại                      #
###################################################################################

#########################################################################################
###### TODO:    +   từ array của YUV đọc 8x8 pixel                                      #
#               +   từ mảng 8x8 pixel dùng biến đổi DCT                                 #
#               +   Từ biến đổi DCT dùng lượng tử hóa vecto,... ra file đã nén 111001.. #
#               +   nâng cấp chương trình lên UI, có nút chọn file, hiện kích cỡ        #
#                   file, file sau khi nén, tỷ lệ nén, chọn thư mục đầu ra.             #
#########################################################################################

#print a[0][0]
#for i in range(0,612):
  #  for j in range(0,612):
        #if (i%2 == 0) and (j%2 == 0):
            #for k in range(0,3):
         #       a[i][j] = [80,223,58]
    
#a[306][306] = [255,0,0]
print a
b = RGB2YUV(a)
print len(b)
print b
c = YUV2RGB(b)
print len(c)
print c
###### END-TODO
         
#print a
#print a[0][0]
#print len(a[0])
#print len(a)
#b = np.abs(np.fft.rfft2(a))
for i in range(0,612):
    for j in range(0,612):
        #if (i%2 == 0) and (j%2 == 0):
            for k in range(0,3):
                c[i][j][k] = round(c[i][j][k])
print c.astype('uint8')

j = Image.fromarray(c.astype('uint8'))
j.save("C:/Users/khanh/Desktop/Multimedia/loi_noi_hay_trans.jpg")
print a[0][0][0]
print int(2.9)
print round(2.9999999)
print "Success"
