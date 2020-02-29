import nltk
from pathlib import Path
from bs4 import BeautifulSoup
import spacy

# python -m spacy download en_core_web_sm
xml_path = Path("input/test.xml")

soup = BeautifulSoup(xml_path.read_text(encoding="utf-8"), 'html.parser')
print(soup.prettify())

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

# for each thing in set, match in text, replace matches with <><>?
# or build tag in soup?
def create_entity_set(plaintext):
    nltk.n