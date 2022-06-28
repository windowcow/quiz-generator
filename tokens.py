from dataclasses import dataclass


@dataclass
class Token:
    STEM = r'^#.*;'
    KEY = r'^\[\*\].*;'
    DISTRACTOR = r'^\[ \].*;'