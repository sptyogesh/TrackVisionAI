# 🚀 *TrackVisionAI: Object Tracking and Detection with YOLO & Computer Vision** 📹

Welcome to the Object Tracker project! This application leverages object tracking technology to process videos, calculate key metrics and visualize the results. It is designed to meet the following core objectives:

- **Track objects** in a video.
- **Calculate and display specific metrics** such as total time each object spends in the video and the total number of unique object IDs detected.
- **Visualize tracking results** including bounding boxes, centroids, and trails.
- **Export the results** as a video and display it in an HTML window.

## 📝 **Table of Contents**

- [Project Overview](#project-overview)
- [Core Features](#core-features)
- [Tech Stack](#tech-stack)
- [How to Run the Application](#how-to-run-the-application)
- [Metrics Calculated](#metrics-calculated)
- [Visualizations](#visualizations)
- [Output Video](#output-video)
- [Testing](#testing)


## 🎯 **Project Overview**

This project is designed to automatically track and annotate objects in a given video using YOLO (You Only Look Once) object detection. The system tracks the objects, calculates various metrics, and outputs a processed video with bounding boxes, object trails and centroids displayed. Additionally, it saves the output video in a format suitable for web display.

## 🛠️ **Core Features**

- **Object Tracking**: Detect and track objects throughout the video.
- **Metric Calculation**: 
  - Track the total time each object stays in the video.
  - Calculate the number of unique object IDs.
- **Visualization**: 
  - Draw bounding boxes around tracked objects.
  - Display centroids for each object.
  - Show the trail of each object’s movement.
- **Export Video**: Save the processed video with visual annotations.
- **Web Integration**: View the video result seamlessly in a browser.

## 🖥️ **Tech Stack**

- **Flask**: Lightweight web framework for handling file uploads and displaying results.
- **YOLOv8 (Ultralytics)**: Object detection model for tracking and annotating objects in videos.
- **OpenCV**: Library for processing video and drawing visual elements.
- **Pillow (PIL)**: Python Imaging Library for handling image formats.
- **JavaScript** (HTML5 Video): For displaying the output video in the browser.

## 🚀 **How to Run the Application**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/macv-object-tracker.git
   cd macv-object-tracker
   ```

2. **Install Dependencies**: 

   Ensure you have pip installed. Run the following command to install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup the Environment**:

   -Download the YOLO model weights (best.pt) and place them in the models/ directory.
   -Ensure that your video files are placed in the uploads/ directory.

4. **Run the Application**:

   ```bash
   python app.py
   ```

5. **Visit the Application**: 

    Open your browser and go to http://127.0.0.1:5000/ to interact with the application and upload a video for object tracking.

## 📊 **Metrics Calculated**

- **Total Time Each Object Spends**: The total time an object stays within the video frame is tracked and displayed.

- **Total Unique Object IDs**: The number of distinct objects identified and tracked is displayed to show the diversity of objects detected.

##🎥 **Visualizations**

- **Bounding Boxes**: The tracked objects are enclosed within bounding boxes during the video playback.

- **Centroids**: The centroid (center point) of each object is highlighted to track its position.

- **Object Trails**: Each object’s movement is visualized with a trail, showing the path it followed during the video.

##📹 **Output Video**

- After the tracking and annotation process, the video is saved and stored in the **static/results/** directory.
- The processed video can be displayed in a browser by navigating to the results page.

##🧪 **Testing**

Ensure the following functionality works correctly:

- **File Upload**: Test video upload functionality.
- **Object Tracking**: Verify that objects are correctly tracked and annotated in the video.
- **Visualization**: Confirm that bounding boxes, centroids, and trails are displayed correctly.
- **Output Video**: Check that the processed video plays smoothly in a browser.
