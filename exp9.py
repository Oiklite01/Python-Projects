#-m for pip
import nltk
input_paragraph="""Japanese kamikaze tactics of World War II were born out of obscurity 
and represent a unique and controversial chapter in military history. This essay explores 
the origins, motivations, effectiveness, and legacy of suicide bombings by Japanese pilots.
."""
sentences=nltk.tokenize.sent_tokenize(input_paragraph)
words=nltk.tokenize.word_tokenize(input_paragraph)
print(sentences)
print()
print(words)