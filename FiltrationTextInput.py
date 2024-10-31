import nltk
from nltk.corpus import stopwords
import string
import re
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def filter_text(text):
    # Lowercasing
    text = text.lower()
    # Removing punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Removing stop words
    words = [word for word in text.split() if word not in stop_words]
    # Removing special characters
    filtered_text = [re.sub(r'\W+', '', word) for word in words]
    return ' '.join(filtered_text)
user_input = input("Enter some text: ")
filtered_result = filter_text(user_input)
print("Filtered Text:", filtered_result)

#OUTPUT
#Enter some text: Hello, World! This is a sample text with punctuation, STOPWORDS, and special symbols #@$.
#Filtered Text: hello world sample text punctuation stopwords special symbols