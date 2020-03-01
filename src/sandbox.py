from pathlib import Path
from bs4 import BeautifulSoup
import spacy

# python -m spacy download en_core_web_sm
xml_path = Path("input/test.xml")

soup = BeautifulSoup(xml_path.read_text(encoding="utf-8"), 'html.parser')
print(soup.prettify())

nlp = spacy.load("en_core_web_sm")

# example_sent = "Apple is looking at buying U.K. startup for $1 billion"
# doc = nlp(example_sent)
# altered_sent = example_sent
# for ent in doc.ents:
#     xml_string = "<entity type=\"" + str(ent.label_) + "\">" + ent.text + "</entity>"
#     altered_sent = altered_sent.replace(ent.text, xml_string)
# print(example_sent)
# print(altered_sent)


def annotate_text_ner(plaintext):
    altered_text = plaintext
    spacy_doc = nlp(plaintext)
    for ent in spacy_doc.ents:
        print(ent.text + "__" + str(ent.label_))
        xml_string = "<entity type=\"" + str(ent.label_) + "\">" + ent.text + "</entity>"
        altered_text = altered_text.replace(ent.text, xml_string)

    return altered_text


for text in soup.find_all("text"):
    # print(text)
    annotated_text = annotate_text_ner(str(text))
    # print(annotated_text)
    new_soup = BeautifulSoup(annotated_text, features="html.parser")
    text.replace_with(new_soup)

print("NEW")
print(soup)