# Fake News Detection using Machine Learning

## 📌 Project Overview

This project is a **Fake News Detection system** that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) and Machine Learning techniques. The model is deployed as a **web application using Streamlit**, allowing users to input news text and get instant predictions.

---

## 🧠 Problem Statement

With the rapid spread of misinformation online, identifying fake news has become a critical challenge. This project aims to build an automated system that can accurately detect fake news articles based on their textual content.

---

## 📊 Dataset

* **Source:** Kaggle Fake News Dataset
* **Content:** Labeled news articles (Real / Fake)
* **Preprocessing:**

  * Text cleaning
  * Removal of stopwords
  * TF-IDF vectorization

---

## ⚙️ Technology Stack

* **Programming Language:** Python
* **Libraries:**

  * Scikit-learn
  * Pandas
  * NumPy
  * Joblib
  * Streamlit
* **Model:** Logistic Regression
* **Vectorization:** TF-IDF

---

## 🚀 Model Training & Performance

* Algorithm: Logistic Regression
* Feature Extraction: TF-IDF Vectorizer
* Train-Test Split: 80:20
* **Accuracy Achieved:** ~94%

---

## 🌐 Web Application (Streamlit)

### Features:

* User-friendly interface
* Accepts custom news article input
* Displays prediction as **Real** or **Fake**
* Shows dataset and model accuracy information

---

## 🗂️ Project Structure

```
├── app.py                 # Streamlit application
├── app.ipynb              # Model training notebook
├── vectorizer.jb          # Saved TF-IDF vectorizer
├── lr_model.jb            # Trained Logistic Regression model
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## ▶️ How to Run the Project

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```
4. Open the browser and test news articles

---

## 📈 Outcome

The system successfully classifies news articles with high accuracy and demonstrates the effective use of NLP and machine learning for real-world misinformation detection.

---
<img width="1918" height="965" alt="image" src="https://github.com/user-attachments/assets/f1f80676-f3d1-4b27-ba49-49d4a4c02e6b" />

## 🔮 Future Enhancements

* Add confidence score for predictions
* Compare multiple ML models
* Deploy using cloud platforms
* Extend to multilingual fake news detection

---

## 👨‍💻 Author

**Siva Kumar**

---

⭐ This project is suitable for **BTech placements and ML interviews**.
