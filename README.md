# Selfie App Features Application
Bringing Fun and Practical Computer Vision Skills to Life

<img width="1057" alt="Screenshot 2024-11-10 at 2 20 18 pm" src="https://github.com/user-attachments/assets/89457c95-003b-4b97-8fe9-f7c77a557195">

## Description
This project is all about leveling up with **OpenCV** and **computer vision** techniques! Here, I’ve built tools that add cool effects to images and videos—like Cartoonify and Pencil Sketch for unique visuals, plus blemish removal and chroma keying to swap out backgrounds. Each feature explores a different aspect of image processing, making it both fun and valuable for anyone diving into computer vision.

## Features

| Cartoonify | Pencil Sketch | Blemish Removal | Chroma Keying |
|------------|---------------|-----------------|---------------|
| This feature converted images into cartoon-style visuals by applying edge detection and color quantization techniques. I developed this effect to create a fun, animated look by simplifying colors and emphasizing outlines. | The pencil sketch feature transformed images into grayscale, hand-drawn-style sketches. Using edge enhancement and shading, I designed this effect to simulate a realistic pencil-drawn look from digital images. | I implemented a blemish removal tool that cleaned up minor imperfections in images. By detecting and blending blemished areas, this feature produced smoother and clearer results, enhancing the overall image quality. | This feature enabled background replacement in videos using chroma keying, a technique that removes a specified color (typically green) and replaces it with a custom background. I created this tool to explore background manipulation, making it easy to switch video backgrounds creatively. |

## Installation

To get started with this project, follow the steps below:

1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/shamiul5201/selfie_app_features_application.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd selfie_app_features_application
    ```
3. **Install the required dependencies** manually. The project requires the following libraries:
    - OpenCV
    - NumPy
    - Jupyter (for the notebook)
    - Other libraries used in the project (such as argparse for script arguments)

   You can install these libraries using `pip`:
    ```bash
    pip install opencv-python numpy jupyter
    ```
   If you encounter any missing dependencies or errors when running the project, please install them individually as required.

4. **Ensure you have Python 3.10 or higher** installed. You can verify this by running:
    ```bash
    python --version
    ```

## Usage

### Running the Jupyter Notebook
1. To use the **Cartoonify** and **Pencil Sketch** features, open the Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
2. Open the `selfie_app_features.ipynb` notebook file and follow the instructions in the cells to run the effects on your images.
   - Make sure you have an image ready to apply the effects.
   - You can modify the image paths in the code cells as needed.

### Using the Python Scripts
For the **Blemish Removal** and **Chroma Keying** features, run the corresponding `.py` files:

- **Blemish Removal**:
    ```bash
    python blemish_removal.py --input your_image.jpg --output output_image.jpg
    ```
    This will process the input image and remove any blemishes, saving the result as `output_image.jpg`.

- **Chroma Keying** (for video background replacement):
    ```bash
    python chroma_keying.py --video input_video.mp4 --background new_background.jpg --output output_video.mp4
    ```
    This will replace the background of the video with your chosen image.

---

### Notes:
- Replace `your_image.jpg`, `input_video.mp4`, and `new_background.jpg` with your actual file names.
- The Python scripts can be run from the command line by providing the necessary arguments as shown above.

## Future Improvements

- **Enhance Image Effects**: Improve the quality of the Cartoonify and Pencil Sketch features by experimenting with more advanced filters and machine learning models to achieve more refined effects.

- **Real-Time Video Processing**: Implement real-time video processing for the Cartoonify and Pencil Sketch effects to allow these transformations to be applied live during video capture.

- **Background Removal for Chroma Keying**: Add automatic background removal to the chroma keying feature, enabling dynamic background replacement without requiring a specific color.

- **User Interface (UI)**: Develop a simple graphical user interface (GUI) to make the application more user-friendly. This UI could allow users to upload images and videos without modifying the code directly.

- **Model Optimization**: Optimize the performance of the image processing models to improve execution time, particularly for high-resolution images and longer videos.

- **Additional Filters and Features**: Introduce new filters, such as sepia tone, oil painting, or watercolor effects, to expand the creative possibilities of the application.

- **Error Handling and Logging**: Improve error handling and add logging to enhance debugging and provide better feedback when processing fails or files are missing.

## Conclusion

This project demonstrates practical applications of computer vision techniques using OpenCV, showcasing features like cartoonifying images, creating pencil sketches, removing blemishes, and implementing chroma keying in videos. Through this project, I have strengthened my skills in image processing and OpenCV, applying creative transformations to images and videos.

The project has room for further enhancements, such as real-time video processing, additional effects, and a user-friendly interface. These improvements could broaden its applications, making it a more comprehensive tool for both personal and creative use. Overall, this project represents a solid foundation in image manipulation and provides valuable opportunities for expanding its capabilities.
