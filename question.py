from typing import Tuple


class Question:
    def __init__(self, question_list: Tuple[str, str]):
        self.items = []
        for token, content in question_list:
            if token in ('key', 'distractor'):
                self.items.append([token, content[4:0]])
            else:
                self.items.append([token, content[2:0]])
