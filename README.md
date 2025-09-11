# 🏠 Bangalore Home Price Prediction

A Machine Learning web app to predict home prices in Bangalore, built using **Python, Flask, and Scikit-learn**.

## 🚀 Features
- Predicts house price based on:
  - ✅ Area (sqft)  
  - ✅ BHK  
  - ✅ Bathrooms  
  - ✅ Location  
- Interactive web interface built with HTML, CSS, and JavaScript  
- REST API powered by Flask  

## 🖥️ Demo
🔗 [Live Demo](http://ec2-16-171-6-104.eu-north-1.compute.amazonaws.com/)  
💻 [GitHub Repo](https://github.com/Yohannes-Kewani/house-price-regression)

## ⚙️ Tech Stack
- Python, Numpy, Pandas, Scikit-learn  
- Flask (Backend)  
- HTML, CSS, JavaScript (Frontend)  
- Nginx + AWS EC2 (Deployment)  

## ▶️ Run Locally
```bash
# Clone repo
git clone https://github.com/Yohannes-Kewani/house-price-regression.git
cd house-price-regression

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Flask server
python server.py
