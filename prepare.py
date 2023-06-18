import os
import re

qData_folder = "leetcode_scrapping/QDATA/"

target_str = "Example 1:"

all_lines = []

for i in range(1, 2139):
    file_path = os.path.join(qData_folder, "{}/{}.txt".format(i, i))

    doc = ""
    with open(file_path, "r", encoding='utf-8', errors="ignore") as f:
        lines = f.readlines()

    for line in lines:
        if target_str in line:
            break
        else:
            doc += line

    all_lines.append(doc)


def preprocess(text):      # remove problem no, and return a list of lowercase words
    # removing non alphanumeric chars
    text = re.sub(r'[^a-zA-Z0-9\s-]', '', text)
    terms = [term.lower() for term in text.strip().split()]

    return terms


vocab = {}
documents = []

for index, line in enumerate(all_lines):
    # read statement and add it to the line and then preprocess
    tokens = preprocess(line)
    documents.append(tokens)
    tokens = set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

# to reverse sort the vocab based on frequency

vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))


print('Number of documents: ', len(documents))
print('Size of vocab: ', len(vocab))
print("Sample document: ", documents[100])

# save the vocab in a text file
with open('TF-IDF/vocab.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)


# save the idf values in a text file
with open('TF-IDF/idf-values.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])


# save the documents in a text file
with open('TF-IDF/documents.txt', 'w') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))


inverted_index = {}

for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)


# save the inverted index in a text file
with open('TF-IDF/inverted-index.txt', 'w') as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id)
                for doc_id in inverted_index[key]]))
