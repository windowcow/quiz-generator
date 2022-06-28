from dataclasses import dataclass
import re
import string
from tokens import Token

# load sample file
sample_file = open("sample-question.txt", 'r')
sample_text = sample_file.read()
sample_file.close()

print(sample_text)

# preprocessing : remove whitespace


def strip_whitespace(target: str):
    return target.strip(string.whitespace)

# sample_text = strip_whitespace(sample_text)


print(sample_text)


def tokenizer(target_text: str):
    # There should be only one stem
    group = re.match(Token.STEM, target_text)
    while True:
        # remove whitespace
        target_text = strip_whitespace(target_text)


a = re.match(r'#.*;', sample_text).group()


print(a)
