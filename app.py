import joblib
import numpy as np
from pywebio.input import input
from pywebio.output import put_text, put_markdown, put_error
from pywebio import start_server

# Model yükleme
def load_my_model():
    model = joblib.load('my_cefr_model.pkl')
    tfidf = joblib.load('my_tfidf_vectorizer.pkl')
    le = joblib.load('my_label_encoder.pkl')
    return model, tfidf, le

# Ön işleme
def preprocess_text(text):
    return text.lower().strip()

# Tahmin
def predict_with_my_model(sentence, model, tfidf, le):
    processed = preprocess_text(sentence)
    vector = tfidf.transform([processed])
    prediction = model.predict(vector)
    proba = model.predict_proba(vector)[0]
    return le.inverse_transform(prediction)[0], {level: prob for level, prob in zip(le.classes_, proba)}

# Ana fonksiyon
def main():
    put_markdown("# 🧠 CEFR Seviye Tahmin Sistemi")
    
    while True:
        # Kullanıcıdan cümle al
        sentence = input("İngilizce bir cümle girin:")
        if not sentence:
            break  # Boş cümle girilirse döngü durur

        try:
            # Model ve verilerle tahmin yap
            level, probabilities = predict_with_my_model(sentence, model, tfidf, le)
            
            put_text(f"🎯 Tahmin Edilen Seviye: {level}")
            put_markdown("**Olasılıklar:**")
            
            for lvl, prob in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
                put_text(f"{lvl}: %{prob * 100:.2f}")
        
        except Exception as e:
            put_error(f"Tahmin sırasında hata oluştu: {str(e)}")
            break  # Hata alındığında döngü durur

# Model ve yardımcıları yükle
try:
    model, tfidf, le = load_my_model()
except Exception as e:
    put_error(f"Model veya vektörizer dosyaları yüklenemedi:\n{str(e)}")
    start_server(main, port=8080, debug=True)
    exit()

# Web uygulamasını çalıştır
start_server(main, port=8080, debug=True)
