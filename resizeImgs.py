import cv2
from os import walk
import os

def shrinkImage(infile, outfile, divisor):
    "reads in an image, and reduces it by factor it, and writes it to outfile"

    img = cv2.imread(infile)
    h,w = img.shape[:2]
    h = int(h/divisor)
    w = int(w/divisor)

    output = cv2.resize(img, (w, h) )
    cv2.imwrite(outfile, output)
dir = "orig-images"
outdir = "resizedImages"


# open a folder and resize all the images inside
f = []
for (dirpath, dirnames, filenames) in walk(dir):
    f.extend(filenames)

# make the directory for the resized images.
if not(os.path.isdir(outdir)):
    os.makedirs(outdir)
# resize original images
for imgname in f: 
    if imgname.find("jpg", 0) != -1:
        fname = dir + "/" + imgname
        outname = outdir + "/" + imgname
        shrinkImage(fname, outname, 2)