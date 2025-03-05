import nltk

#%% Download data
nltk.data.path.append(r"D:\nlp_learning\btkAkademiNLP\nltk_data")  # Özel klasör yolu
#wordnet: lemmatization işlemi için gerekli veritabanı
nltk.download("wordnet", download_dir=r"D:\nlp_learning\btkAkademiNLP\nltk_data")

#%% Stemming
from nltk.stem import PorterStemmer  # Stemming için fonksiyon

# porter stemmer nesnesini oluştur
stemmer = PorterStemmer()
words = ["running", "runner", "ran", "runs", "better", "go", "went"]

# Kelimelerin stem'lerini buluyoruz, bunu yaparken de porter stemmerin stem() fonksiyonunu kullanıyoruz
stems = [stemmer.stem(w) for w in words]
print(f"stems: {stems}")

# %% Lemmatization
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running", "runner", "ran", "runs", "better", "go", "went"]
lemmas = [lemmatizer.lemmatize(w, pos="v") for w in words]
print(f"lemmas: {lemmas}")
