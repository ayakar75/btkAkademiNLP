# import libraries
import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import re
from collections import Counter

# %% veri setinin içeriye aktarılması
df = pd.read_csv("./data/IMDB Dataset.csv")

# metin verilerini alalım
documents = df["review"]
labels = df["sentiment"]


# %% metin temizleme
def clean_text(text):
    #büyük küçük harf çevrimi
    text = text.lower()
    #rakamları temizleme
    text = re.sub(r"\d+", "", text)
    #özel karakterlerin kaldırılması
    text = re.sub(r"[^\w\s]", "", text)
    #kısa kelimelerin temizlenmesi
    text = " ".join([word for word in text.split() if len(word) > 2])

    return text  #temizlenmiş text'i return et


# metinleri temizle
cleaned_doc = [clean_text(row) for row in documents]
print("Cleaned documents:", cleaned_doc)

#%% stopwords kelimelerini temizleme
# NLTK'nin veri yolunu ekle
nltk.data.path.append(r"D:\nlp_learning\btkAkademiNLP\nltk_data")

# Stop words listesini yükle
stop_words = set(stopwords.words('english'))


def stop_words_cleaner(text):
    """Metindeki stopwords'leri temizler."""
    # Tokenize et (kelimelere ayır)
    words = nltk.word_tokenize(text)

    # Stopwords'leri çıkar
    filtered_words = [word for word in words if word.lower() not in stop_words]

    return " ".join(filtered_words)  # Kelimeleri tekrar birleştir


# Tüm dökümanlar için stopwords temizleme
filtered_documents = [stop_words_cleaner(doc) for doc in documents]
cleaned_doc = filtered_documents
print("Filtered documents:", filtered_documents)

# %% Bag Of Words


# vectorizer tanımla
vectorizer = CountVectorizer()

# metin --> sayısal hale getir
X = vectorizer.fit_transform(cleaned_doc[:75])  # 75 adedini yapıyoruz

# kelime kümesi göster
feature_names = vectorizer.get_feature_names_out()

# vektör temsili göster
vertor_temsili2 = X.toarray()
print(f"Vektör Temsili:{vertor_temsili2}")

df_bow = pd.DataFrame(vertor_temsili2, columns=feature_names)

# kelime frekanslarını göster
word_counts = X.sum(axis=0).A1
word_freq = dict(zip(feature_names, word_counts))

# %% İlk 5 kelimeyi print ettir

most_common_five_words = Counter(word_freq).most_common(5)
print(f"most_common_five_words: {most_common_five_words}")
