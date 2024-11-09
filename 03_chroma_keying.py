# Enter your code here
import cv2
import numpy as np

def chroma_key(foreground_frame, background_frame, lower_color, upper_color, softness=0):
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(foreground_frame, cv2.COLOR_BGR2HSV)
    
    # Create a mask for the green screen
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Optional: Soften edges
    if softness > 0:
        kernel_size = int(softness)
        mask = cv2.GaussianBlur(mask, (kernel_size, kernel_size), 0)
    
    # Invert the mask for the foreground
    foreground_mask = cv2.bitwise_not(mask)
    
    # Extract the subject from the frame
    subject = cv2.bitwise_and(foreground_frame, foreground_frame, mask=foreground_mask)
    
    # Resize the background frame to match the size of the foreground frame
    background_frame = cv2.resize(background_frame, (foreground_frame.shape[1], foreground_frame.shape[0]))
    
    # Extract the background area from the new background frame
    background = cv2.bitwise_and(background_frame, background_frame, mask=mask)
    
    # Combine the subject and new background
    combined = cv2.add(subject, background)

    return combined

# Define the range of green color in HSV space
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# Open the video capture for the green screen video
green_screen_video = './data/greenscreen-demo.mp4'
cap_foreground = cv2.VideoCapture(green_screen_video)

# Open the video capture for the background video
background_video = './data/greenscreen-asteroid.mp4'
cap_background = cv2.VideoCapture(background_video)

while cap_foreground.isOpened() and cap_background.isOpened():
    ret_fg, frame_fg = cap_foreground.read()
    ret_bg, frame_bg = cap_background.read()
    
    # If we run out of frames in the background video, loop it
    if not ret_bg:
        cap_background.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret_bg, frame_bg = cap_background.read()

    if not ret_fg:
        break
    
    # Apply chroma keying
    output_frame = chroma_key(frame_fg, frame_bg, lower_green, upper_green, softness=5)
    
    # Display the result
    cv2.imshow('Chroma Key', output_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_foreground.release()
cap_background.release()
cv2.destroyAllWindows()