---
marp: true
theme: custom
---

# NLP: Filtering and Distance
Today we will talk about filtering, tokenizing, and distance metrics. The point is to be able to extract useful data from unstructured text.

---
# Tokenizing
Text must be split into usable chunks, depending on the problem you're trying to solve. Tokenizing is an automatic, standard way to break up a sentence into word-like chunks.

`"The cats are running faster than the dogs."`
`['The', 'cats', 'are', 'running', 'faster', 'than', 'the', 'dogs', '.']`


---
# Stemming
Some words share the same stem (or root). The word `cats` has the stem `cat`.

`['The', 'cats', 'are', 'running', 'faster', 'than', 'the', 'dogs', '.']`
`['the', 'cat', 'are', 'run', 'faster', 'than', 'the', 'dog', '.']`


---
# Stopwords
Some words don't give us a lot of information. We can define and remove `stopwords`.

`['the', 'cat', 'are', 'run', 'faster', 'than', 'the', 'dog', '.']`
`['cat', 'run', 'faster', 'dog']`

---
# Part-of-Speech Tagging
Some words can be identified by the sentence structure.
`text = "The cats are running faster than the dogs."`
```[
    ('The',     'DT' ), # determiner
    ('cats',    'NNS'), # Plural noun
    ('are',     'VBP'), # verb, non-3rd person singular present
    ('running', 'VBG'), # verb, gerund/present participle
    ('faster',  'RBR')  # comparative adverb
... ]
```

---
# Eastham Example
Demo


---
# Distance Metrics
Sometimes you want to compare words directly without filtering. A common way to compare words is by edit distance:

Example: `cat` and `cats` would take one edit (addition).

Example: `cat` and `cut` would take one edit (substitution).

---
# Distance Metric Demo
Demo