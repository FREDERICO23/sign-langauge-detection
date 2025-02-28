# recognition/views.py
import os
import numpy as np
import base64
from io import BytesIO
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from PIL import Image
import tensorflow as tf

from .models import SignImage

# Load the model
MODEL_PATH = os.path.join(settings.STATIC_ROOT, 'model', 'sign_language_model.h5')

def load_model():
    """Load the TensorFlow model if available, otherwise return None"""
    if os.path.exists(MODEL_PATH):
        return tf.keras.models.load_model(MODEL_PATH)
    return None

def index(request):
    """Home page view"""
    return render(request, 'index.html')

def recognize_sign(request):
    """Process uploaded image and make prediction"""
    if request.method == 'POST' and request.FILES.get('sign_image'):
        # Save the uploaded image
        image_file = request.FILES['sign_image']
        sign_image = SignImage(image=image_file)
        sign_image.save()
        
        # Load the image and preprocess it
        img = Image.open(sign_image.image.path).convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to model input size
        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = img_array.reshape(1, 28, 28, 1)  # Reshape for model
        
        # Create a base64 encoded version of the image for display
        buffered = BytesIO()
        Image.open(sign_image.image.path).save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        img_base64 = f"data:image/jpeg;base64,{img_str}"
        
        # Load the model and make prediction
        model = load_model()
        
        # Default values in case model isn't loaded
        predicted_letter = "?"
        confidence = 0.0
        
        if model:
            # Make prediction
            prediction = model.predict(img_array)
            predicted_label = np.argmax(prediction)
            confidence = float(np.max(prediction))
            
            # Convert numeric label to letter (A=0, B=1, etc.)
            # Note: J and Z are not in the dataset as they require motion
            predicted_letter = chr(65 + predicted_label)
            
            # Handle J and Z (which aren't in the dataset)
            if predicted_letter in ['J', 'Z']:
                predicted_letter = f"{predicted_letter}*"
        
        context = {
            'sign_image': sign_image,
            'img_base64': img_base64,  # Add base64 encoded image
            'predicted_letter': predicted_letter,
            'confidence': confidence * 100,  # Convert to percentage
            'model_loaded': model is not None,
        }
        
        return render(request, 'result.html', context)
    
    return redirect('recognition:index')