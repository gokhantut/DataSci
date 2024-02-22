import spacy as spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Create a list of garden path sentences
gardenpathSentences = [
    "The old man the boat",
    "The horse raced past the barn fell",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Tokenize and perform named entity recognition on each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    for token in doc:
        print(token.text, token.pos_, token.dep_, token.ent_type_)

# Entity explanations
print(spacy.explain("ORG"))
print(spacy.explain("NORP"))

# The two entities I looked up were ORG and NORP
# ORG stands for "Companies, agencies, institutions, etc."
# NORP stands for "Nationalities or religious or political groups"
# Both of these entities make sense in terms of their associated words. 
# For example, in the sentence "The cotton clothing is made of grows in Mississippi", 
# there is no organization or national/religious/political group mentioned, so there are no 
# entities of these types. However, in the sentence "Mary gave the child a Band-Aid", "Band-Aid" 
# is the name of a company and is recognized as an ORG entity, and in the sentence "That Jill is never here 
# hurts", "Jill" may be associated with a particular nationality or political group and is recognized 
# as a NORP entity.
