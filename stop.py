import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Read the contents of the file
file_name = "paragraphs.txt"
with open(file_name, "r") as file:
    text = file.read()

# Tokenize the text into words
words = nltk.word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

# Join the filtered words back into a paragraph
filtered_text = ' '.join(filtered_words)

# Write the filtered text to a file
filtered_output_file_name = "filtered_paragraph.txt"
with open(filtered_output_file_name, "w") as filtered_output_file:
    filtered_output_file.write(filtered_text)

print(f"Filtered paragraph saved to '{filtered_output_file_name}'")

# Count the frequency of each word
word_freq = Counter(filtered_words)
print(word_freq)

# Open a file for writing the word frequency count
word_freq_output_file_name = "word_frequency_output.txt"
with open(word_freq_output_file_name, "w") as word_freq_output_file:
    # Write the word frequency count to the file
    for word, freq in word_freq.items():
        word_freq_output_file.write(f"{word}: {freq}\n")

print(f"Word frequency count saved to '{word_freq_output_file_name}'")
