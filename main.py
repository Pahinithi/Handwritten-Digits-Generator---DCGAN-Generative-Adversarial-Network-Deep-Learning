import numpy as np
import io
from flask import Flask, render_template, send_file
from keras.models import load_model
from PIL import Image

app = Flask(__name__)

# Load the correct generator model
generator = load_model('discriminator_model.h5')

def generate_digit_image():
    # Generate random noise with the shape (1, 100)
    noise = np.random.normal(0, 1, (1, 100))
    
    # Generate image using the generator model
    generated_image = generator.predict(noise)
    
    # Rescale the image to [0, 255] and clip values to be in valid range
    generated_image = (generated_image * 127.5 + 127.5).astype(np.uint8)
    
    # Reshape the output image to (28, 28, 1) and squeeze to (28, 28)
    generated_image = generated_image.reshape(28, 28)
    
    # Convert to PIL Image
    image = Image.fromarray(generated_image)
    
    # Save image to a bytes buffer
    buf = io.BytesIO()
    image.save(buf, format='PNG')
    buf.seek(0)
    
    return buf

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    image_buffer = generate_digit_image()
    return send_file(image_buffer, mimetype='image/png', as_attachment=False, attachment_filename='generated_digit.png')

if __name__ == '__main__':
    app.run(debug=True)
