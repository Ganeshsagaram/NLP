import nltk

def tokenize_and_tag(text):
    # Tokenize the text into individual words
    tokens = nltk.word_tokenize(text)
    
    # Perform part-of-speech tagging on the tokens
    tagged_tokens = nltk.pos_tag(tokens)
    
    return tagged_tokens

# Example usage
text = "The quick brown fox jumps over the lazy dog."
tagged_words = tokenize_and_tag(text)
print(tagged_words)
