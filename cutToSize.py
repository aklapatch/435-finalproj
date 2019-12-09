import cv2
from os import walk
import os

def shrinkSquareImage(infile, outfile, dims):
    "reads in an image, and reduces it by factor it, and writes it to outfile"

    img = cv2.imread(infile)
    h,w = img.shape[:2]
    if h == w:
            output = cv2.resize(img, dims )
            cv2.imwrite(outfile, output)
        
dir = "../ALOTCUTDOWN"
outdir = "../ALOT384"

# open a folder and resize all the images inside
f = []
for (dirpath, dirnames, filenames) in walk(dir):
    f.extend(filenames)

# make the directory for the resized images.
if not(os.path.isdir(outdir)):
    os.makedirs(outdir)

# resize original images
for imgname in f: 
    if imgname.find("png", 0) != -1:
        fname = dir + "/" + imgname
        outname = outdir + "/" + imgname
        shrinkSquareImage(fname, outname, (384,384))