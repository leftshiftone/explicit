import os
import unittest

from explicit_nlu.ExplicitEngine import ExplicitEngine
from explicit_nlu.parser.xml.ExplicitXmlParser import ExplicitXmlParser


class DEGeneralTest(unittest.TestCase):
    root_dir = os.path.dirname(os.path.realpath(__file__))

    def test(self):
        # logging.basicConfig(level = logging.DEBUG)

        rules = ExplicitXmlParser().parse(f"{self.root_dir}/../../src/main/resources/de/general.xml")
        engine = ExplicitEngine(rules)

        default_check = {
            "date1d": None,
            "date1m": None,
            "date1y": None,
            "date1dm": None,
            "date1dmy": None,
            "date2d": None,
            "date2m": None,
            "date2y": None,
            "date2dm": None,
            "date2dmy": None
        }

        result = engine.execute("Wunschtermin ist der 6. 5. - 09.08.2021 wir sind insgesamt um die 8 Erwachsene.")
        check = default_check
        check.update({"date1d": "6", "date1m": "5", "date2dmy": "09.08.2021"})
        self.assertEqual(result, [check])

        result = engine.execute("Wunschtermin ist der 6. 5. - 09.08.2021 wir sind insgesamt um die 8 Erwachsene und 2 Kinder.")
        check = default_check
        check.update({"date1d": "6", "date1m": "5", "date2dmy": "09.08.2021"})
        self.assertEqual(result, [check])

        result = engine.execute("""
            Wunschtermin ist der 6. - 09.08.2021. Wir sind insgesamt um die 8 Erwachsene und 4 Kinder. Gerne würden wir uns selbst versorgen, aber auch Frühstücksservice wäre ok, wenn es dabei ist. Schön wäre es, wenn die Lage auf dem Land ist, wo man gut einfache Wanderungen und Ausflüge machen kann. Gerne auch mit Tieren, falls das möglich ist. Wenn eine Sauna dabei oder in der Nähe ist, wär das ein Highlight - aber muss nicht dringend sein. Können Sie mir bitte Angebote zusenden.
            """
        )
        check = default_check
        check.update({"date1d": "6", "date1m": "5", "date2dmy": "09.08.2021"})
        self.assertEqual(result, [check])

        result = engine.execute("""
            Wunschtermin ist der 6. - 09.08.2021. Wir sind insgesamt um die 8 Erwachsene und 4 Kinder. Gerne würden wir uns selbst versorgen, aber auch Frühstücksservice wäre ok, wenn es dabei ist. Schön wäre es, wenn die Lage auf dem Land ist, wo man gut einfache Wanderungen und Ausflüge machen kann. Gerne auch mit Tieren, falls das möglich ist. Wenn eine Sauna dabei oder in der Nähe ist, wär das ein Highlight, aber muss nicht dringend sein. Können Sie mir bitte Angebote zusenden.
            """
        )
        check = default_check
        check.update({"date1d": "6", "date1m": "5", "date2dmy": "09.08.2021"})
        self.assertEqual(result, [check])

    if __name__ == '__main__':
        unittest.main()
