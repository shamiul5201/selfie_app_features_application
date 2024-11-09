# Enter your code here
import cv2
import numpy as np

# Parameters
radius = 15

def sobel_filter(crop_img):
    """Apply Sobel filter to calculate gradients."""
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    gradient_x = np.mean(np.abs(sobel_x))
    gradient_y = np.mean(np.abs(sobel_y))
    return gradient_x, gradient_y

def append_dictionary(x, y, r, source):
    """Extract patch and calculate gradients."""
    crop_img = source[y:y + 2 * r, x:x + 2 * r]
    gradient_x, gradient_y = sobel_filter(crop_img)
    return gradient_x, gradient_y

def identify_best_patch(x, y, r, source):
    """Identify the best patch for blemish replacement."""
    patches = {}
    directions = [(2 * r, 0), (2 * r, r), (-2 * r, 0), (-2 * r, -r),
                  (0, 2 * r), (r, 2 * r), (0, -2 * r), (-r, -2 * r)]

    for idx, (dx, dy) in enumerate(directions, 1):
        new_x, new_y = x + dx, y + dy
        gradient_x, gradient_y = append_dictionary(new_x, new_y, r, source)
        patches[f'Key{idx}'] = (new_x, new_y, gradient_x, gradient_y)

    # Find the best patch
    best_key = min(patches, key=lambda k: patches[k][2] + patches[k][3])
    best_x, best_y, _, _ = patches[best_key]
    return best_x, best_y

def selected_blemish(x, y, r, source):
    """Select the blemish and identify the best patch."""
    return identify_best_patch(x, y, r, source)

def blemish_removal(action, x, y, flags, userdata):
    """Handle mouse events for blemish removal."""
    global source, radius

    if action == cv2.EVENT_LBUTTONDOWN:
        blemish_location = (x, y)
        new_x, new_y = selected_blemish(x, y, radius, source)
        new_patch = source[new_y:new_y + 2 * radius, new_x:new_x + 2 * radius]

        # Create mask for the new patch
        mask = 255 * np.ones(new_patch.shape, new_patch.dtype)

        # Apply the patch using seamless cloning
        source = cv2.seamlessClone(new_patch, source, mask, blemish_location, cv2.NORMAL_CLONE)
        cv2.imshow("Blemish Removal App", source)

    elif action == cv2.EVENT_LBUTTONUP:
        cv2.imshow("Blemish Removal App", source)

if __name__ == "__main__":
    # Load the source image
    source = cv2.imread("./data/blemish.png")

    # Make a dummy image to reset
    dummy = source.copy()

    # Set up the window and mouse callback
    cv2.namedWindow("Blemish Removal App")
    cv2.setMouseCallback("Blemish Removal App", blemish_removal)

    # Main loop
    while True:
        cv2.imshow("Blemish Removal App", source)
        key = cv2.waitKey(20) & 0xFF
        if key == 27:  # Esc key to exit
            break
        elif key == ord('c'):  # 'c' key to clear drawing
            source = dummy.copy()

    cv2.destroyAllWindows()
