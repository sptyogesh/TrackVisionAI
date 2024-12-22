import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from file_utils import allowed_file, allowed_mime_type, convert_image, convert_video, yolo_annotate
import logging
from pathlib import Path

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'mp4', 'avi'}
app.config['RESULTS_FOLDER'] = 'static/results'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        if filename.lower().endswith(('mp4', 'avi')):
            model_path = 'models/best.pt'
            results = yolo_annotate(file_path, model_path, output_dir=app.config['RESULTS_FOLDER'])
            if results:
                return jsonify({"message": "Video annotated successfully", "results": str(results)}), 200
            else:
                return jsonify({"error": "Error in YOLO annotation"}), 500
        if filename.lower().endswith(('jpg', 'jpeg', 'png')):
            output_path = os.path.join(app.config['RESULTS_FOLDER'], filename)
            if convert_image(file_path, output_path):
                return jsonify({"message": "Image converted successfully", "output_path": output_path}), 200
    return jsonify({"error": "File type not allowed"}), 400
@app.route('/cleanup', methods=['POST'])
def cleanup():
    try:
        cleanup_old_files(app.config['RESULTS_FOLDER'], keep_last_n=5)
        return jsonify({"message": "Old files cleaned up successfully"}), 200
    except Exception as e:
        logging.error(f"Error cleaning up files: {e}")
        return jsonify({"error": f"Error cleaning up files: {e}"}), 500
if __name__ == '__main__':
    Path(app.config['UPLOAD_FOLDER']).mkdir(parents=True, exist_ok=True)
    Path(app.config['RESULTS_FOLDER']).mkdir(parents=True, exist_ok=True)
    app.run(debug=True)
