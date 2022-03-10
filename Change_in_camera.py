import cv2
import numpy as np
def frame_diff(prev_frame, cur_frame, next_frame):
    diff_frames_1 = cv2.absdiff(next_frame,cur_frame)
    diff_frames_2=cv2.absdiff(cur_frame,prev_frame)

    return cv2.bitwise_and(diff_frames_1,diff_frames_2)

def get_frame(cap):
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
##    (thresh, blackAndWhiteImage) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
##This would help us to make canny(however it have error)
    return gray
if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    prev_frame = get_frame(cap)
    cur_frame = get_frame(cap)
    next_frame = get_frame(cap)
    #cv2.imwrite(r'C:/Users/YOURUSERNAME/Desktop/samplenew.png', next_frame)
    c=0
    list1=[0]
while True:
    c=c+1
    a=frame_diff(prev_frame,cur_frame, next_frame)
    cv2.imshow('Object Movement',a)
    prev_frame = cur_frame
    cur_frame = next_frame
    print(int(np.sum(a)))
    next_frame = get_frame(cap)
    key = cv2.waitKey(1)
    if key == 27:
        break
    """b=frame_diff(prev_frame,cur_frame, next_frame)
    cv2.imshow('Object Movement',b)
    prev_frame = cur_frame
    cur_frame = next_frame
    sum2=int((np.sum(b)))
    next_frame = get_frame(cap)
    key = cv2.waitKey(1)
    if key == 27:
        break
    print (abs((sum1-sum2)))
    list1.append
    """

