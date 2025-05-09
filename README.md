# CEFR Seviye Tahmin Sistemi

![CEFR](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/CEFR_Levels.svg/320px-CEFR_Levels.svg.png)

Bu proje, verilen bir İngilizce cümlenin **CEFR (Common European Framework of Reference for Languages)** seviyesini (A1, A2, B1, B2, C1, C2) tahmin etmek için geliştirilmiş bir **makine öğrenmesi modelidir**. Bu sistem, dil seviyelerini belirlemek için çeşitli sınıflandırma algoritmalarını kullanır ve kullanıcıya sonuçları sunar.

## Proje Özeti

Bu sistem, İngilizce cümleleri analiz eder ve aşağıdaki CEFR seviyelerinden birini tahmin eder:
- **A1**: Temel düzey
- **A2**: Temel seviye
- **B1**: Orta seviye
- **B2**: Orta üstü seviye
- **C1**: İleri seviye
- **C2**: Mükemmel seviye

### Proje Adımları:
1. **Veri Hazırlığı ve Ön İşleme**: İngilizce cümleler üzerinde metin ön işleme adımları (küçük harfe çevirme, noktalama işaretlerini kaldırma, stopwords temizleme, lemmatization) uygulanır.
2. **Model Eğitimi**: Farklı sınıflandırma algoritmaları (SVM, Random Forest, Naive Bayes, Neural Network) kullanılarak model eğitilir.
3. **Model Değerlendirme**: Modelin performansı test verileriyle değerlendirilir.
4. **Model Kaydetme**: En iyi model kaydedilir ve tekrar kullanılabilir hale getirilir.
5. **Tahmin Fonksiyonu**: Kullanıcıdan alınan cümle ile tahmin yapılır.

---

## Kullanılan Teknolojiler

- **Python 3.x**: Python programlama dili.
- **Scikit-learn**: Makine öğrenmesi için.
- **NLTK**: Doğal dil işleme (stopwords, lemmatization).
- **Joblib**: Modelin kaydedilmesi ve yüklenmesi.
- **Matplotlib** & **Seaborn**: Veri görselleştirme için.
- **WordCloud**: Kelime bulutları oluşturmak için.
- **Tkinter**: GUI uygulaması için.

---

