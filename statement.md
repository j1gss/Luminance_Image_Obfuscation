# Project Statement
### 1.Problem Statement
In the new world of computer vision and artificial intelligence, data privacy is becoming a thing of the past. Traditional methods of image redaction like **Gaussian blur, pixelation, black box masking** are becoming obsolete.

As a result of recent advancements in **Deconvolutional Neural Networks (DNNs)**, AI models are able to perform the reverse process of pixelation in order to reconstruct the original data from pixelated patterns with horrifying accuracy. This is a major security threat for those who want to share visual data that may include **Personally Identifiable Information (PII)**, such as faces, license plates, or confidential documents. An urgent requirement, therefore exists on an obfuscation method that allows **mathematical irreversible noise** with the aesthetic context of the original media to be preserved.

### 2.Scope of the Project
This project deals with development of a **Python** based **Command Line Interface (CLI)** tool in for destructive image obfuscation.

**The scope includes:**
- **Algorithm Implementation:** Coming up with a tailor made interval based pixel sorting algorithm with the help of NumPy library.
- **Luminance Calculation:** The application of the **ITU-R** standard of **BT.601** (`Y=0.299R+0.587G+0.114B`) to transform RGBs to brightness as seen by a human being.
- **User Interaction:** To provide a more user-friendly interface, a CLI was made using `argparse` which allows users to dynamically input the file paths and alter obfuscation parameters(thresholds & directions).
- **Data Handling:** Uses the Pillow library to input and export common raster image formats.

**The scope excludes:**
- Video processing in real time (the current version deals with stationary images).
- Development of Graphical User Interface (GUI) (emphasis is put on backend logic and using terminals).

### 3.Target Users
This is a tool for technical users worried with data security and dataset integrity:
- **Data Scientists & ML Engineers:** Who must scrub or blind or anonymize publicly available data before it is used to train a model, to comply with GDPR/DPDP/privacy policies.
- **Investigative Journalists:** Who need to remove identifiable aspects of sources or locations without using low tech thick black boxes that mask the entire scene.
- **Security Researchers:** Who require tools to produce "corrupted" or "glitched" data in order to stress-test the robustness of Computer Vision systems.

### 4.High Level Features
- **Perceptual Luminance Masking:** This tool does not use the explicit colour thresholding but picks pixels in areas based on perceived-luminance, which can target particular features of the image such as skin tone or retro reflective license plates.
- **Dynamic Thresholding:** It is possible to define the individual low and high values (0-255) for the users. This enables surgery esque precision i.e., obscuring only the light type on a page and not the ink, or reverse.
- **Destructive Interval Sorting:** Physical rearrangement of pixel data is the main characteristic of this technique. The spatial relationship on which facial recognition is based is destroyed by sorting pixels in contiguous intervals thus reconstruction is computationally infeasible.
- **Multi Directional Processing:** Allows **Vertical** (gravity/drip effect) and **Horizontal** (wind/streak effect) ways of sorting the image in case of various image composition.

### 5.Future Scope (Intended Improvements)
- **Support Real Time Webcams:** Optimize the algorithm to live video feeds for real time privacy masking.
- **Face Detection Integration:** Integration of OpenCV that makes the system detect faces automatically and apply the pixel sort only to the face bounding box and elimintes the problem of user having to guess the value of threshold.
- **Steganography:** It is also possible to add an extra parameter to reverse a sort(decrypt), in case a special key is provided,allowing for safe data transfer encrypted in the glitch art.
