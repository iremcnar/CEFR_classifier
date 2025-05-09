# CEFR Seviye Tahmin Sistemi 🎓🌍

Bu proje, verilen bir İngilizce cümlenin **CEFR (Common European Framework of Reference for Languages)** seviyesini (A1, A2, B1, B2, C1, C2) tahmin etmek için geliştirilmiş bir modeldir. 💻🔍 Model, farklı makine öğrenmesi algoritmaları kullanarak cümlenin CEFR seviyesini belirler. 🧠💡

---

## Proje Özeti 📋

Bu sistem, İngilizce cümleleri analiz eder ve belirli bir dil seviyesi tahmin eder. Proje şu adımlardan oluşmaktadır:

1. **Veri Hazırlığı ve Ön İşleme** 🧹: İngilizce cümleler üzerinde metin ön işleme adımları uygulanır (küçük harfe çevirme, noktalama işaretlerini kaldırma, stopwords temizleme, lemmatization).
2. **Model Eğitimi** 🤖: **CEFR seviyelerini** tahmin etmek için farklı sınıflandırma algoritmaları (SVM, Random Forest, Naive Bayes, Neural Network) kullanılır.
3. **Model Değerlendirme ve Kaydetme** 🏆: Eğitilen modeller, test verisi üzerinde değerlendirilir ve **en iyi performans gösteren model** kaydedilir.
4. **Tahmin Fonksiyonu** 🔮: Kullanıcıdan alınan İngilizce cümleye göre tahmin yapmak için bir fonksiyon yazılır.
5. **GUI veya Komut Satırı Kullanımı** 🖥️: Kullanıcılar, terminal veya GUI üzerinden tahmin yapabilirler.

---

## Kullanılan Teknolojiler 🔧

- **Python 3.x** 🐍
- **Scikit-learn**: Model eğitimi ve vektörleştirme için.
- **NLTK**: Doğal dil işleme için (stopwords, lemmatization).
- **Joblib**: Modelin ve diğer gerekli dosyaların kaydedilmesi ve yüklenmesi.
- **Matplotlib & Seaborn**: Veriyi görselleştirmek ve analiz etmek için.
- **WordCloud**: Kelime bulutları oluşturmak için.
- **Tkinter**: GUI uygulaması için (isteğe bağlı).
















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
