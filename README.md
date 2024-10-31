# NLP_FiltrationTextInput
This code takes user input, converts it to lowercase, removes punctuation, filters out stop words, and removes special characters, outputting a cleaned version of the text.

The code performs several text preprocessing steps. 
1. It downloads a list of English stop words (common words like "and," "the," etc.). In the filter_text function, the input text is converted to lowercase, removing any capitalization.
2. Then punctuation is stripped from the text.
3. Followed by the removal of stop words using the stop_words set. Each word is checked, and special characters are removed using a regular expression (re.sub), leaving only alphabetic characters.
4.  The function then returns the cleaned, filtered text, which is printed as the final output. 
For instance, if the input is "Hello, World! This is a sample text with punctuation, STOPWORDS, and special symbols #@$.", the output will be "hello world sample text punctuation stopwords special symbols".
