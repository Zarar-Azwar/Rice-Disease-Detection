# Rice-Disease-Detection
<img height="80" width="150" src="https://globalaihub.com/wp-content/uploads/2022/03/Google-Colab-Logo-1.png">
<a href="https://colab.research.google.com/drive/1T869Nl0MtFrgdfVa2ypUa_ELCiD6u5tO?usp=sharing">Colab Link</a>
<h4>Results</h4>
<table>
<thead>
<th>Input</th>
<th>Result</th>
</thead>
<tr>
<td>
<img height="300" width="300" src="https://github.com/Zarar-Azwar/Rice-Disease-Detection/blob/main/static/healthy2.jpg">
</td>

<td>
<img height="300" width="300" src="https://github.com/Zarar-Azwar/Rice-Disease-Detection/blob/main/static/1.png">
</td>
</tr>
<tr>
<td>
<img height="300" width="300" src="https://github.com/Zarar-Azwar/Rice-Disease-Detection/blob/main/static/diseased2.jpg">
</td>

<td>
<img height="300" width="300" src="https://github.com/Zarar-Azwar/Rice-Disease-Detection/blob/main/static/2.png">
</td>
</tr>

</table>
# Rice Disease Detection

## 🌾 Detect Healthy vs. Diseased Rice Plants with AI

Rice Disease Detection is a web application that uses deep learning to classify whether an uploaded image of a rice plant is **healthy** or **diseased**. The model is trained on a dataset of rice plant images and leverages **CNN-based deep learning** for classification.

---

## 🚀 Features

- **Deep Learning Model**: Uses **CNN (Convolutional Neural Networks)** for accurate classification of rice plant health.
- **Real-Time Predictions**: Upload an image and get an instant classification as **Healthy** or **Diseased**.
- **Flask Web Application**: Simple and interactive UI for testing images.

---

## 📌 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Rice-Disease-Detection.git
   cd Rice-Disease-Detection
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download or place the trained model** (`riceDisease.h5`) in the project directory.

---

## 🛠 Usage

1. **Run the Flask app**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Upload an image** and click **Submit**.
4. **View the result**, which will classify the image as **Healthy** or **Diseased**.

---

## 📂 Project Structure
```
Rice-Disease-Detection/
│── static/              # Static files (CSS, JS, uploaded images)
│── templates/           # HTML templates for Flask
│── model/               # Pre-trained model (riceDisease.h5)
│── app.py               # Main Flask application
│── requirements.txt     # Python dependencies
│── README.md            # Documentation
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 💡 Future Enhancements
- ✅ Improve accuracy with additional datasets
- ✅ Deploy as a live web application
- ✅ Enhance UI with Bootstrap or React

---

## ✨ Contributors
Developed by **Zarar Azwar Khalid and Shiza Khurram** 🚀
 

---
## 📩 Contact
For inquiries, reach out via [shizakhurram7@gmail.com/zararazwar1@gmail.com].

Ensuring healthier crops with AI! 🌾🔬


