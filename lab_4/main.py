import function_lab_2 as f2
import random
import function_3_lab as f3
import re


list_dict = [f2.create_random_dict() for i in range(random.randint(2, 9))]  # creation a list of random number of dicts
f2.find_duplicates(list_dict)  # find duplicates in dicts
f2.create_single_dict()     # creation of one joint dict


text = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

replaced_text = re.sub(" iz ", " is ", text, flags=re.IGNORECASE)   # replace
normal_sentences = f3.func_normalized_sentences(replaced_text)  # normalizing text
last_sentence = f3.func_last_words(normal_sentences)  # creation new sentence with last words
final_text = f3.func_final_text(last_sentence)  # building new text with added sentence
f3.func_whitespaces(final_text) # count whitespaces