# Metinlerde bulunan fazla boşlukları ortadan kaldır.

text = "HeLLo,     World!     2035"

"""
text.split()
Out[2]: ['HeLLo', 'World!', '2035']
"""
cleaned_text = ' '.join(text.split())
print(f"text: {text} \ncleaned_text: {cleaned_text}")

# %% büyük -> küçük harf çevrimi
text = "HeLLo, World! 2035"
cleaned_text2 = text.lower()  # küçük harfe çevir
print(f"text: {text} \ncleaned_text2: {cleaned_text2}")

# %% noktalama işaretlerini kaldır

import string

text = "HeLLo, World! 2035"
cleaned_text3 = text.translate(str.maketrans('', '', string.punctuation))
print(f"text: {text} \ncleaned_text3: {cleaned_text3}")

# %% özel karakterleri kaldır, %,@, /, *, #

import re

text = "HeLLo, World! 2035%"

cleaned_text4 = re.sub(r'[^A-Za-z0-9\s]', '', text)
print(f"text: {text} \ncleaned_text4: {cleaned_text4}")

# %% yazım hatalarını düzelt
from textblob import TextBlob  # metin analizlerinde kullanılan bir kütüphane

text = "Hellıo, Wirld! 2035"

cleaned_text5 = TextBlob(text).correct()  # correct: yazım hatalarını düzeltir
print(f"text: {text} \ncleaned_text5: {cleaned_text5}")

# %% html ya da url etiketlerini kaldır
from bs4 import BeautifulSoup
html_text = "<div>Hello, World! 2035</div>" # html etiketi var
cleaned_text6 = BeautifulSoup(html_text, "html.parser").get_text()
print(f"text: {html_text} \ncleaned_text6: {cleaned_text6}")