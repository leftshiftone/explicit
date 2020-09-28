import unittest

from explicit.ExplicitEngine import ExplicitEngine
from explicit.parser.xml.XmlExplicitRulesParser import XmlExplicitRulesParser


class ExplicitEngineTest(unittest.TestCase):

    def test_simple_string_extractor(self):
        rulez = XmlExplicitRulesParser().parse("./extractors.xml")
        engine = ExplicitEngine(rulez)
        result = engine.execute("simple string extractor")

        self.assertEqual([{'one': 'A', 'two': 'B'}], result)

    def test_simple_number_extractor(self):
        rulez = XmlExplicitRulesParser().parse("./extractors.xml")
        engine = ExplicitEngine(rulez)
        result = engine.execute("simple number extractor")

        self.assertEqual([{'one': 1, 'two': 2}], result)

    def test_simple_boolean_extractor(self):
        rulez = XmlExplicitRulesParser().parse("./extractors.xml")
        engine = ExplicitEngine(rulez)
        result = engine.execute("simple boolean extractor")

        self.assertEqual([{'one': True, 'two': False}], result)

    def test_simple_variable_extractor(self):
        rulez = XmlExplicitRulesParser().parse("./extractors.xml")
        engine = ExplicitEngine(rulez)
        result = engine.execute("simple variable extractor")

        self.assertEqual([{'one': "variable", 'two': "extractor"}], result)

    def test_simple_function_extractor(self):
        rulez = XmlExplicitRulesParser().parse("./extractors.xml")
        engine = ExplicitEngine(rulez)
        result = engine.execute("simple function extractor")

        self.assertEqual([{'one': "FUNCTION", 'two': "EXTRACTOR"}], result)

    if __name__ == '__main__':
        unittest.main()
