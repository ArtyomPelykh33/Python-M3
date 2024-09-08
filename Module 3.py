import re
text = r"""homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""
# format text in lowercase and split by rows
lower_text = text.lower()
a = lower_text.splitlines()

# remove \xa0 from text and split by rows
text = ''.join(a).replace('\xa0', '')
text1 = text.split(". ")

# capitalize the first character of each row and return to original format (new sentence from the new line)
cap = [a.capitalize() for a in text1]
new = '.\n'.join(cap)

# add whitespaces as in original text
new2 = new.replace('\n', '\n  ')
new3 = new2.replace(':', ':\n ')

# make a list of sentences from text
sent = re.split(r'[.!?]\s*', new3)

#  collect the last word of each sentence
last_words = [sent.split()[-1] for sent in sent if sent]

# create a new sentence from collected words
new_sentence = ''.join(last_words).capitalize() + '.'

# Find last word of each sentence, form a new sentence of them and insert it to existed text
sentences = re.split(r'([.!?]\s*)', new3)
# step 1: Find the index of the sentence that ends with the word "paragraph"
for i in range(len(sentences)):
    if sentences[i].endswith('paragraph'):
        # step 2: Insert the new sentence after the sentence that ends with "paragraph"
        sentences.insert(i + 2, '' + new_sentence + '\n  ')
        break  # stop after inserting the new sentence

# rebuild the text
updated_text = ''.join(sentences)

# replace 'iz' with 'is' when it is a mistake
formatted_text = updated_text.replace(' iz', ' is')

# print final view of text and count all spaces. including whitespaces
print(formatted_text)
print("Number of spaces: ", formatted_text.count(' '))


