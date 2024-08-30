from keras.models import load_model

# Load the discriminator model
discriminator = load_model('discriminator_model.h5')

# Print the summary of the discriminator model
print("Discriminator Model Summary:")
discriminator.summary()

# Load the generator model
generator = load_model('generator_model.h5')

# Print the summary of the generator model
print("Generator Model Summary:")
generator.summary()
