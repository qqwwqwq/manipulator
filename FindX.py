import numpy as np
np.set_printoptions(suppress=True)
import cv2
import glob

blocksize=[11,8]
with np.load('B.npz') as X:
    mtx, dist, _, _ = [X[i] for i in ('mtx','dist','rvecs','tvecs')]
print(mtx,dist)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((blocksize[0]*blocksize[1],3), np.float32)
objp[:,:2] = np.mgrid[0:blocksize[0],0:blocksize[1]].T.reshape(-1,2)
# def draw(img, corners, imgpts):
#     corner = tuple(corners[0].ravel())
#     img = cv2.line(img, corner, tuple(imgpts[0].ravel()), (255,0,0), 5)
#     img = cv2.line(img, corner, tuple(imgpts[1].ravel()), (0,255,0), 5)
#     img = cv2.line(img, corner, tuple(imgpts[2].ravel()), (0,0,255), 5)
#     return img
def findc(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (blocksize[0], blocksize[1]), None)
    if ret == True:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        # Find the rotation and translation vectors
        s, rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)
        e = cv2.Rodrigues(rvecs)[0]
        # tra=np.array([[tvecs[0]],[tvecs[1]],[tvecs[2]]])
        tra = np.array([[0, 0, 0, 1]])
        ll = np.concatenate([e, tvecs], axis=1)
        trasp = np.concatenate([ll, tra], axis=0)
        print(trasp, 'cameras')
        return trasp



axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]).reshape(-1,3)
for fname in glob.glob("/Users/apple/Desktop/image"+'/*'):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (blocksize[0],blocksize[1]),None)

    if ret == True:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)

        # Find the rotation and translation vectors.

        s,rvecs, tvecs, inliers = cv2.solvePnPRansac(objp, corners2, mtx, dist)
        e=cv2.Rodrigues(rvecs)[0]
        #tra=np.array([[tvecs[0]],[tvecs[1]],[tvecs[2]]])
        tra = np.array([[0,0,0,1]])
        ll=np.concatenate([e,tvecs],axis=1)
        trasp=np.concatenate([ll,tra],axis=0)
        print(trasp,'cameras')
        # project 3D points to image plane
        # imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
        # img = draw(img,corners2,imgpts)
        # cv2.imshow('img',img)
        # k = cv2.waitKey(0) & 0xff
        # if k == 's':
        #     cv2.imwrite(fname[:6]+'.png', img)

cv2.destroyAllWindows()