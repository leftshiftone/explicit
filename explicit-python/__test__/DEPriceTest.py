import unittest

from explicit.ExplicitEngine import ExplicitEngine
from explicit.parser.xml.ExplicitXmlParser import ExplicitXmlParser


class DEPriceTest(unittest.TestCase):

    def test(self):
        # logging.basicConfig(level = logging.DEBUG)

        rulez = ExplicitXmlParser().parse("../../src/main/resources/de/price.xml")
        engine = ExplicitEngine(rulez)

        result = engine.execute("800 / 900 euro")
        self.assertEqual(result, [{"amountMax": 900.0, "amountMin": 800.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("800 bis 900 euro")
        self.assertEqual(result, [{"amountMax": 900.0, "amountMin": 800.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("900 euro")
        self.assertEqual(result, [{"amount":900.0, "scope":"total", "currency":"euro"}])

        result = engine.execute("800 / 900 €")
        self.assertEqual(result, [{"amountMax": 900.0, "amountMin": 800.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("800 / 900 dollar")
        self.assertEqual(result, [{"amountMax": 900.0, "amountMin": 800.0, "scope": "total", "currency": "dollar"}])

        result = engine.execute("800 / 900 $")
        self.assertEqual(result, [{"amountMax": 900.0, "amountMin": 800.0, "scope": "total", "currency": "dollar"}])

        result = engine.execute("800 euro / 900 euro")
        self.assertEqual(result, [{"amountMax": 900.0, "amountMin": 800.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("800 euro")
        self.assertEqual(result, [{"amount": 800.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("vom 10 april bis zum 5 mai 2016 um 900 €")
        self.assertEqual(result, [{"amount": 900.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("bis 1.000,- €")
        self.assertEqual(result, [{"amount": 1000.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("bis 1.000,- euro")
        self.assertEqual(result, [{"amount": 1000.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("1000euro")
        self.assertEqual(result, [{"amount": 1000.0, "scope": "total", "currency": "euro"}])

        result = engine.execute("550-600€")
        self.assertEqual(result, [{"amountMin": 550.0, "amountMax":600, "scope": "total", "currency": "euro"}])

        result = engine.execute("bis 550€.")
        self.assertEqual(result, [{"amount":550, "scope": "total", "currency": "euro"}])

        result = engine.execute("das Hotel ca. 1.200€ kostet")
        self.assertEqual(result, [{"amount":1200, "scope": "total", "currency": "euro"}])

        result = engine.execute("1.500-1.800 €.")
        self.assertEqual(result, [{"amountMax": 1800.0, "amountMin":1500.0, "currency": "euro", "scope": "total"}])

        result = engine.execute("Unsere Preisvorstellung liegt bei 1.500-1.800 €.")
        self.assertEqual(result, [{"amountMax": 1800.0, "amountMin":1500.0, "currency": "euro", "scope": "total"}])

        result = engine.execute("Unsere Preisvorstellung liegt bei 1.500-1.800 € pro Person.")
        self.assertEqual(result, [{"amountMax": 1800.0, "amountMin":1500.0, "currency": "euro", "scope": "person"}])

        result = engine.execute("Unsere Preisvorstellungen liegen bei 300 euro pro Person.")
        self.assertEqual(result, [{"amount": 300.0, "currency": "euro", "scope": "person"}])

        result = engine.execute("Und pro Kopf 2000€ wäre schön")
        self.assertEqual(result, [{"amount": 2000.0, "currency": "euro", "scope": "person"}])

        result = engine.execute("3000 p.P")
        self.assertEqual(result, [{"amount": 3000.0, "currency": "euro", "scope": "person"}])

        result = engine.execute("Preis bis ca. 900 Euro pro Person Gesamtpreis also ca. 3600")
        self.assertEqual(result, [{"amount": 900.0, "currency": "euro", "scope": "person"}])

        result = engine.execute("für 2 personen nicht mehr als 2000€")
        self.assertEqual(result, [{"amount": 2000.0, "currency": "euro", "scope": "total", "negation":False}])

        result = engine.execute("nicht über 4.000 eur")
        self.assertEqual(result, [{"amount": 4000.0, "currency": "euro", "scope": "total", "negation":False}])

        result = engine.execute("pro person nicht mehr als 1000 eur")
        self.assertEqual(result, [{"amount": 1000.0, "currency": "euro", "scope": "person", "negation":False}])

        result = engine.execute("nicht mehr als 1000 euro pro person")
        self.assertEqual(result, [{"amount": 1000.0, "currency": "euro", "scope": "person", "negation":False}])

        result = engine.execute("für 5 personen nicht mehr als 1000 euro")
        self.assertEqual(result, [{"amount": 1000.0, "currency": "euro", "scope": "total", "negation":False}])

        result = engine.execute("pro person bis 1000,- euro")
        self.assertEqual(result, [{"amount": 1000.0, "currency": "euro", "scope": "person"}])

        result = engine.execute("1000 euro pro kopf")
        self.assertEqual(result, [{"amount": 1000.0, "currency": "euro", "scope": "person"}])

        result = engine.execute("es soll günstig sein")
        self.assertEqual(result, [{"sensibility": "high", "priceCategory": "cheap", "currency": "euro"}])

    if __name__ == '__main__':
        unittest.main()
