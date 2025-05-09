# ✨ CEFR Level Prediction System 📊🧠

This project is a machine learning system that **predicts the CEFR (Common European Framework of Reference for Languages)** level of English sentences (**A1, A2, B1, B2, C1, C2**).  
It was developed entirely using a **custom-trained model** created from scratch using NLP and classification algorithms.

---

## 🧩 Project Workflow

🔍 **1. Data Preprocessing**  
• Converted text to lowercase  
• Removed punctuation, digits, and English stopwords  
• Applied lemmatization

🧠 **2. Model Training**  
• Trained and tested 4 different classifiers:  
  - SVM  
  - Random Forest  
  - Naive Bayes  
  - Neural Network  

📊 **3. Model Evaluation**  
• Compared models using precision, recall, and F1-score  
• Selected the best performing model  

💾 **4. Model Saving**  
• Saved the model, vectorizer, and label encoder with `joblib`  

🗣️ **5. Prediction Interface**  
• Allows users to input an English sentence to predict its CEFR level  
• Works via the command line interface (CLI)

---

## 🔧 Technologies and Libraries Used

| Purpose              | Library        |
|----------------------|----------------|
| 👨‍💻 Programming     | Python 3.x     |
| 🧹 Text Processing   | NLTK           |
| 🤖 Machine Learning  | Scikit-learn   |
| 📁 Model Saving      | Joblib         |
| 📊 Visualization     | Matplotlib, Seaborn |
| ☁️ Word Cloud        | WordCloud      |
| 🖼️ Optional UI       | Tkinter        |

----------------------------------------------------------------------------------------
[TR]
# ✨ CEFR Seviye Tahmin Sistemi 📊🧠

Bu proje, **İngilizce cümlelerin CEFR (Common European Framework of Reference for Languages)** seviyesini (**A1, A2, B1, B2, C1, C2**) tahmin etmek için tamamen **kendi oluşturduğum bir modelle** geliştirilmiştir. Makine öğrenmesi ve doğal dil işleme (NLP) teknikleriyle, cümlelerin hangi seviyeye ait olduğunu tahmin edebilen bir sistemdir.

---

## 🧩 Proje Adımları

🔍 **1. Veri Hazırlığı ve Ön İşleme**  
• Metinler küçük harfe çevrildi  
• Noktalama işaretleri, sayılar ve durak kelimeler (stopwords) kaldırıldı  
• Lemmatization uygulandı

🧠 **2. Model Eğitimi**  
• 4 farklı sınıflandırma algoritması denendi:  
  - SVM  
  - Random Forest  
  - Naive Bayes  
  - Neural Network  

📊 **3. Model Değerlendirme**  
• Modeller precision, recall ve f1-score gibi metriklerle değerlendirildi  
• En iyi performansı gösteren model seçildi  

💾 **4. Modeli Kaydetme**  
• `joblib` ile model, vektörleştirici ve etiketleyici dosya olarak kaydedildi  

🗣️ **5. Tahmin Fonksiyonu ve Arayüz**  
• Kullanıcının yazdığı İngilizce cümleler analiz edilerek seviyeleri tahmin edilir  
• Komut satırından kullanılabilir hale getirildi  

---

## 🔧 Kullanılan Teknolojiler ve Kütüphaneler

| Amaç | Kütüphane |
|------|-----------|
| 👨‍💻 Programlama | Python 3.x |
| 🧹 NLP | NLTK |
| 🤖 Makine Öğrenmesi | Scikit-learn |
| 📁 Model Kaydetme | Joblib |
| 📊 Görselleştirme | Matplotlib, Seaborn |
| ☁️ Kelime Bulutu | WordCloud |
| 🖼️ GUI (İsteğe Bağlı) | Tkinter |
