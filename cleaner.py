# Define the English vocabulary
START_TOKEN = '<START>'
PADDING_TOKEN = '<PADDING>'
END_TOKEN = '<END>'

english_vocabulary = [START_TOKEN, ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        ':', '<', '=', '>', '?', '@',
                        '[', '\\', ']', '^', '_', '`',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                        'y', 'z',
                        '{', '|', '}', '~','\n', PADDING_TOKEN, END_TOKEN]

# Convert the vocabulary to a set for faster lookup
vocabulary_set = set(english_vocabulary)

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove characters not in the vocabulary
    cleaned_text = ''.join([char for char in text if char in vocabulary_set])
    return cleaned_text

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            cleaned_line = clean_text(line)
            outfile.write(cleaned_line)

# Example usage
input_file = 'Lang/paracrawl-release1.en-ru.zipporah0-dedup-clean.en'
output_file = ('Lang/output_eng.eng')
process_file(input_file, output_file)
