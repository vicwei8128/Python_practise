#Using opencv to calculate PCA for image orientation correction(https://www.programmersought.com/article/9534136088/)
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
import math

import ImageDisplay

def drawAxis(img, p_, q_, colour, scale):
    p = list(p_)
    q = list(q_)
    
    angle = math.atan2(p[1] - q[1], p[0] - q[0]) # angle in radians
    hypotenuse = math.sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))
    # Here we lengthen the arrow by a factor of scale
    q[0] = p[0] - scale * hypotenuse * math.cos(angle)
    q[1] = p[1] - scale * hypotenuse * math.sin(angle)
    cv2.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA)
    # create the arrow hooks
    p[0] = q[0] + 9 * math.cos(angle + math.pi / 4)
    p[1] = q[1] + 9 * math.sin(angle + math.pi / 4)
    cv2.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA)
    p[0] = q[0] + 9 * math.cos(angle - math.pi / 4)
    p[1] = q[1] + 9 * math.sin(angle - math.pi / 4)
    cv2.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 1, cv2.LINE_AA)
    
def getOrientation(pts, img):    
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)
    for i in range(data_pts.shape[0]):
        data_pts[i,0] = pts[i,0,0]
        data_pts[i,1] = pts[i,0,1]
    # Perform PCA analysis
    mean = np.empty((0))
    mean, eigenvectors, eigenvalues = cv2.PCACompute2(data_pts, mean)
    # mean, eigenvectors = cv2.PCACompute(data_pts, mean, 2) #image, mean=None, maxComponents=10
    # Store the center of the object
    cntr = (int(mean[0,0]), int(mean[0,1]))

    cv2.circle(img, cntr, 3, (255, 0, 255), 2) #Draw a circle at the center of PCA
    p1 = (cntr[0] + 0.02 * eigenvectors[0,0] * eigenvalues[0,0], cntr[1] + 0.02 * eigenvectors[0,1] * eigenvalues[0,0])
    p2 = (cntr[0] - 0.02 * eigenvectors[1,0] * eigenvalues[1,0], cntr[1] - 0.02 * eigenvectors[1,1] * eigenvalues[1,0])
    drawAxis(img, cntr, p1, (0, 255, 0), 1) # , 
    drawAxis(img, cntr, p2, (255, 255, 0), 1) #yellow
    angle = math.atan2(eigenvectors[0,1], eigenvectors[0,0]) # orientation in radians #PCA first dimension angle    
    return angle

def rotate_img(img,angle):
    """ center rotates the image, the input angle is radians """
    angle_o=(angle-math.pi/2)*180/math.pi # 
    height = img.shape[0]  # original image height
    width = img.shape[1]  # original image width
    rotateMat = cv2.getRotationMatrix2D((width / 2, height / 2), angle_o, 1)  # Rotate the image by angle
    heightNew = int(width * math.fabs(math.sin(angle)) + height * math.fabs(math.cos(angle)))
    widthNew = int(height * math.fabs(math.sin(angle)) + width * math.fabs(math.cos(angle)))

    rotateMat[0, 2] += (widthNew - width) / 2  
    rotateMat[1, 2] += (heightNew - height) / 2
    imgRotation = cv2.warpAffine(img, rotateMat, (widthNew, heightNew), borderValue=(255, 255, 255))
    return imgRotation

src = cv2.imread(r"images/tower.jpg")
src=cv2.resize(src,(350,350))

# cv2.imshow('src', src)
#plt.figure(1);plt.imshow(src,cmap='gray')
# Convert image to grayscale
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# Convert image to binary
_, bw = cv2.threshold(src, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(bw, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
areas=[]
areas_angle=[]
imageContour = bw.copy()
for i, c in enumerate(contours):
    # Calculate the area of each contour
    area = cv2.contourArea(c)
    # Ignore contours that are too small or too large
    if area < 1e2 or 1e5 < area:
        continue
    areas.append(area)
    # Draw each contour only for visualisation purposes
    cv2.drawContours(imageContour, contours, i, (0, 0, 255), 2)
    # Find the orientation of each shape
    angle=getOrientation(c, imageContour)
    areas_angle.append(angle)
# cv2.imshow('output', src)
# cv2.waitKey()

# Calculate the direction of the largest connected domain
ind=np.argmax(areas)
imgRotation=rotate_img(src,areas_angle[ind])

tileImage=ImageDisplay.concat_tile_resize([[src, bw], [imageContour, imgRotation]])
cv2.imshow('Source-Grey-Contour-Rotation', tileImage)
cv2.waitKey()
print("done")