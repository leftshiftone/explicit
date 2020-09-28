import datetime
import unittest

from explicit.ExplicitEngine import ExplicitEngine
from explicit.parser.xml.XmlExplicitRulesParser import XmlExplicitRulesParser


class DEDateTimeTest(unittest.TestCase):

    def test(self):
        # logging.basicConfig(level = logging.DEBUG)

        rulez = XmlExplicitRulesParser().parse("../../src/main/resources/de/datetime.xml")
        engine = ExplicitEngine(rulez)

        result = engine.execute("vom 1 April bis zum 10 April 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 1), "date2": datetime.datetime(2018, 4, 10)}])

        result = engine.execute("text vom 1 April bis zum 10 April 2018 text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 1), "date2": datetime.datetime(2018, 4, 10)}])

        result = engine.execute("ab dem 1 März 2018 1 woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 3, 1), "date2": datetime.datetime(2018, 3, 8)}])

        result = engine.execute("text ab dem 1 März 2018 1 woche text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 3, 1), "date2": datetime.datetime(2018, 3, 8)}])

        result = engine.execute("01.01.2010 bis 01.02.2010")
        self.assertEqual(result, [{"date1": datetime.datetime(2010, 1, 1), "date2": datetime.datetime(2010, 2, 1)}])

        result = engine.execute("01.01.2010 - 01.02.2010")
        self.assertEqual(result, [{"date1": datetime.datetime(2010, 1, 1), "date2": datetime.datetime(2010, 2, 1)}])

        result = engine.execute("Zeitraum Ende April bis Anfang Mai 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 26), "date2": datetime.datetime(2018, 5, 5), "fuzzy":True}])

        result = engine.execute("text Zeitraum Ende April bis Anfang Mai 2018 text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 26), "date2": datetime.datetime(2018, 5, 5), "fuzzy":True}])

        result = engine.execute("Zeitraum Ende April - Anfang Mai 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 26), "date2": datetime.datetime(2018, 5, 5), "fuzzy":True}])

        result = engine.execute("Zeitraum Ende April/Anfang Mai 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 26), "date2": datetime.datetime(2018, 5, 5), "fuzzy":True}])

        result = engine.execute("text Zeitraum Ende April - Anfang Mai 2018 text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 26), "date2": datetime.datetime(2018, 5, 5), "fuzzy":True}])

        result = engine.execute("in der zeit von ende april bis mitte mai 2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 4, 30), "date2": datetime.datetime(2017, 5, 15)}])

        result = engine.execute("text in der zeit von ende april bis mitte mai 2017 text")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 4, 30), "date2": datetime.datetime(2017, 5, 15)}])

        result = engine.execute("ab 10.10.2010 text text für 1 woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2010, 10, 10), "date2": datetime.datetime(2010, 10, 17)}])

        result = engine.execute("text ab 10.10.2010 text text für 1 woche text")
        self.assertEqual(result, [{"date1": datetime.datetime(2010, 10, 10), "date2": datetime.datetime(2010, 10, 17)}])

        result = engine.execute("ab 10.10.2010 text text für 2 wochen")
        self.assertEqual(result, [{"date1": datetime.datetime(2010, 10, 10), "date2": datetime.datetime(2010, 10, 24)}])

        result = engine.execute("text ab 10.10.2010 text text für 2 wochen text")
        self.assertEqual(result, [{"date1": datetime.datetime(2010, 10, 10), "date2": datetime.datetime(2010, 10, 24)}])

        result = engine.execute("möchten ende april 2018 text text 1 woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 30), "date2": datetime.datetime(2018, 5, 7)}])

        result = engine.execute("text möchten ende april 2018 text text 1 woche text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 30), "date2": datetime.datetime(2018, 5, 7)}])

        result = engine.execute("möchte ende april 2018 text text 1 woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 30), "date2": datetime.datetime(2018, 5, 7)}])

        result = engine.execute("text möchte ende april 2018 text text 1 woche text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 4, 30), "date2": datetime.datetime(2018, 5, 7)}])

        result = engine.execute("text frühestens am 1 juli bis spätestens am 10 august 2018 text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 7, 1), "date2": datetime.datetime(2018, 8, 10), "fuzzy":True}])

        result = engine.execute("text früh am 1 juli bis spät am 10 august 2018 text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 7, 1), "date2": datetime.datetime(2018, 8, 10), "fuzzy":True}])

        result = engine.execute("text früh. am 1 juli bis spät. am 10 august 2018 text")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 7, 1), "date2": datetime.datetime(2018, 8, 10), "fuzzy":True}])

        result = engine.execute("vom 5 april 2016 bis zum 12 april 2016")
        self.assertEqual(result, [{"date1": datetime.datetime(2016, 4, 5), "date2": datetime.datetime(2016, 4, 12)}])

        result = engine.execute("Zeitraum frühestens 8 Juli bis spätestens 30 Juli 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 7, 8), "date2": datetime.datetime(2018, 7, 30), "fuzzy":True}])

        result = engine.execute("Zeitraum frühestens 8. Juli bis spätestens 30 Juli 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 7, 8), "date2": datetime.datetime(2018, 7, 30), "fuzzy":True}])

        result = engine.execute("Zeitraum früh. 8. Juli bis spät 30 Juli 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 7, 8), "date2": datetime.datetime(2018, 7, 30), "fuzzy":True}])

        result = engine.execute("Zeitraum früh. 8. Juli bis spät 30 Juli 2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 7, 8), "date2": datetime.datetime(2017, 7, 30), "fuzzy":True}])

        result = engine.execute("ab 14. August 2018 eine Woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 8, 14), "date2": datetime.datetime(2018, 8, 21)}])

        result = engine.execute("ab 14. August 2018 eine Woche text.")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 8, 14), "date2": datetime.datetime(2018, 8, 21)}])

        result = engine.execute("29.9.2017 bis 6.10. 2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 9, 29), "date2": datetime.datetime(2017, 10, 6)}])

        result = engine.execute("text text 29.9.2017 bis 6.10. 2017 text text")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 9, 29), "date2": datetime.datetime(2017, 10, 6)}])

        result = engine.execute("4.1 bis 05.01. 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 1, 4), "date2": datetime.datetime(2018, 1, 5)}])

        result = engine.execute("zwischen 8.9 und 18.09 2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 9, 8), "date2": datetime.datetime(2017, 9, 18)}])

        result = engine.execute("zwischen 2005 und 2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2005, 1, 1), "date2": datetime.datetime(2017, 1, 1)}])

        result = engine.execute("zwischen 8.9. 2017 und 18.09 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 9, 8), "date2": datetime.datetime(2018, 9, 18)}])

        result = engine.execute("Zeitraum Ende August/Anfang September 2018.")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 8, 25), "date2": datetime.datetime(2018, 9, 5), "fuzzy":True}])

        result = engine.execute("06.08.2017. -12.08.2017.")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 8, 6), "date2": datetime.datetime(2017, 8, 12)}])

        result = engine.execute("ab 29.7.17")
        self.assertEqual(result, [{"date": datetime.datetime(2017, 7, 29)}])

        result = engine.execute("ende februar 2010")
        self.assertEqual(result, [{"date": datetime.datetime(2010, 2, 28), "fuzzy":True}])

        result = engine.execute("weihnachtsferien 2015")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 12, 20), "date2": datetime.datetime(2016, 1, 10), "fuzzy":True}])

        result = engine.execute("in den weihnachtsferien 2015")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 12, 20), "date2": datetime.datetime(2016, 1, 10), "fuzzy":True}])

        result = engine.execute("08/08/2015")
        self.assertEqual(result, [{"date": datetime.datetime(2015, 8, 8)}])

        result = engine.execute("08/08/2015 - 15/08/2015")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 8, 8), "date2": datetime.datetime(2015, 8, 15)}])

        result = engine.execute("08/08/2015 - 15/08/2015.")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 8, 8), "date2": datetime.datetime(2015, 8, 15)}])

        result = engine.execute("der 50 woche 2015")
        self.assertEqual(result, [{"date": datetime.datetime(2015, 12, 17)}])

        result = engine.execute("der 50. woche 2015")
        self.assertEqual(result, [{"date": datetime.datetime(2015, 12, 17)}])

        result = engine.execute("Januar 2015")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 1, 1), "date2": datetime.datetime(2015, 1, 31)}])

        result = engine.execute("text juli und august 2015 egal wann")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 7, 1), "date2": datetime.datetime(2015, 8, 31)}])

        result = engine.execute("6.10. 2017")
        self.assertEqual(result, [{"date": datetime.datetime(2017, 10, 6)}])

        result = engine.execute("29.9.2017 text text 6.10. 2017")
        self.assertEqual(result, [{"date": datetime.datetime(2017, 10, 6)}, {"date": datetime.datetime(2017, 9, 29)}])

        result = engine.execute("zeitraum juni - juli 2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 6, 1), "date2": datetime.datetime(2017, 7, 31), "fuzzy":True}])

        result = engine.execute("03.07. - bis zum 23.07.15")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 7, 3), "date2": datetime.datetime(2015, 7, 23)}])

        result = engine.execute("Vom 04.07 bis zum 11.07.2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 7, 4), "date2": datetime.datetime(2017, 7, 11)}])

        result = engine.execute("vom 04.07. bis zum 11.07 2017")
        self.assertEqual(result, [{"date1": datetime.datetime(2017, 7, 4), "date2": datetime.datetime(2017, 7, 11)}])

        result = engine.execute("Ab dem 23.05. bis 6.06. 2018 4 Personen")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 5, 23), "date2": datetime.datetime(2018, 6, 6)}])

        result = engine.execute("für den 7.11/8.11 - 11.11 2015")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 11, 8), "date2": datetime.datetime(2015, 11, 11)}])

        result = engine.execute("Unsere Preisvorstellung liegt bei 1.500-1.800 € pro Person.")
        self.assertEqual(result, [])

        result = engine.execute("Zeitraum: zwischen 1. Nov. und 18. Nov. 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 11, 1), "date2": datetime.datetime(2018, 11, 18)}])

        result = engine.execute("am 10.1. 2018 für 1 Woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 1, 10), "date2": datetime.datetime(2018, 1, 17)}])

        result = engine.execute("vom 4.10. 2018 1.woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 10, 4), "date2": datetime.datetime(2018, 10, 11)}])

        result = engine.execute("Hätte vor im Januar 2018 im Urlaub zu fliegen.")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 1, 1), "date2": datetime.datetime(2018, 1, 31), "fuzzy":True}])

        result = engine.execute("31.8.18 bis14.9.18")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 8, 31), "date2": datetime.datetime(2018, 9, 14)}])

        result = engine.execute("6.-20. April 2015")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 4, 6), "date2": datetime.datetime(2015, 4, 20)}])

        result = engine.execute("vom 10.08 bis zum 19.08.15.")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 8, 10), "date2": datetime.datetime(2015, 8, 19)}])

        result = engine.execute("Im Zeitraum Januar bis April 2015")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 1, 1), "date2": datetime.datetime(2015, 4, 30), "fuzzy":True}])

        result = engine.execute("Hätte vor im Januar 2015 im Urlaub zu fliegen")
        self.assertEqual(result, [{"date1": datetime.datetime(2015, 1, 1), "date2": datetime.datetime(2015, 1, 31), "fuzzy":True}])

        result = engine.execute("Ich will zwischen 8.11 und 15.11.2018 verreisen")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 11, 8), "date2": datetime.datetime(2018, 11, 15)}])

        result = engine.execute("ab 14. August 2018 eine Woche")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 8, 14), "date2": datetime.datetime(2018, 8, 21)}])

        result = engine.execute("Zeitraum Ende August/Anfang September 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 8, 25), "date2": datetime.datetime(2018, 9, 5), "fuzzy":True}])

        result = engine.execute("ich suche von 9.2. bis 15/16.2 2018")
        self.assertEqual(result, [{"date1": datetime.datetime(2018, 2, 9), "date2": datetime.datetime(2018, 2, 16)}])

        result = engine.execute("vom 8.6.2019 - 22.6.19 oder 14.09.19 - 05.10.19")
        self.assertEqual(result, [
            {"date1": datetime.datetime(2019, 6, 8), "date2": datetime.datetime(2019, 6, 22)},
            {"date1": datetime.datetime(2019, 9, 14), "date2": datetime.datetime(2019, 10, 5)}
        ])

    if __name__ == '__main__':
        unittest.main()
