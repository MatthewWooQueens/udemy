import re
from collections import Counter
from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")

def word_in_sentences(word, text):
    pattern = re.compile("[A-Z]{1}[^.]*[^a-zA-Z]+love[^a-zA-Z]+[^.]*.")
    findings = re.findall(pattern, text)
    print(findings)
 
def most_used_words(text):
    pattern = re.compile("[a-zA-Z]+")
    findings = re.findall(pattern,text.lower())
    #print(findings[:5])

    d = Counter(findings)
    print((sorted(d.items(),key=lambda item: item[1], reverse=True))[:5])
    return d


def paragraph_contain(word, text):
    pattern = re.compile("[^\n]+love[^\n]+")
    findings = re.findall(pattern, text.lower())
    print(findings)

def extract_title(text):
    pattern = re.compile("[a-zA-Z]+[\n]{2}")
    findings = re.findall(pattern, text.lower())
    for x in range(len(findings)):
        findings[x] = findings[x].strip("\n\n")
    print(findings)

def main():
    with open("miracle_in_the_andes.txt",'r', encoding="utf8") as file:
        book = file.read()
    #print(book)
    book.count("Chapter")

    pattern = re.compile("Chapter [0-9]")
    findings = re.findall(pattern, book)
    print(len(findings))

    word = "love"
    #word_in_sentences(word, book)
    d_list = most_used_words(book)
    #paragraph_contain(word,book)
    #extract_title(book)
    filter = []
    for count, w in d_list.items():
        if w not in english_stopwords:
            filter.append((w, count))
    print(filter)

if __name__ == '__main__':
    main()
