import re

normalized_sentences = []

def func_whitespaces(final_text):
    count_on_text = 0
    symbols_to_count = [" ", "\t", "\n"]
    for s in symbols_to_count:
        count_on_text += final_text.count(s)
    print('Number of whitespace ', count_on_text)
    return count_on_text

def func_final_text(last_sentence):
    temp_list = []
    for item in normalized_sentences:
        if "paragraph" in item:
            item = f'{item}. {last_sentence}'  # Inserting new sentence after "paragraph" word
            temp_list.append(item)  # Adding created sentence to the text
        else:
            temp_list.append(item)  # Adding next sentence to the text
    final_text = ''.join(temp_list)
    print(final_text)
    return final_text

def func_last_words(replaced_text):
    last_words = []
    for sentence in replaced_text:
        if sentence.strip():
            last_words.append(sentence.split()[-1])  # Extracting the last word from every sentence
    last_sentence = ' '.join(last_words)  # Join all words
    return last_sentence.capitalize()  # Normalizing new sentence

def func_normalized_sentences(replaced_text):
    sentences = re.split(r'([:.]\s*)',
                         replaced_text)  # Dividing into sentences by end punctuation marks. Creating list with sentences
    for sentence in sentences:
        normalized_sentences.append(sentence.capitalize())  # Normalizeing a sentence
    joined_text = ''.join(normalized_sentences)  # Join all sentences from list to string
    normal_sentences = re.split(r'[.]\s*', joined_text)
    return normal_sentences
