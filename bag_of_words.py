# Count Vectorizer İçeriye Aktar
from sklearn.feature_extraction.text import CountVectorizer

# Veri Seti Oluştur
documents = [
    "kedi bahçede",
    "kedi evde"
]

# vectorizer tanımla
vectorizer = CountVectorizer()

# Metini Sayısal Vektörlere Çevir
X= vectorizer.fit_transform(documents)

# Kelime Kümesi Oluşturma
feature_names = vectorizer.get_feature_names_out()
print(f"Kelimeler: {feature_names}")

# Vektör Temsili
vector_temsili = X.toarray()
print(f"Vektör Temsili: {vector_temsili}")
