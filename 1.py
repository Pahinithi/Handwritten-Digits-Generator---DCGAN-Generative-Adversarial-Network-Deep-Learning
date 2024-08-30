from keras.models import load_model, save_model

# Load the discriminator model
discriminator = load_model('discriminator_model.h5')
print("Discriminator Model Summary:")
discriminator.summary()

# Load the generator model
try:
    generator = load_model('generator_model.h5')
    print("Generator Model Summary:")
    generator.summary()
except FileNotFoundError as e:
    print(f"Error loading generator model: {e}")

# If generator model is not loaded, this block will not execute
if 'generator' in locals():
    try:
        generator.save('generator_model.h5')  # Save the generator model
        print("Generator model saved successfully.")
    except Exception as e:
        print(f"Error saving generator model: {e}")
