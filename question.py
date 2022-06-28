from typing import Tuple
from typing import List


class Question:
    def __init__(self, question_tuple: List[Tuple[str, str]]):
        self.items = []
        for token, content in question_tuple:
            if token in ('key', 'distractor'):
                self.items.append([token, content[4:-1]])
            else:
                self.items.append([token, content[2:-1]])


if __name__ == "__main__":
    question = Question([("stem", "# 강아지 다리 수는?;")])
    print(question.items)
