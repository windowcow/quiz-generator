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

#


def tokenizer(target_text: str):

    # there should be only one stem
    try:
        target_text = strip_whitespace(target_text)
        temp_result = re.match(Token.STEM, target_text).group()
        target_text = target_text.replace(temp_result, '')
        yield 'stem', temp_result
    except:
        print("no stem found")
        return "no stem found"

    while True:
        # removing whitespace
        target_text = strip_whitespace(target_text)

        # matching
        try:
            temp_result = re.match(Token.KEY, target_text).group()
            target_text = target_text.replace(temp_result, '')
            target_text = strip_whitespace(target_text)

            yield 'key', temp_result

        except:
            try:
                temp_result = re.match(Token.DISTRACTOR, target_text).group()
                target_text = target_text.replace(temp_result, '')
                target_text = strip_whitespace(target_text)

                yield 'distractor', temp_result

            except:
                print("no option found")
                return "no option found"


# target_text = sample_text
# target_text = strip_whitespace(target_text)
# print("1", target_text)

# temp_result = re.match(Token.STEM, target_text).group()
# target_text = target_text.replace(temp_result, '')
# print("2", target_text)

# target_text = strip_whitespace(target_text)
# temp_result = re.match(Token.DISTRACTOR, target_text).group()
# target_text = target_text.replace(temp_result, '')
# print("3", target_text)

# print(target_text)


##########
tknizer = tokenizer(sample_text)
generated_tokens = []
for i in tknizer:
    generated_tokens.append(i)


print(generated_tokens)
