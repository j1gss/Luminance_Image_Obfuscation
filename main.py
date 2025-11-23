"""program that takes an image,selects rows of pixels
based on a threshold(luminance), & sorts them vertically or horizontally"""
import numpy as np
import PIL.Image as Image
import argparse

def sort_pixs(row,start,end):
    sub=row[start:end]
    lum=np.array([0.299,0.587,0.114])
    lum_vals=np.sum(sub*lum,axis=1)
    sorted=np.argsort(lum_vals)
    return sub[sorted]

def row(row,low,high):
    lum_row=np.sum(row*[0.299,0.587,0.114],axis=1)
    mask=(lum_row>=low) & (lum_row<=high)
    idx_start=None
    for i, is_active in enumerate(mask):
        if is_active:
            if idx_start is None:
                idx_start=i
        else:
            if idx_start is not None:
                row[idx_start:i]=sort_pixs(row,idx_start,i)
                idx_start=None
    if idx_start is not None:
        row[idx_start:]=sort_pixs(row,idx_start,len(row))
    return row

def pix_sort(inp_path,out_path,low,high,vertical=True):
    print("Pixel Sorting")
    img=Image.open(inp_path).convert('RGB')
    pixs=np.array(img)
    if vertical:
        pixs=np.rot90(pixs)
    height,width,_=pixs.shape
    for h in range(height):
        pixs[h]=row(pixs[h],low,high)
    if vertical:
        pixs=np.rot90(pixs,-1)
    result_img=Image.fromarray(pixs)
    result_img.save(out_path)
    print("Pixels Sorted")

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Interval Based Pixel Sorter")
    parser.add_argument("input_image",help="path to input image")
    parser.add_argument("-o","--output",help="path to save output image",default="output.png")
    parser.add_argument("--v",action="store_true",help="vertical sorting(default:horizontal")
    parser.add_argument("--low",type=int,default=0,help="lower threshold")
    parser.add_argument("--high",type=int,default=250,help="upper threshold")
    args=parser.parse_args()

    pix_sort(
    inp_path=args.input_img,
    out_path=args.output,
    low=args.low,
    high=args.high,
    vertical=args.v
    )