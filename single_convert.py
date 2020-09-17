import cv2
import os
import argparse

# Necessary Arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i',"--input",required = True, type = str, help = "Input for the video files")
ap.add_argument('-o',"--output",required = True, type = str, help = "Output directory for the images extracted")
ap.add_argument('-fps',"--framesps", default=int(cv2.CAP_PROP_FPS) ,help = "Extract at the desired Frame rate")
ap.add_argument('-frate',"--frate",default=0.1, type=float, help="To determine the amount of frames to be extracted per second")
args=vars(ap.parse_args())

video_path = args['input']
save_path = args['output'] 
skip_frames = args['framesps']
frameRate = args['frate']






def length_of_video(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def extracting_frames(video_path,save_path,skip_frames):
    length = length_of_video(video_path)
    if length == 0:
        print("Length is 0,Video not Available")
        return 0

    cap = cv2.VideoCapture(video_path)
    count = 0

    ret,frame = cap.read()
    test_file_path = save_path + "image" + str(count) +".png"
    cv2.imwrite(test_file_path,frame)

    if os.path.isfile(test_file_path):
        print("Saving Test Frame successful")
        count = 1
        while ret:
            ret,frame = cap.read()
            if ret and count%int(skip_frames/(frameRate))==0:
                #naming
                name = save_path + "image" + str(count) +".png"
                cv2.imwrite(name,frame)
                print(name)
                count+=1
            else:
                count+=1
    else:
        print("Problem saving the Test Frame.")
        return 0
    cap.release()

extracting_frames(video_path,save_path,skip_frames)