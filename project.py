import cv2
import os
import numpy as np
import shutil

def match_histograms(source, target):
    resized = cv2.resize(source, (target.shape[1], target.shape[0]), interpolation=cv2.INTER_LINEAR)
    return cv2.equalizeHist(resized)

def color_transfer(targetgray, referencecolor):
    ref_lab = cv2.cvtColor(referencecolor, cv2.COLOR_BGR2LAB)
    lref, aref, bref = cv2.split(ref_lab)
    target_resized = cv2.resize(targetgray, (referencecolor.shape[1], referencecolor.shape[0]))
    matched_l = match_histograms(target_resized, lref).astype(np.uint8)
    result_lab = cv2.merge((matched_l, aref.astype(np.uint8), bref.astype(np.uint8)))
    return cv2.cvtColor(result_lab, cv2.COLOR_LAB2BGR)

def extract(inputvideo, framesfolder):
    cap = cv2.VideoCapture(inputvideo)
    if not os.path.exists(inputvideo):
        print("File not found")
        return
    count = 0
    if not os.path.exists(framesfolder):
        os.makedirs(framesfolder)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(framesfolder, f"frame{count:04d}.jpg"), frame)
        count += 1
    cap.release()

def colourframes(framesfolder, processedfolder, referenceimage):
    if not os.path.exists(referenceimage):
        print("File not found")
        return
    if not os.path.exists(framesfolder):
        print("Folder not found")
        return
    refcolor = cv2.imread(referenceimage, cv2.IMREAD_COLOR)
    files = sorted(os.listdir(framesfolder))
    if not os.path.exists(processedfolder):
        os.makedirs(processedfolder)
    for file in files:
        path = os.path.join(framesfolder, file)
        if not os.path.exists(path):
            print("File not found")
            continue
        frame = cv2.imread(path)
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        colorized = color_transfer(grayframe, refcolor)
        cv2.imwrite(os.path.join(processedfolder, file), colorized)

def videoputback(processedfolder, outputvideo, fps):
    if not os.path.exists(processedfolder):
        print("Folder not found")
        return
    files = sorted(os.listdir(processedfolder))
    if not files:
        print("File not found")
        return
    exampleframe = cv2.imread(os.path.join(processedfolder, files[0]))
    h, w, _ = exampleframe.shape
    writer = cv2.VideoWriter(outputvideo, cv2.VideoWriter_fourcc(*'DIVX'), fps, (w, h))
    for file in files:
        path = os.path.join(processedfolder, file)
        if not os.path.exists(path):
            print("File not found")
            continue
        frame = cv2.imread(path)
        writer.write(frame)
    writer.release()

def emptyfolder(folderpath):
    if not os.path.exists(folderpath):
        print("Folder not found")
        return
    for item in os.listdir(folderpath):
        path = os.path.join(folderpath, item)
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)

def processvideo(inputvideo, referenceimage, outputvideo):
    framesdir = "extractedframes"
    processeddir = "processedframes"
    extract(inputvideo, framesdir)
    colourframes(framesdir, processeddir, referenceimage)
    cap = cv2.VideoCapture(inputvideo)
    if not os.path.exists(inputvideo):
        print("File not found")
        return
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    videoputback(processeddir, outputvideo, fps)
    emptyfolder(framesdir)
    emptyfolder(processeddir)

inputvideo = r"C:/Users/HP/Desktop/DIP-OpenCV-Learning/Images/input_video.mp4"
referenceimage = r"C:/Users/HP/Desktop/DIP-OpenCV-Learning/Images/ref.png"
outputvideo = r"C:/Users/HP/Desktop/DIP-OpenCV-Learning/Images/output_video.avi"

processvideo(inputvideo, referenceimage, outputvideo)
