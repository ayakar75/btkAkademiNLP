
import nltk # natural language toolkit

nltk.data.path.append(r"C:\nlp_learning\btkAkademiNLP\nltk_data")  # Özel klasör yolu
nltk.download("punkt", download_dir=r"C:\nlp_learning\btkAkademiNLP\nltk_data")
nltk.download("punkt_tab", download_dir=r"C:\nlp_learning\btkAkademiNLP\nltk_data")

text = "Hello, World! How are you? Hello, hi ..."

# Kelime tokenizasyonu: word_tokenize: metni kelimelere ayırır,
# # noktalama işaretleri ve boşluklar ayrı birer token olarak elde edilecektir.
word_tokens = nltk.word_tokenize(text)
print(word_tokens)


# Cümle tokenizasyonu: sent_tokenize: metni cümlelere ayırır. Her bir cümle bir toke olur.
