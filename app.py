from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)
process = None  # Global variable to store the subprocess

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-detection', methods=['POST'])
def run_detection():
    global process
    try:
        if process and process.poll() is None:
            return jsonify({'status': 'running', 'message': 'Detection is already running.'})
        
        # Replace with your actual script or function to run the ML model
        process = subprocess.Popen(['python', 'finalworking.py'])
        return jsonify({'status': 'success', 'message': 'Detection started!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/stop-detection', methods=['POST'])
def stop_detection():
    global process
    try:
        if process and process.poll() is None:
            process.terminate()  # Stop the process
            process.wait()
            return jsonify({'status': 'success', 'message': 'Detection stopped!'})
        return jsonify({'status': 'error', 'message': 'No detection process is running.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
