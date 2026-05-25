import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

# Load the pre-trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'trained_model', 'trained_model.keras')
try:
    model = load_model(MODEL_PATH)
    st.success(f"Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define class labels
labels = {
    0: "T-shirt/top", 1: "Trouser", 2: "Pullover", 3: "Dress", 4: "Coat",
    5: "Sandal", 6: "Shirt", 7: "Sneaker", 8: "Bag", 9: "Ankle Boot"
}

# Function to preprocess the image
def preprocess_image(image):
    try:
        # Convert to grayscale if not already
        if image.mode != 'L':
            image = image.convert('L')

        # Resize to 28x28
        image = image.resize((28, 28))

        # Convert to numpy array and normalize
        image_array = np.array(image).astype('float32') / 255.0

        # Reshape for model input (add batch and channel dimensions)
        image_array = image_array.reshape(1, 28, 28, 1)

        return image_array
    except Exception as e:
        raise ValueError(f"Error processing image: {e}")

# Streamlit app layout
st.title("Fashion MNIST Image Classifier")
st.write("Upload a 28x28 grayscale image (PNG or JPG) to classify it into one of the 10 fashion categories.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        # Open the image
        image = Image.open(uploaded_file)
        
        # Preprocess and Predict
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions[0])
        
        # Define 3 columns: [Image, Spacer, Chart]
        # The numbers [4, 1, 5] represents the relative width of each column
        col1, spacer, col2 = st.columns([4, 1, 5])

        with col1:
            # Display the uploaded image
            st.subheader("Uploaded Image")
            st.image(image, use_column_width=True)
            
            # Display result text below image in standard format
            st.write("**Prediction:**")
            st.write( f"**{labels[predicted_class]}**")

        with col2:
            # Display confidence bar chart
            st.subheader("Confidence")
            prob_dict = {labels[i]: float(predictions[0][i]) for i in range(10)}
            st.bar_chart(prob_dict)

    except ValueError as ve:
        st.error(f"Invalid image: {ve}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload an image to get started.")
