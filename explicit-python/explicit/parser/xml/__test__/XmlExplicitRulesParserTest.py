import unittest

from explicit.parser.xml.XmlExplicitRulesParser import XmlExplicitRulesParser


class XmlExplicitRulesParserTest(unittest.TestCase):

    def test_tokenization(self):
        parser = XmlExplicitRulesParser()
        rulez = parser.parse("D:/IntellijProjects/nerulez/src/main/resources/de/datetime.xml")

        self.assertTrue(len(rulez.mappings) > 0)
        self.assertTrue(len(rulez.rulez) > 0)
        self.assertTrue(len(rulez.patterns) > 0)
        self.assertTrue(len(rulez.labels) > 0)
        self.assertTrue(len(rulez.tokens) > 0)
        self.assertTrue(len(rulez.features) > 0)

    if __name__ == '__main__':
        unittest.main()
