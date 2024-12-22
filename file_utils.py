import os
import shutil
import logging
from ultralytics import YOLO
from pathlib import Path

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'mp4', 'avi'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def allowed_mime_type(mime_type):
    ALLOWED_MIME_TYPES = ['image/jpeg', 'image/png', 'video/mp4', 'video/avi']
    return mime_type in ALLOWED_MIME_TYPES
def convert_image(input_path, output_path):
    from PIL import Image
    try:
        img = Image.open(input_path)
        img.save(output_path)
        return output_path
    except Exception as e:
        logging.error(f"Error converting image: {e}")
        return None
def convert_video(input_path, output_path):
    import cv2
    try:
        cap = cv2.VideoCapture(input_path)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break
        cap.release()
        out.release()
        return output_path
    except Exception as e:
        logging.error(f"Error converting video: {e}")
        return None
def yolo_annotate(video_path, model_path, output_dir='static/results'):
    """Annotate a video using YOLOv8 model."""
    try:
        model = YOLO(model_path)
        results = model.track(source=video_path, save=True)
        results.save(save_dir=output_dir)
        logging.info("YOLO annotation completed successfully.")
        return results
    except Exception as e:
        logging.error(f"Error in YOLO annotation: {e}")
        return None
def cleanup_old_files(output_dir='static/results', keep_last_n=5):
    try:
        files = os.listdir(output_dir)
        files = [os.path.join(output_dir,f) for f in files if os.path.isfile(os.path.join(output_dir, f))]
        files.sort(key=os.path.getmtime, reverse=True)
        for file in files[keep_last_n:]:
            os.remove(file)
        logging.info(f"Cleaned up old files, keeping last {keep_last_n} files.")
    except Exception as e:
        logging.error(f"Error cleaning up old files: {e}")
