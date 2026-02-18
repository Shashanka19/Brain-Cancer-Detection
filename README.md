# Brain Cancer Detection

A deep learning-based web application for detecting brain cancer from medical images using a Convolutional Neural Network (CNN) model.

## 🧠 Overview

This project uses a trained Keras model to analyze brain scan images and predict whether they indicate the presence of brain cancer. The application provides a user-friendly web interface built with Flask for easy image upload and instant predictions.

## ✨ Features

- **Medical Image Analysis**: Upload brain scan images for instant cancer detection
- **Deep Learning Model**: Uses a trained CNN model for accurate predictions
- **Web Interface**: Clean and intuitive Flask-based UI
- **Preprocessing Pipeline**: Automatic image preprocessing (grayscale conversion, resizing, normalization)
- **Real-time Results**: Get instant predictions with visual feedback

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask**: Web framework for the application
- **Keras/TensorFlow**: Deep learning framework for the CNN model
- **PIL (Pillow)**: Image processing
- **NumPy**: Numerical computations

## 📁 Project Structure

```
Brain_Cancer_Detection-main/
├── app.py                 # Flask application main file
├── model.py              # Model loading and prediction logic
├── brainml.ipynb         # Jupyter notebook for model training
├── README.md             # Project documentation
├── static/
│   └── uploads/          # Directory for uploaded images
└── templates/
    └── index.html        # Web interface template
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Brain_Cancer_Detection-main
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install flask keras tensorflow pillow numpy
   ```

4. **Ensure the model file is in place**
   - Place your trained `my_model.keras` file in the appropriate directory
   - Update the model path in `model.py` if needed

## 💻 Usage

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   - Navigate to `http://127.0.0.1:5000/`

3. **Upload an image**
   - Click on the file upload button
   - Select a brain scan image (PNG, JPG, or JPEG format)
   - Click submit to get the prediction

4. **View results**
   - The application will display:
     - Your uploaded image
     - Prediction result: "Brain Cancer" or "No Brain Cancer"

## 🧪 Model Details

- **Input**: 150x150 grayscale images
- **Architecture**: Convolutional Neural Network (CNN)
- **Output**: Binary classification (Cancer/No Cancer)
- **Preprocessing**:
  - Grayscale conversion
  - Image resizing to 150x150 pixels
  - Normalization (pixel values scaled to 0-1 range)

## 📝 How It Works

1. User uploads a brain scan image through the web interface
2. The image is saved to the `static/uploads/` directory
3. The `predict()` function processes the image:
   - Converts to grayscale
   - Resizes to 150x150 pixels
   - Normalizes pixel values
4. The preprocessed image is fed to the trained model
5. Model outputs a probability score
6. Result is displayed: >0.5 = "No Brain Cancer", ≤0.5 = "Brain Cancer"

## ⚠️ Important Notes

- **Medical Disclaimer**: This application is for educational and research purposes only. It should NOT be used as a substitute for professional medical diagnosis or treatment.
- **Supported Formats**: PNG, JPG, JPEG
- **Model Performance**: Accuracy depends on the quality and diversity of training data

## 🔧 Configuration

Update the model path in `model.py` if your model file is located elsewhere:

```python
model_path = os.path.join(os.getcwd(), "path/to/your/model.keras")
```

## 📊 Development

To train your own model:
1. Open `brainml.ipynb` in Jupyter Notebook
2. Follow the notebook cells to train on your dataset
3. Save the trained model as `my_model.keras`
4. Update the model path in `model.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👥 Authors

- Your Name

## 🙏 Acknowledgments

- Dataset providers
- Open source community
- Medical imaging research community

---

**Note**: Always consult with healthcare professionals for medical diagnoses. This tool is intended for research and educational purposes only.