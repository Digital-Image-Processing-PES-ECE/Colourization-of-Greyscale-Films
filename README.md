Colourization of Greyscale Films

### Project Description:
This project focuses on colorizing grayscale video frames using a reference image for color transfer. The process begins by extracting frames from the input video, which are then converted to grayscale. A reference image, typically a color image, is used to guide the colorization process. The core technique involves histogram matching and color transfer, where the grayscale frames are resized to match the reference image and the luminance (brightness) values of each frame are adjusted to match those of the reference. This ensures that the grayscale frames are colorized with similar color tones to the reference image.

The project is structured into four main functions: `extract`, which extracts frames from the video; `colourframes`, which colorizes the grayscale frames using the reference image; `videoputback`, which recomposes the colorized frames into a new video; and `emptyfolder`, which cleans up temporary folders used for storing extracted and processed frames. After the frames are processed, the colorized frames are combined into a new video, retaining the original video's frame rate and resolution. This process helps enhance old grayscale videos by giving them a realistic color appearance, making them more visually appealing while preserving the original content.

#### Course concepts used - 
1. - Histogram Mathcing
2. - Greyscale Conversion
3. - Image resizing
   
#### Additional concepts used -
1. - Colour Transfer
2. - Frame extraction
3. - Video Processing and FPS Handling
   
#### Dataset - 
Link and/or Explanation if generated

#### Novelty - 
1. - Grayscale video colorization using reference image.
2. - Histogram matching for consistent color transfer.
3. - Efficient frame extraction, processing, and video creation.
   
### Contributors:
1. Dharun Pranaav K B (PES1UG22EC068)
2. Dheemanth Bhushan (PES1UG22EC069)

### Steps:
1. Clone Repository
```git clone https://github.com/Digital-Image-Processing-PES-ECE/Colourization-of-Greyscale-Films.git ```

2. Install Dependencies
```pip install -r requirements.txt```

3. Run the Code
```project.py```

### Outputs:
* Check for the 2 folders they must have images during the code running and should be empty once the Code has completed Running
* Final output video must be coloured

### References:
1. -F. S. Mohamad, A. A. Manaf and S. Chuprat, "Histogram matching for color detection: A preliminary study," 2010 International Symposium on Information Technology, Kuala Lumpur, Malaysia, 2010, pp. 1679-1684, doi: 10.1109/ITSIM.2010.5561637
2. -Qi-Chong Tian, Laurent D. Cohen. Histogram-based Color Transfer for Image Stitching. Journal of Imaging, 2017, 3 (3), ⟨10.3390/jimaging3030038⟩. ⟨hal-01617305⟩
   
### Limitations and Future Work:
Limitations:

Dependence on reference image quality: The effectiveness of colorization is highly reliant on the quality and relevance of the reference image. Poor or mismatched references can lead to unnatural colorization results.

Limited to similar scenes: The color transfer works best when the scenes in the video are similar to the reference image, making it less adaptable to diverse or dynamic scenes.

Processing time for large videos: Extracting, processing, and recomposing video frames can be computationally expensive, especially for long or high-resolution videos.

Future Work:

Integration of advanced colorization algorithms: Exploring more sophisticated methods like gradient-based or texture-aware colorization to enhance visual accuracy without relying on a single reference image.

Real-time video processing: Implementing more optimized algorithms for faster video processing, potentially enabling real-time colorization for live or streaming videos.

Enhancing adaptability to diverse scenes: Developing methods to improve the colorization process across varying lighting conditions, object types, and environments to handle a broader range of video content.
