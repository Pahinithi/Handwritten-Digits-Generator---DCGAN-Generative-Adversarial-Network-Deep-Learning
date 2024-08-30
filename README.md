# Handwritten Digit Generator - DCGAN

This project uses a Deep Convolutional Generative Adversarial Network (DCGAN) to generate random handwritten digits. The generator model creates images based on random noise, and the Flask web application allows users to generate and view these digits.

## Features

- **Generate Handwritten Digits**: Click a button to generate a new random handwritten digit.
- **Beautiful UI/UX**: Unique and visually appealing design with Bootstrap and custom styles.
- **Image Display**: View the generated digit directly on the webpage.

## Technologies Used

- **Backend**: Flask
- **Deep Learning**: Keras
- **Frontend**: HTML, Bootstrap
- **Python Libraries**: NumPy, PIL, io

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Pahinithi/Handwritten-Digits-Generator---DCGAN-Generative-Adversarial-Network-Deep-Learning
   cd Handwritten-Digits-Generator-DCGAN
   ```

2. **Install Dependencies**

   Create a virtual environment and install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Download Model Files**

   Ensure you have the model files (`generator_model.h5` and `discriminator_model.h5`) in the project directory. If not, download or train the models and place them in the root directory.

4. **Run the Flask Application**

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. Open your browser and navigate to `http://127.0.0.1:5000/`.
2. Click the "Generate Digit" button to create a new handwritten digit.
3. The generated digit will be displayed below the button.

## Screenshots

<img width="1728" alt="DL11" src="https://github.com/user-attachments/assets/7d2988c2-58db-4e96-a160-8dc3801f3b87">


## Troubleshooting

- **FileNotFoundError**: Ensure that `generator_model.h5` and `discriminator_model.h5` are in the project directory and correctly named.
- **ModuleNotFoundError**: Install missing Python packages using `pip install -r requirements.txt`.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License

## Contact

Developed by Nithilan. For questions or support, please contact me at [nithilan32@gmail.com](mailto:nithilan32@gmail.com).
