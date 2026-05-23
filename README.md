# 💰 Census Income Classifier

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136.1-009688.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.57.0-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub Stars](https://img.shields.io/github/stars/kasa-maker/Census-Income-Classifier?style=social)

A machine learning web application that predicts whether an individual's annual income exceeds $50K based on census data. Built with FastAPI backend and Streamlit frontend.

## 🎯 Features

- **Interactive Web Interface**: User-friendly Streamlit frontend for data input
- **RESTful API**: FastAPI backend for model predictions
- **Machine Learning Model**: Pre-trained classifier using census demographic data
- **Docker Support**: Containerized deployment with Docker Compose
- **Real-time Predictions**: Instant income classification based on 14 input features

## 🏗️ Architecture

```
┌─────────────────┐         ┌─────────────────┐
│   Streamlit     │  HTTP   │    FastAPI      │
│   Frontend      │ ──────> │    Backend      │
│   (Port 8501)   │         │   (Port 8000)   │
└─────────────────┘         └─────────────────┘
                                     │
                                     ▼
                            ┌─────────────────┐
                            │  ML Model       │
                            │  (model.pkl)    │
                            └─────────────────┘
```

## 📋 Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional, for containerized deployment)
- Git

## 🚀 Quick Start

### Option 1: Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/kasa-maker/Census-Income-Classifier.git
   cd Census-Income-Classifier
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server**
   ```bash
   uvicorn main:app --reload
   ```
   Backend will run on `http://localhost:8000`

5. **Start the frontend (in a new terminal)**
   ```bash
   streamlit run app.py
   ```
   Frontend will run on `http://localhost:8501`

### Option 2: Docker Deployment

1. **Clone the repository**
   ```bash
   git clone https://github.com/kasa-maker/Census-Income-Classifier.git
   cd Census-Income-Classifier
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: `http://localhost:8501`
   - Backend API: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

## 📊 Input Features

The model uses the following 14 features for prediction:

| Feature | Type | Description |
|---------|------|-------------|
| Age | Integer | Age of the individual |
| Workclass | Categorical | Employment type (Private, Government, Self-employed, etc.) |
| fnlwgt | Integer | Final weight (census sampling weight) |
| Education | Categorical | Highest education level achieved |
| Education-num | Integer | Numeric representation of education level |
| Marital Status | Categorical | Marital status category |
| Occupation | Categorical | Type of occupation |
| Relationship | Categorical | Relationship status |
| Race | Categorical | Race category |
| Gender | Categorical | Male or Female |
| Capital Gain | Integer | Capital gains income |
| Capital Loss | Integer | Capital losses |
| Hours per Week | Integer | Average working hours per week |
| Native Country | Categorical | Country of origin |

## 🔌 API Endpoints

### GET `/`
Health check endpoint
```json
{
  "message": "Adult Income Prediction API is running successfully!"
}
```

### POST `/predict`
Predict income category

**Request Body:**
```json
{
  "age": 30,
  "workclass": "Private",
  "fnlwgt": 200000,
  "education": "Bachelors",
  "education_num": 13,
  "marital_status": "Married-civ-spouse",
  "occupation": "Tech-support",
  "relationship": "Husband",
  "race": "White",
  "gender": "Male",
  "capital_gain": 0,
  "capital_loss": 0,
  "hours_per_week": 40,
  "native_country": "United-States"
}
```

**Response:**
```json
{
  "prediction": ">50K"
}
```

## 🛠️ Technology Stack

- **Backend**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **ML Framework**: Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Containerization**: Docker, Docker Compose

## 📁 Project Structure

```
Census-Income-Classifier/
├── app.py                    # Streamlit frontend
├── main.py                   # FastAPI backend
├── model.pkl                 # Pre-trained ML model
├── requirements.txt          # Python dependencies
├── Dockerfile                # Backend Docker image
├── Dockerfile.streamlit      # Frontend Docker image
├── docker-compose.yml        # Multi-container orchestration
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## 🧪 Testing

1. **Test Backend API**
   ```bash
   curl http://localhost:8000/
   ```

2. **Test Prediction Endpoint**
   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{
          "age": 30,
          "workclass": "Private",
          "fnlwgt": 200000,
          "education": "Bachelors",
          "education_num": 13,
          "marital_status": "Married-civ-spouse",
          "occupation": "Tech-support",
          "relationship": "Husband",
          "race": "White",
          "gender": "Male",
          "capital_gain": 0,
          "capital_loss": 0,
          "hours_per_week": 40,
          "native_country": "United-States"
        }'
   ```

3. **Access Interactive API Docs**
   Visit `http://localhost:8000/docs` for Swagger UI

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**kasa-maker**

- GitHub: [@kasa-maker](https://github.com/kasa-maker)

## 🙏 Acknowledgments

- Dataset: UCI Machine Learning Repository - Adult Income Dataset
- Built with FastAPI and Streamlit frameworks

---

⭐ If you find this project useful, please consider giving it a star!
