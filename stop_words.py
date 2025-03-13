import nltk

from nltk.corpus import stopwords

nltk.data.path.append(r"D:\nlp_learning\btkAkademiNLP\nltk_data")  # Özel klasör yolu
# Farklı dillerde en çok kullanılan stopwords içeren veri seti
nltk.download("stopwords", download_dir=r"D:\nlp_learning\btkAkademiNLP\nltk_data")

# İngilizce stop words analizi (with nltk)
stopwords.words('english')
stop_words_english = set(stopwords.words('english'))
print(stop_words_english)

text = "There are some examples of handling stop words from some texts."

text_list = text.split()
print(text_list)

# Eğer word ingilizce stop words listesinde yoksa,
# bu kelimeyi filtrelenmiş listeye ekliyoruz.
filtered_words = [word for word in text_list if word.lower() not in stop_words_english]
print(f"filtered_words: {filtered_words}")



# %%Türkçe stop words analizi (with nltk)

stop_words_tr = set(stopwords.words('turkish'))
print(stop_words_tr)

# Örnek Türkçe metin
metin = "merhaba arkadaşlar çok güzel bir ders işliyoruz. Bu ders faydalı mı?"
metin_list = metin.split()
print(metin_list)
filtered_words_tr = [word for word in metin_list if word.lower() not in stop_words_tr]
print(f"filtered_words_tr: {filtered_words_tr}")

# %% Kütüphanesiz stop words çıkarımı (filtrelenmesi)

# Stop word listesi oluştur
tr_stopwords = ["için", "bu", "ile", "mu", "mi", "özel"]

# Örnek Türkçe metin
metin= "Bu bir denemedir. Amacımız bu metinde bulunan özel karaterleri elemek mi acaba?"

filtered_words = [word for word in metin.split() if word.lower() not in tr_stopwords]
print(f"filtered_words: {filtered_words}")
filtered_stopwords_tr = set([word.lower() for word in metin.split() if word.lower() in tr_stopwords])
print(f"filtered_words_tr: {filtered_stopwords_tr}")

