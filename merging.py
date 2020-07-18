import cv2
import numpy as  np
from matplotlib import pyplot as plt
image=cv2.imread("apple.jpg")
im=cv2.imread(".jpg")


image=cv2.resize(image,(500,500))
im=cv2.resize(im,(500,500))

lay=image.copy()
l=im.copy()
gp=[lay]
ap=[l]
for i in range(6):
    lay=cv2.pyrDown(lay)
    gp.append(lay)
for i in range(6):
    l=cv2.pyrDown(l)
    ap.append(l)
op1=gp[5]
op=[op1]
for i in range(5,0,-1):
    g_p=cv2.pyrUp(gp[i])
    g_p=cv2.resize(g_p,gp[i-1].shape[-2::-1])
    a1=cv2.subtract(gp[i-1],g_p)
    op.append(a1)
op2=ap[5]
o_p=[op2]
for i in range(5,0,-1):
    a_p=cv2.pyrUp(ap[i])
    a_p=cv2.resize(a_p,ap[i-1].shape[-2::-1])
    b1=cv2.subtract(ap[i-1],a_p)
    o_p.append(b1)
apple_orange_pyramid=[]
for a,o in zip(op,o_p):
    cols,rows,ch=a.shape
    lap=np.hstack((a[:, :int(cols/2)],o[:, int(cols/2):]))
    apple_orange_pyramid.append(lap)
apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv2.resize(apple_orange_reconstruct,apple_orange_pyramid[i].shape[-2::-1])
    apple_orange_reconstruct=cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)


cv2.imshow("dd",apple_orange_reconstruct)


cv2.waitKey(0)
cv2.destroyAllWindows()

