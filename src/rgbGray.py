import numpy as np

def rgbtogray_AVG(img):
    return np.mean(img,axis=2)
def rgbtogray_weighted(img):
    w_r,w_g,w_b=0.299,0.587,0.114
    imgray = w_r*img[...,0] + w_g*img[...,1] + w_b*img[...,2]
    return imgray