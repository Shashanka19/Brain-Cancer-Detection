from PIL import Image, ImageOps
import numpy as np
import keras
import os

# Load the trained model with a dynamically set path
model_path = os.path.join(os.getcwd(), r"D:\DS projects\braincancer\app\my_model.keras")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")

model = keras.models.load_model(model_path)

def image_pre(path):
    """Preprocess the image before prediction"""
    print(f"Processing image: {path}")
    size = (150, 150)

    # Open Image
    image = Image.open(path).convert("L")  # Convert to grayscale
    image = ImageOps.fit(image, size, Image.LANCZOS)  # Resize
    image_array = np.asarray(image)

    # Reshape and Normalize
    data = image_array.reshape((-1, 150, 150, 1)).astype(np.float32)
    data = data / 255.0  # Normalize to range [0,1]
    
    return data

def predict(image_path):
    """Predict using the trained model"""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")

    print(f"Received image path: {image_path}")
    data = image_pre(image_path)  # Preprocess image
    prediction = model.predict(data)

    print("Raw Prediction Output:", prediction)

    return float(prediction[0][0])  # Convert output to a readable format
