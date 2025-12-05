# 🏠 Immo Eliza: Real Estate Price Predictor

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-green.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success)

## 🚀 Live Demo
**[Click here to view the deployed application](https://immo-eliza-deployment-irwpupzpzdhqplknd6bwwc.streamlit.app)**

## 📖 Description

**Immo Eliza Deployment** is the final stage of the machine learning pipeline for Belgian real estate valuation. This repository contains a fully interactive web application built with **Streamlit** that allows users to estimate the market value of a property in seconds.

The app interfaces with a trained **XGBoost Regressor model**, handling complex preprocessing steps (like location mapping and categorical encoding) behind a user-friendly "Premium" interface.

-----

## ✨ Key Features

* **Premium UI:** A clean, dashboard-style layout with a hero header, toggle switches, and grouped input containers.
* **Smart Location Mapping:** Automatically detects and maps Belgian **Zip Codes** to their corresponding **Provinces** to match the model's training data.
* **Intelligent Preprocessing:**
    * Handles **Case Sensitivity** (e.g., mapping "Villa" to "villa").
    * Maps UI labels (e.g., "Hyper Equipped") to the model's expected technical terms.
    * Real-time input validation.
* **Instant Valuation:** Provides a price prediction in milliseconds using a serialized ML model.

-----

## 📦 Repository Structure

```text
immo-eliza-deployment/
├── streamlit/
│   ├── artifacts/
│   │   ├── model.pkl        # Trained XGBoost model
│   │   └── features.pkl     # List of model feature columns
│   ├── app.py               # Main application logic
│   └── requirements.txt     # Dependencies for the cloud environment
└── README.md
```

-----

## 🛠️ Installation & Local Usage
If you want to run this application on your own machine:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Fred-git121/immo-eliza-deployment.git
    cd immo-eliza-deployment
   ```
   
2. **Install dependencies:**

    ```bash
    pip install -r streamlit/requirements.txt
    ```
   
3. **Run the App:**

    ```bash
    streamlit run streamlit/app.py
    ```
   
4. **View:** The app will open automatically in your browser at http://localhost:8501.

-----

## 🧠 Model Information
The underlying model is a XGBoost Regressor trained on a dataset of Belgian real estate properties.

* **Target:** Price (€)

* **Performance:** R 
2
  Score ~0.71 (on test set)

* **Key Features:**

    * **Location:** Province (derived from Zip Code)

    * **Property Type:** 30+ distinct types (Villa, Apartment, Mansion, etc.)

    * **Condition:** Building state (New, Good, To Renovate, etc.)

    * **Specs:** Living area, bedrooms, kitchen equipment.

    * **Amenities:** Garden, Terrace, Swimming Pool.

-----

## ⚠️ Note on Artifacts
To run this app, the model.pkl and features.pkl files must be present in the streamlit/artifacts/ folder.

* If you are forking this repo: You will need to generate your own model using the training scripts from the immo-eliza-ml project and place the artifacts in the correct folder.

-----

## 🤝 Contributors
[Frédéric Delville](https://github.com/Fred-git121) - Solo Project

This project is part of the BeCode AI Bootcamp.
