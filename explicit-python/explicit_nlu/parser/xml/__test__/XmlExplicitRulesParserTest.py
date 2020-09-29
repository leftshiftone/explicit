import unittest

from explicit_nlu.parser.xml.ExplicitXmlParser import ExplicitXmlParser


class XmlExplicitRulesParserTest(unittest.TestCase):

    def test_tokenization(self):
        parser = ExplicitXmlParser()
        rulez = parser.parse("D:/IntellijProjects/nerulez/src/main/resources/de/datetime.xml")

        self.assertTrue(len(rulez.mappings) > 0)
        self.assertTrue(len(rulez.rulez) > 0)
        self.assertTrue(len(rulez.patterns) > 0)
        self.assertTrue(len(rulez.labels) > 0)
        self.assertTrue(len(rulez.tokens) > 0)
        self.assertTrue(len(rulez.features) > 0)

    if __name__ == '__main__':
        unittest.main()
