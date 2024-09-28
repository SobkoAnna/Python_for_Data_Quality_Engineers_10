import re
text = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# Replacing iz with is, ignoring uppercase and lowercase letters
replaced_text = re.sub(" iz "," is ", text, flags=re.IGNORECASE)

sentences = re.split(r'([:.]\s*)', replaced_text)  # Dividing into sentences by end punctuation marks. Creating list with sentences
normalized_sentences = []
for sentence in sentences:
    normalized_sentences.append(sentence.capitalize())  # Normalizeing a sentence
joined_text = ''.join(normalized_sentences)     # Join all sentences from list to string

normal_sentences = re.split(r'[.]\s*', joined_text)
last_words = []
for sentence in normal_sentences:
    if sentence.strip():
        last_words.append(sentence.split()[-1])  # Extracting the last word from every sentence
last_sentence = ' '.join(last_words)  # Join all words

last_sentence = last_sentence.capitalize()  # Normalizing new sentence

new_list = []
for item in normalized_sentences:
    if "paragraph" in item:
        item = f'{item}. {last_sentence}'  # Inserting new sentence after "paragraph" word
        new_list.append(item)  # Adding created sentence to the text
    else:
        new_list.append(item)   # Adding next sentence to the text
final_text = ''.join(new_list)  # Join all sentences from list to string
print(final_text)

# Count the number of spaces in the text
count_on_text = 0
symbols_to_count = [" ", "\t", "\n"]
for s in symbols_to_count:
    count_on_text += final_text.count(s)
print('Number of whitespace ', count_on_text)
