# Selfie App Features Application
Welcome to this repository! This project showcases a variety of image processing features implemented using Python. Below, you'll find an overview of the three key features included in this repository:

   
<img width="1057" alt="Screenshot 2024-11-10 at 2 20 18 pm" src="https://github.com/user-attachments/assets/89457c95-003b-4b97-8fe9-f7c77a557195">

3. Blemish Removal output

https://github.com/user-attachments/assets/bfd299eb-ed15-4f58-ae57-2fc2414e2e41


4. Chroma Keying Output
   
https://github.com/user-attachments/assets/e6b96933-6904-46da-a102-698107a35f2b

## Blemish Removal

### Overview
The blemish removal tool is an interactive image-editing utility designed to remove unwanted spots or blemishes from an image. It allows users to click on a blemish in the image, automatically identifies the best replacement patch, and blends the patch seamlessly into the selected area. This is achieved through gradient-based patch selection and seamless cloning using OpenCV.


### Key Functions and Their Purposes
1. **`sobel_filter(crop_img)`**  
   - Calculates gradients in the x and y directions for a given image patch using the Sobel operator.  
   - These gradients are used to identify texture changes, which help find smooth patches for replacement.  

2. **`append_dictionary(x, y, r, source)`**  
   - Extracts a patch from the image and calculates its gradients using `sobel_filter`.  
   - Returns the gradient information, which helps assess the patch's smoothness.  

3. **`identify_best_patch(x, y, r, source)`**  
   - Searches for candidate patches around the blemish location.  
   - Compares patches and selects the one with the smoothest gradients (lowest combined x and y gradients) for replacement.  

4. **`selected_blemish(x, y, r, source)`**  
   - Wrapper function that calls `identify_best_patch` and returns the optimal patch location for a blemish.  

5. **`blemish_removal(action, x, y, flags, userdata)`**  
   - Handles mouse events, allowing the user to select blemishes interactively:  
     - **Left Mouse Click:** Selects a blemish and replaces it with the best-matching patch using OpenCV's `seamlessClone`.  
     - **Mouse Release:** Updates and displays the modified image.  

6. **Main Loop**  
   - Sets up the OpenCV window and listens for user actions:  
     - **Key 'C':** Resets the image to its original state.  
     - **Esc Key:** Exits the application.  
   - Displays the interactive blemish removal tool.

### Usage and Prerequisites
#### Prerequisites
1. Install OpenCV and NumPy:
   ```python
   pip install opencv-python numpy
   ```
2. Execute the script:
   ```python
   python 02_blemish_removal.py
   ```

#### Example Use Case
- **Removing small imperfections in portrait images for photo editing.**

---


##  Chroma Keying  

### Overview

The chroma keying tool replaces a specific color (e.g., green screen) in a video or image with a new background. This technique is widely used in video editing, film production, and real-time streaming to create visually dynamic content.

### Key Functions and Their Purposes  

1. **`chroma_key(foreground_frame, background_frame, lower_color, upper_color, softness=0)`**  
   - Implements the chroma key (green screen) effect by performing the following steps:  
     - Converts the foreground image to HSV color space.  
     - Creates a binary mask to isolate the specified color range (e.g., green screen).  
     - Optionally applies Gaussian blur to soften the edges of the mask.  
     - Extracts the subject from the foreground using the inverted mask.  
     - Resizes the background to match the size of the foreground frame.  
     - Replaces the masked area with the resized background.  

2. **Main Loop**  
   - Reads frames from the foreground (green screen) and background videos.  
   - Applies the `chroma_key` function frame-by-frame.  
   - If the background video runs out of frames, loops it to ensure continuous playback.  
   - Displays the composited video output in real-time.  
   - Exits the application when the **'Q' key** is pressed.
