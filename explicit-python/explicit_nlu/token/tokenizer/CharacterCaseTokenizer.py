import re
from enum import Enum
from typing import List

from explicit_nlu.parser.ExplicitRules import Token


class CharacterCaseTokenizer:

    @staticmethod
    def tokenize(text: str, tokens: List[Token] = []) -> List[str]:
        def evaluate_token(part: str):
            for token in tokens:
                if not token.regex and token.pattern == part:
                    return (token.replacement or part).split()

                if token.regex:
                    matcher = re.search(token.pattern, part)
                    is_boundary = text.endswith(part)

                    if matcher and (token.boundary or not is_boundary):
                        list = []
                        if matcher.start() > 0:
                            list.extend(CharacterCaseTokenizer.tokenize(part[0:matcher.start()], tokens))

                        if len(matcher.groups()) > 0:
                            for group in matcher.groups():
                                list.extend([group])
                        else:
                            list.extend([matcher.group(0)])

                        if len(part) > len(matcher.group()):
                            if not part.endswith(matcher.group()):
                                list.extend(CharacterCaseTokenizer.tokenize(part[matcher.end():], tokens))

                        return list

            return mapper(part)

        def mapper(part: str) -> List[str]:
            result: List[str] = []
            writer: List[str] = []

            token_type: TokenType | None = None

            for char in part:
                if token_type is None:
                    writer.append(char)
                elif token_type is TokenType.to_type(char):
                    if token_type is TokenType.SPECIAL:
                        result.append("".join(writer))
                        writer = [char]
                    else:
                        writer.append(char)
                else:
                    result.append("".join(writer))
                    writer = [char]
                token_type = TokenType.to_type(char)

            if len(writer) > 0:
                result.append("".join(writer))

            return result

        a_list = list(map(evaluate_token, text.lower().split()))
        return [item for sublist in a_list for item in sublist]


class TokenType(Enum):
    TEXT = 1
    NUMBER = 2
    SPECIAL = 3

    @staticmethod
    def to_type(char: str) -> 'TokenType':
        if char.isalpha():
            return TokenType.TEXT
        if char.isdigit():
            return TokenType.NUMBER
        return TokenType.SPECIAL
