# Real_time_survill

**Real_time_survill** is a real-time surveillance system that leverages deep learning techniques to detect and classify violent activities in video streams. By utilizing LSTM-based neural networks, the system can analyze temporal patterns in video data to identify potential threats, enhancing security measures in various environments.

## Features

- **Real-Time Video Analysis**: Processes live video feeds to detect violent activities as they occur.
- **Deep Learning Models**: Employs pre-trained LSTM models for accurate activity recognition.
- **Customizable Thresholds**: Allows users to set sensitivity levels for activity detection.
- **Alert System**: Generates alerts when violent activities are detected.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shark4real/Real_time_survill.git
   cd Real_time_survill
   ```


2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```


3. **Download Pre-trained Models**:
   Place the necessary `.h5` model files (`lstm-model.h5`, `lstm-violence-detection.h5`, etc.) in the project directory.

## Usage

To start the surveillance system, run:


```bash
python app.py
```


This will initiate the video stream analysis. The system will process each frame and display alerts if violent activities are detected.

## Project Structure

- `app.py`: Main application file to run the surveillance system.
- `finalworking.py`: Contains the core logic for video processing and activity detection.
- `train.py` & `train2.py`: Scripts used for training the LSTM models.
- `postdatagen.py`: Generates data for post-processing and analysis.
- `*.h5`: Pre-trained model files used for activity recognition.
- `requirements.txt`: List of Python dependencies required to run the project.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.

---

For more details, visit the [GitHub repository](https://github.com/shark4real/Real_time_survill). 
