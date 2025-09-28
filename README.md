# Heart Disease Predictor

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)]()
[![Flask](https://img.shields.io/badge/Flask‑web‑framework‑lightgrey.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

A web application to predict the likelihood of heart disease from patient data using a trained ML model.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Architecture](#architecture)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Running Locally](#running-locally)  
4. [Usage](#usage)  
5. [Model Training & Data](#model-training--data)  
6. [Project Structure](#project-structure)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Project Overview

This project provides:

- A machine learning model (e.g. classifier) to predict whether a patient is likely to have heart disease, based on features like age, cholesterol, blood pressure, etc.
- A Flask-based web interface to take input from users and show predictions.
- A backend with database support (if any) to store results or user data (depending on your implementation).
- Templates and static assets to render the UI.

Use case: physicians or users input health metrics and get a prediction.

---

## Architecture

Below is a high-level view of the architecture and data flow:

```mermaid
flowchart LR
  A[User Input (Web Form)] --> B[Flask Backend (app.py)]
  B --> C[Data Preprocessing Module]
  C --> D[ML Model (clf.pkl)]
  D --> E[Prediction Result]
  E --> F[Flask Template Rendering]
  F --> A

  B --> G[Database Layer (database.py)]
  G --> H[Store / Retrieve Records]
```

Alternatively, as ASCII:

```
   +------------------+
   | User (Browser)   |
   +--------+---------+
            |
            v
   +--------+---------+
   | Flask Backend     |
   | (app.py)          |
   +----+-------+------+
        |       |
        |       v
        |   +---+------+
        |   | Database |
        |   +----------+
        v
 +------+------+        +-----------------+
 | Preprocess &  |----->| ML Model (clf)  |
 | Feature Logic |      +-----------------+
 +---------------+
        |
        v
 +---------------+
 | Prediction     |
 +-------+--------+
         |
         v
 +----------------------+
 | Rendered Response UI |
 +----------------------+
```

### Components

- **Web interface / UI**: HTML forms, CSS, and Flask templating (in `templates/` and `static/`).
- **Backend (Flask)**: Handles HTTP requests, input validation, routing, calling model prediction.
- **Preprocessing**: Any scaling, encoding, feature handling done before feeding to the model.
- **ML Model**: The trained classifier stored as `clf.pkl` in the repository.
- **Database (optional)**: e.g. in `database.py` to store user inputs, predictions, logs.
- **Data & Notebooks**: Dataset (`heart.csv`) and Jupyter notebook for experiments.

---

## Getting Started

### Prerequisites

You need:

- Python 3.x  
- `pip`  
- (Optionally) virtual environment tool like `venv` or `conda`  

### Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/Kaustubh01/Heart-Disease-Predictor.git
   cd Heart-Disease-Predictor
   ```

2. (Optional) Create & activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # on macOS / Linux
   venv\Scripts\activate       # on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. Ensure the trained model file `clf.pkl` is present (it is in this repo).  
2. Run the Flask app:

   ```bash
   python app.py
   ```

3. Open your browser at `http://127.0.0.1:5000` (or another host/port if configured).  
4. Use the UI to input patient features and get a prediction.

---

## Usage

- Fill in the form fields (e.g. age, cholesterol, blood pressure, etc.).  
- Submit the form.  
- View the prediction results (e.g. “Heart Disease: Yes / No” or probability).

You can extend or customize this to show probability scores, confidence, or explanation (e.g. SHAP, LIME).

---

## Model Training & Data

- The dataset used is `heart.csv` (provided in `datasets/`).  
- Experiments and model selection have been done in `heart_disease_predictor.ipynb`.  
- The final model is serialized into `clf.pkl`.  

If you want to retrain or improve:

1. Load the CSV in Jupyter, do exploratory data analysis.  
2. Preprocess features (scaling, encoding).  
3. Train multiple classifiers (Logistic Regression, Random Forest, etc.).  
4. Evaluate (cross‑validation, ROC, etc.).  
5. Save the best model using `pickle` or `joblib`.  
6. Replace `clf.pkl` and ensure input feature order matches.

---

## Project Structure

Here is the folder layout with explanation:

```
Heart-Disease-Predictor/
├── app.py                     # Flask app entry point, defines routes, prediction logic
├── database.py                # Database utilities (e.g. storing or retrieving records)
├── clf.pkl                     # Serialized trained ML model
├── hear_disease_predictor.ipynb  # Jupyter notebook for training & analysis
├── heart.csv                   # Dataset
├── requirements.txt            # Python package dependencies
├── templates/                   # Flask HTML templates
│   ├── index.html
│   └── result.html
├── static/                      # Static assets (CSS, JS, images)
│   ├── css/
│   └── js/
├── models/                       # (Optional) you can store alternate models here
└── datasets/                    # (Optional) raw or additional datasets
```

Notes:

- `app.py` handles routing, input validation, and calling prediction logic.  
- `database.py` is optional (depending on whether you store user interactions).  
- Templates folder stores the front-end layout.  
- `clf.pkl` must be consistent with the preprocessing pipeline.

---

## Contributing

Contributions are welcome! Some ideas:

- Add more models (e.g. XGBoost, Neural Networks).  
- Add explainability (SHAP, LIME).  
- Add user authentication and save user history.  
- Improve UI/UX and styling.  
- Deploy to a cloud service (Heroku, AWS, etc.).  

Steps:

1. Fork the repository  
2. Create a new branch: `git checkout -b feature-name`  
3. Make changes & test  
4. Commit changes and push: `git push origin feature-name`  
5. Open a Pull Request  

Please follow proper code style and add documentation.

---

## License

This project is licensed under the **MIT License** — see `LICENSE` for more details.

---

> **Note:** You may want to add badges (build status, coverage) or screenshots of the UI at top for better presentation.