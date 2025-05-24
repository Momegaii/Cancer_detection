# Lung Cancer Prediction Project

This project is designed to predict the likelihood of lung cancer based on user input. It utilizes machine learning models to analyze various health indicators and provide predictions.

## Project Structure

```
Lung_cancer
├── main.py          # Main logic for lung cancer prediction
├── utilies.py       # Utility functions for data processing and model handling
├── models
│   ├── model.pkl    # Serialized machine learning model for prediction
│   └── model2.pkl   # Another serialized model for prediction
├── requirements.txt  # List of dependencies for the project
└── README.md        # Documentation for the project
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Lung_cancer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:
   ```
   python main.py
   ```

2. Follow the prompts to enter the required health indicators:
   - Age
   - Smoking status (1 for yes, 0 for no)
   - Chronic cough (1 for yes, 0 for no)
   - Shortness of breath (1 for yes, 0 for no)
   - Fatigue (1 for yes, 0 for no)
   - Weight loss (1 for yes, 0 for no)

3. The application will provide predictions based on the input data.

## Models

The project uses two machine learning models stored in the `models` directory. These models are trained to predict lung cancer based on the input features provided by the user.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.