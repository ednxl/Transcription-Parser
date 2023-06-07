import os
import re
import spacy
import string
from collections import Counter

# List of names to exclude from counting
excluded_names = [
    "Ethan",
    "Paul",
    "Garrett",
    "Hannah",
    "Brian",
    "Bryan",
    "Kenneth",
    "Parker",
    "Justin",
    "Cody",
    "Stephine",
    "Greg",
    "Del",
    "Dell",
    "Bye",
    "Gotcha",
    "Alrighty",
    "Hey",
    "Yeah",
    "Ill",
    "Sweet",
]

# List of phrases to exclude from counting
excluded_phrases = [
    "i m not sure i",
    "m not sure i m",
    "not sure i m not",
    "not sure i m not",
    "thanks for watching thanks for",
    "for watching thanks for watching",
    "watching thanks for watching thanks",
    "sure i m not sure",
    "four plus four plus four",
    "plus four plus four plus",
    "thank you thank you thank",
    "i do nt",
    "thanks for watching",
    "i m going",
    "for watching thanks",
    "watching thanks for",
    "m going to",
    "do nt know",
    "i m not",
    "it looks like",
    "m not sure",
    "go ahead and",
    "have a good",
    "you thank you",
    "sure i m",
    "not sure i",
    "thank you thank",
    "all right all",
    "right all right",
    "thanks for watching thanks",
    "for watching thanks for",
    "watching thanks for watching",
    "i m going to",
    "i do nt know",
    "have a good one",
    "m not sure i",
    "thank you thank you",
    "sure i m not",
    "i m not sure",
    "not sure i m",
    "all right all right",
    "four plus four plus",
    "plus four plus four",
    "you thank you thank",
    "do nt know i",
    "its a 2pifi backhaul",
    "a 2pifi backhaul its",
    "2pifi backhaul its a",
    "backhaul its a 2pifi",
    "know i do nt",
    "right all right all",
    "nt know i do",
    "you have a good",
    "bye   this is",
    "i m out here",
    "do nt know if",
    "how s it going",
    "all right thank you",
    "a good one you",
    "m out here at",
    "do nt know what",
    "i do nt think",
    "what s going on",
    "m going to go",
    "good one you too",
    "to go ahead and",
    "i m sorry i",
    "i do nt see",
    "  hey this is",
    "i m gon na",
    "it looks like its",
    "ot 46 ot 46",
    "46 ot 46 ot",
    "going to go ahead",
    "can i help you",
    "how can i help",
    "i m just trying",
    "m just trying to",
    "give me just a",
    "thank you no problem",
    "m sorry i m",
    "switch it back up",
    "its going to be",
    "okay i m going",
    "i do nt have",
    "going to go back",
    "it back up i",
    "back up i m",
    "up i m going",
    "going to have to",
    "m going to switch",
    "going to switch it",
    "to switch it back",
    "go back to the",
    "i m trying to",
    "but i do nt",
    "let me take a",
    "to go back to",
    "just trying to get",
    "yeah it looks like",
    "you too bye  ",
    "so i do nt",
    "sorry i m sorry",
    "me take a look",
    "m going to get",
    "  this is brian",
    "brian how can i",
    "i just wanted to",
    "appreciate it no problem",
    "this is brian how",
    "is brian how can",
    "yeah i do nt",
    "thank you very much",
    "good night good night",
    "to five real quick",
    "ill go ahead and",
    "me just a second",
    "night good night good",
    "let me switch to",
    "me switch to five",
    "switch to five real",
    "no problem you have",
    "problem you have a",
    "i was going to",
    "all right i m",
    "one you too bye",
    "  netops this is",
    "bye   hey this",
    "i m over here",
    "no problem bye bye",
    "see if i can",
    "hey ethan this is",
    "it i m going",
    "m going to do",
    "go ahead and get",
    "five real quick okay",
    "real quick okay let",
    "okay let me switch",
    "do nt know why",
    "it looks like the",
    "to see if you",
    "this is ethan hey",
    "thanks man thanks man",
    "trying to get you",
    "to get you started",
    "that s what i",
    "were going to go",
    "a good one bye",
    "man thanks man thanks",
]


def process_file(file_path, nlp):
    with open(file_path, "r") as file:
        text = file.read()
        # Remove punctuation from the text
        text = text.translate(str.maketrans("", "", string.punctuation))
        # Replace "2x5" with "2Pifi"
        text = text.replace("2x5", "2Pifi")
        doc = nlp(text)
        names = [ent.text.split()[0] for ent in doc.ents if ent.label_ == "PERSON"]
        names = [name for name in names if name not in excluded_names]
        words = [
            token.text.lower()
            for token in doc
            if token.text.lower() not in string.punctuation
        ]
        return words, names


def process_folder(folder_path, nlp):
    all_words = []
    all_names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                words, names = process_file(file_path, nlp)
                all_words.extend(words)
                all_names.extend(names)
    return all_words, all_names


def is_common_word(word):
    excluded_words = [
        "i",
        "you",
        "he",
        "she",
        "it",
        "we",
        "they",
        "and",
        "but",
        "or",
        "the",
        "a",
        "an",
        "in",
        "on",
        "at",
        "for",
        "to",
        "from",
        "with",
        "is",
        "am",
        "are",
        "was",
        "were",
        "be",
        "being",
        "been",
        "have",
        "has",
        "had",
        "do",
        "does",
        "did",
        "done",
        "can",
        "could",
        "will",
        "would",
        "shall",
        "should",
        "may",
        "might",
        "must",
        "okay",
        "that",
        "yeah",
        "so",
        "all",
        "just",
        "m",
        "its",
        "s",
        "nt",
        "this",
        "right",
        "there",
        "going",
        "what",
        "up",
        "like",
        "one",
        "me",
        "of",
        "not",
        "no",
        "here",
        "if",
        "see",
        "get",
        "know",
        "good",
        "out",
        "back",
        "got",
        "go",
        "bye",
        "oh",
        "now",
        "hey",
        "well",
        "thanks",
        "let",
        "thank",
        "sure",
        "ticket",
        "ill",
        "yes",
        "then",
        " ",
        "my",
        "looks",
        "re",
        "think",
        "alright",
        "into",
        "because",
        "watching",
        "man",
        "down",
        "how",
        "sir",
        "about",
        "as",
        "still",
        "over",
        "tower",
        "call",
        "problem",
        "everything",
        "need",
        "look",
        "lets",
        "too",
        "them",
        "site",
        "ve",
        "anything",
        "said",
        "appreciate",
        "cool",
        "four",
        "mean",
        "give",
        "two",
        "sorry",
        "your",
        "off",
        "yep",
        "ahead",
        "side",
        "doing",
        "check",
        "when",
        "something",
        "take",
        "want",
        "probably",
        "make",
        "try",
        "other",
        "1",
        "number",
        "guess",
        "ok",
        "-",
        "trying",
        "some",
        "last",
        "guys",
        "any",
        "second",
        "put",
        "gotcha",
        "where",
        "uh",
        "-",
        "ca",
        "time",
        "only",
        "which",
        "able",
        "those",
        "looking",
        "alrighty",
        "plus",
        "quick",
        "thing",
        "really",
        "why",
        "say",
        "ll",
        "actually",
        "way",
        "us",
        "kind",
        "ethan",
        "sounds",
        "bad",
        "set",
        "real",
        "come",
        "already",
        "north",
        "through",
        "stuff",
        "again",
        "gon",
        "na",
        "much",
        "else",
        "more",
        "awesome",
        "maybe",
        "west",
        "name",
        "getting",
        "these",
        "our",
        "working",
        "little",
        "five",
        "issue",
        "gig",
        "night",
        "10",
        "even",
        "help",
        "pretty",
        "both",
        "2",
        "minutes",
        "calling",
        "day",
        "phone",
        "work",
        "brian",
        "hi",
        "before",
        "righty",
        "internet",
        "same",
        "him",
        "open",
        "byebye"]
    return word not in excluded_words


def find_common_words(words, count=20):
    word_counts = Counter(words)
    common_words = [
        (word, count)
        for word, count in word_counts.most_common()
        if is_common_word(word)
    ]
    return common_words[:count]


def find_common_phrases(words, count=20, excluded_phrases=None):
    phrases = []
    for i in range(len(words) - 2):
        if words[i] != words[i + 1] != words[i + 2]:
            phrase = " ".join(words[i : i + 4])
            if excluded_phrases and phrase in excluded_phrases:
                continue
            phrases.append(phrase)
    phrase_counts = Counter(phrases)
    common_phrases = phrase_counts.most_common(count)
    return common_phrases


# Function to find and count specific phrases
def find_specific_phrases(words, phrases):
    specific_phrase_counts = Counter()
    for i in range(len(words) - 4):
        phrase = " ".join(words[i : i + 2])
        if phrase in phrases:
            specific_phrase_counts[phrase] += 1
        phrase = " ".join(words[i : i + 3])
        if phrase in phrases:
            specific_phrase_counts[phrase] += 1
        phrase = " ".join(words[i : i + 4])
        if phrase in phrases:
            specific_phrase_counts[phrase] += 1
    return specific_phrase_counts


# Folder containing the text files
folder_path = "<Folder Path>"

# Load English language model for named entity recognition
nlp = spacy.load("en_core_web_sm")

# Process the folder
words, names = process_folder(folder_path, nlp)

# Find and display common words
common_words = find_common_words(words)
print("Common Words:")
for word, count in common_words:
    print(f"{word}: {count}")

# Find and display common phrases (excluding the excluded phrases)
common_phrases = find_common_phrases(words, excluded_phrases=excluded_phrases)
print("\nCommon Phrases:")
for phrase, count in common_phrases:
    print(f"{phrase}: {count}")


# Specify phrases to look for and count
specific_phrases = [
    "check in",
    "checking in",
    "checking out",
    "check out",
    "clear the tower",
    "clear me",
    "tower cleared",
    "tower clear",
    "not sure",
    "four plus",
    "2pifi backhaul",
    "going to switch",
    "get cleared",
    "tower cleared",
    "last four"]

# Find and display specific phrases
specific_phrase_counts = find_specific_phrases(words, specific_phrases)
print("\nSpecific Phrases:")
for phrase, count in specific_phrase_counts.items():
    print(f"{phrase}: {count}")

# Find and display common names (excluding the excluded names)
common_names = Counter(names).most_common(10)
print("\nCommon Names:")
for name, count in common_names:
    print(f"{name}: {count}")
