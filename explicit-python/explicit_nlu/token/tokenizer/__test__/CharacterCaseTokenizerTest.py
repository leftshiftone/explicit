import os
import unittest

from explicit_nlu.parser.ExplicitRules import Token
from explicit_nlu.parser.xml.ExplicitXmlParser import ExplicitXmlParser
from explicit_nlu.token.tokenizer import CharacterCaseTokenizer


class CharacterCaseTokenizerTest(unittest.TestCase):

    root_dir = os.path.dirname(os.path.realpath(__file__))

    def test_tokenization(self):
        self.assertEqual(["abc", "/", "xyz"], CharacterCaseTokenizer.tokenize("abc/xyz"))
        self.assertEqual(["2018", "."], CharacterCaseTokenizer.tokenize("2018."))
        self.assertEqual(["a", "früh", ".", "b", "spät", ".", "c"], CharacterCaseTokenizer.tokenize("a früh. b spät. c"))
        self.assertEqual(["früh", "bis", "spät"], CharacterCaseTokenizer.tokenize("früh bis\n spät"))
        self.assertEqual(["sommer", "regen"], CharacterCaseTokenizer.tokenize("sommerregen", [Token(pattern="sommer",
                                                                                                    replacement="",
                                                                                                    boundary=True,
                                                                                                    regex=True)]))
        self.assertEqual(["sommer", "regen"], CharacterCaseTokenizer.tokenize("sommerregen", [Token(pattern="regen",
                                                                                                    replacement="",
                                                                                                    boundary=True,
                                                                                                    regex=True)]))


    def test_tokenization_with_price_tokens(self):
        rulez = ExplicitXmlParser().parse(f"{self.root_dir}/../../../../../src/main/resources/de/price.xml")
        self.assertEqual(["bis", "1.000,-", "euro"], CharacterCaseTokenizer.tokenize("bis 1.000,- euro", rulez.tokens))
        self.assertEqual(["das", "hotel", "ca", "1.200", "€", "kostet"], CharacterCaseTokenizer.tokenize("das Hotel ca. 1.200€ kostet", rulez.tokens))
        self.assertEqual(["1.500", "-", "1.800", "€", "."], CharacterCaseTokenizer.tokenize("1.500-1.800 €.", rulez.tokens))
        self.assertEqual(["bis", "550", "€", "."], CharacterCaseTokenizer.tokenize("bis 550€.", rulez.tokens))
        self.assertEqual(["500", "-", "600", "€", "."], CharacterCaseTokenizer.tokenize("500-600€.", rulez.tokens))

    def test_tokenization_with_datetime_tokens(self):
        rulez = ExplicitXmlParser().parse(f"{self.root_dir}/../../../../../src/main/resources/de/datetime.xml")
        self.assertEqual(["06.08.2017.", "bis", "12.08.2017."], CharacterCaseTokenizer.tokenize("06.08.2017. bis12.08.2017.", rulez.tokens))
        self.assertEqual(["ab", "29.7.17"], CharacterCaseTokenizer.tokenize("ab 29.7.17", rulez.tokens))
        self.assertEqual(["08/08/2015", "-", "15/08/2015", "."], CharacterCaseTokenizer.tokenize("08/08/2015 - 15/08/2015.", rulez.tokens))
        self.assertEqual(["ich", "suche", "von", "9.2.", "bis", "16.2", "2018"], CharacterCaseTokenizer.tokenize("ich suche von 9.2. bis 15/16.2 2018", rulez.tokens))

    if __name__ == '__main__':
        unittest.main()
