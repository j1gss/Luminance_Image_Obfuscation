# Luminance Based Image Obfuscation Tool
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python)
![Numpy](https://img.shields.io/badge/Library-Numpy-red?style=flat&logo=numpy)
![PIL](https://img.shields.io/badge/Library-PIL-red?style=flat&logo=pil)
![argparse](https://img.shields.io/badge/Library-argparse-red?style=flat&logo=argparse)
![Status](https://img.shields.io/badge/Status-CLIReady-green)
## Project Review
This project deals with the problem of **visual data privacy**.Standard redaction techniques(blurring/pixelating) are becoming more susceptible to AI reconstruction.

The **Luminance Based Image Obfuscation Tool** is one of the destructive and irreversible processes of anonymising sensitive data. It employs a pixel sorting by intervals to relocate the pixels in some order according to their luminosity(brightness). The tool ruins structural details(faces or text) by converting the image into data, not a picture, and retaining the overall aesthetic and colour palette of the original media.

## Features
- **Luminance Interval Detection:** Compute brightness at the pixel level based on the Rec.601 standard having the formula: Y=0.299R+0.5876G+0.114B
- **CLI Architecture:** Written using argparse such that it can be used on the terminal flexibly, and that can be processed in batches and a range of parameters can be configured dynamically.
- **Directional Control:** Could be used vertically (`--v`) as well as horizontally (default).
- **Adjustable Thresholds:** The user has the facility of setting the luminance ranges (`--low` and `--high`) to gain control over important features.

## Technologies & Tools Used
- **Python3.x:** Core logic.
- **numPy:** The high performance multi-dimensional array manipulation to vectorize the sorting algorithm.
- **Pillow PIL:** Loads and converts images and saves them.
- **Argparse:** Python library that is used as the standard to process command-line-arguments and flags.

## Steps to Install & Run
#### 1.Clone the Repository
```
git clone https://github.com/j1gss/Luminance_Image_Obfuscation.git
```
```
cd Luminance_Image_Obfuscation
```
#### 2.Install the dependencies
```
pip install -r requirements.txt
```
#### 3.Basic Usage
```
python main.py input.jpg
```

## Instructions for Testing & Advanced Usage
In order to test the functionality of the tool,do the following test cases:
**Test Case 1: Default Horizontal Sort** *Sorts according to default values on the x-axis (horizontally)*
```
python main.py input.jpg -o output.png
```
**Test Case 2:Vertical "Drip" Obfuscation** *Vertically sorts pixels.*
```
python main.py input.jpg -o v_output.png --v
```
**Test Case 3:High Contrast** *Uses targeted sorting of images of very high brightness(Luminance 100-255)*
```
python main.py input.jpg -o output.png --low 100 --high 255
```

## Screenshots
| Input    | Default Output | Vertical Output |
| -------- | -------------- | --------------- |
| ![input](https://github.com/j1gss/Luminance_Image_Obfuscation/blob/master/ss/input.jpg)  | ![Default Output](https://github.com/j1gss/Luminance_Image_Obfuscation/blob/master/ss/output.jpg)  | ![Vertical Output](https://github.com/j1gss/Luminance_Image_Obfuscation/blob/master/ss/v_output.jpg)  |
