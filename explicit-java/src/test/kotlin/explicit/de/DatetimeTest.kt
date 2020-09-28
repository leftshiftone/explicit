package explicit.de

import org.junit.jupiter.api.TestFactory
import java.time.LocalDateTime

class DatetimeTest : AbstractExplitirRulesTest("/de/datetime.xml") {

    @TestFactory
    fun test() = register(
            "vom 1 April bis zum 10 April 2018" to listOf(mapOf("date2" to date(10, 4, 2018), "date1" to date(1, 4, 2018))),
            "text vom 1 April bis zum 10 April 2018 text" to listOf(mapOf("date2" to date(10, 4, 2018), "date1" to date(1, 4, 2018))),
            "ab dem 1 März 2018 1 woche" to listOf(mapOf("date2" to date(8, 3, 2018), "date1" to date(1, 3, 2018))),
            "text ab dem 1 März 2018 1 woche text" to listOf(mapOf("date2" to date(8, 3, 2018), "date1" to date(1, 3, 2018))),
            "01.01.2010 bis 01.02.2010" to listOf(mapOf("date2" to date(1, 2, 2010), "date1" to date(1, 1, 2010))),
            "01.01.2010 - 01.02.2010" to listOf(mapOf("date2" to date(1, 2, 2010), "date1" to date(1, 1, 2010))),
            "Zeitraum Ende April bis Anfang Mai 2018" to listOf(mapOf("date2" to date(5, 5, 2018), "date1" to date(26, 4, 2018), "fuzzy" to true)),
            "text Zeitraum Ende April bis Anfang Mai 2018 text" to listOf(mapOf("date2" to date(5, 5, 2018), "date1" to date(26, 4, 2018), "fuzzy" to true)),
            "Zeitraum Ende April - Anfang Mai 2018" to listOf(mapOf("date2" to date(5, 5, 2018), "date1" to date(26, 4, 2018), "fuzzy" to true)),
            "Zeitraum Ende April/Anfang Mai 2018" to listOf(mapOf("date2" to date(5, 5, 2018), "date1" to date(26, 4, 2018), "fuzzy" to true)),
            "text Zeitraum Ende April - Anfang Mai 2018 text" to listOf(mapOf("date2" to date(5, 5, 2018), "date1" to date(26, 4, 2018), "fuzzy" to true)),
            "in der zeit von ende april bis mitte mai 2017" to listOf(mapOf("date2" to date(15, 5, 2017), "date1" to date(30, 4, 2017))),
            "text in der zeit von ende april bis mitte mai 2017 text" to listOf(mapOf("date2" to date(15, 5, 2017), "date1" to date(30, 4, 2017))),
            "ab 10.10.2010 text text für 1 woche" to listOf(mapOf("date2" to date(17, 10, 2010), "date1" to date(10, 10, 2010))),
            "text ab 10.10.2010 text text für 1 woche text" to listOf(mapOf("date2" to date(17, 10, 2010), "date1" to date(10, 10, 2010))),
            "ab 10.10.2010 text text für 2 wochen" to listOf(mapOf("date2" to date(24, 10, 2010), "date1" to date(10, 10, 2010))),
            "text ab 10.10.2010 text text für 2 wochen text" to listOf(mapOf("date2" to date(24, 10, 2010), "date1" to date(10, 10, 2010))),
            "möchten ende april 2018 text text 1 woche" to listOf(mapOf("date2" to date(7, 5, 2018), "date1" to date(30, 4, 2018))),
            "text möchten ende april 2018 text text 1 woche text" to listOf(mapOf("date2" to date(7, 5, 2018), "date1" to date(30, 4, 2018))),
            "möchte ende april 2018 text text 1 woche" to listOf(mapOf("date2" to date(7, 5, 2018), "date1" to date(30, 4, 2018))),
            "text möchte ende april 2018 text text 1 woche text" to listOf(mapOf("date2" to date(7, 5, 2018), "date1" to date(30, 4, 2018))),
            "text frühestens am 1 juli bis spätestens am 10 august 2018 text" to listOf(mapOf("date2" to date(10, 8, 2018), "date1" to date(1, 7, 2018), "fuzzy" to true)),
            "text früh am 1 juli bis spät am 10 august 2018 text" to listOf(mapOf("date2" to date(10, 8, 2018), "date1" to date(1, 7, 2018), "fuzzy" to true)),
            "text früh. am 1 juli bis spät. am 10 august 2018 text" to listOf(mapOf("date2" to date(10, 8, 2018), "date1" to date(1, 7, 2018), "fuzzy" to true)),
            "vom 5 april 2016 bis zum 12 april 2016" to listOf(mapOf("date2" to date(12, 4, 2016), "date1" to date(5, 4, 2016))),
            "Zeitraum frühestens 8 Juli bis spätestens 30 Juli 2018" to listOf(mapOf("date2" to date(30, 7, 2018), "date1" to date(8, 7, 2018), "fuzzy" to true)),
            "Zeitraum frühestens 8. Juli bis spätestens 30 Juli 2018" to listOf(mapOf("date2" to date(30, 7, 2018), "date1" to date(8, 7, 2018), "fuzzy" to true)),
            "Zeitraum früh. 8. Juli bis spät 30 Juli 2018" to listOf(mapOf("date2" to date(30, 7, 2018), "date1" to date(8, 7, 2018), "fuzzy" to true)),
            "Zeitraum früh. 8. Juli bis spät 30 Juli 2017" to listOf(mapOf("date2" to date(30, 7, 2017), "date1" to date(8, 7, 2017), "fuzzy" to true)),
            "ab 14. August 2018 eine Woche" to listOf(mapOf("date2" to date(21, 8, 2018), "date1" to date(14, 8, 2018))),
            "ab 14. August 2018 eine Woche text." to listOf(mapOf("date2" to date(21, 8, 2018), "date1" to date(14, 8, 2018))),
            "29.9.2017 bis 6.10. 2017" to listOf(mapOf("date2" to date(6, 10, 2017), "date1" to date(29, 9, 2017))),
            "text text 29.9.2017 bis 6.10. 2017 text text" to listOf(mapOf("date2" to date(6, 10, 2017), "date1" to date(29, 9, 2017))),
            "4.1 bis 05.01. 2018" to listOf(mapOf("date2" to date(5, 1, 2018), "date1" to date(4, 1, 2018))),
            "zwischen 8.9 und 18.09 2017" to listOf(mapOf("date2" to date(18, 9, 2017), "date1" to date(8, 9, 2017))),
            "zwischen 8.9 und 18.09 2018 1 woche" to listOf(mapOf("date2" to date(18, 9, 2018), "date1" to date(8, 9, 2018))),
            "zwischen 2005 und 2017" to listOf(mapOf("date2" to date(1, 1, 2017), "date1" to date(1, 1, 2005))),
            "zwischen 8.9. 2017 und 18.09 2018" to listOf(mapOf("date2" to date(18, 9, 2018), "date1" to date(8, 9, 2017))),
            "Zeitraum Ende August/Anfang September 2018." to listOf(mapOf("date2" to date(5, 9, 2018), "date1" to date(25, 8, 2018), "fuzzy" to true)),
            "06.08.17 -12.08.17" to listOf(mapOf("date2" to date(12, 8, 2017), "date1" to date(6, 8, 2017))),
            "ab 29.7.17" to listOf(mapOf("date" to date(29, 7, 2017))),
            "ende februar 2010" to listOf(mapOf("date" to date(28, 2, 2010), "fuzzy" to true)),
            "weihnachtsferien 2015" to listOf(mapOf("date2" to date(10, 1, 2016), "date1" to date(20, 12, 2015), "fuzzy" to true)),
            "in den weihnachtsferien 2015" to listOf(mapOf("date2" to date(10, 1, 2016), "date1" to date(20, 12, 2015), "fuzzy" to true)),
            "08/08/2015" to listOf(mapOf("date" to date(8, 8, 2015))),
            "08/08/2015 - 15/08/2015" to listOf(mapOf("date2" to date(15, 8, 2015), "date1" to date(8, 8, 2015))),
            "08/08/2015 – 15/08/2015" to listOf(mapOf("date2" to date(15, 8, 2015), "date1" to date(8, 8, 2015))),
            "08/08/2015 – 15/08/2015." to listOf(mapOf("date2" to date(15, 8, 2015), "date1" to date(8, 8, 2015))),
            "der 50 woche 2015" to listOf(mapOf("date" to date(17, 12, 2015))),
            "der 50. woche 2015" to listOf(mapOf("date" to date(17, 12, 2015))),
            "Januar 2015" to listOf(mapOf("date2" to date(31, 1, 2015), "date1" to date(1, 1, 2015))),
            "text juli und august 2015 egal wann" to listOf(mapOf("date2" to date(31, 8, 2015), "date1" to date(1, 7, 2015))),
            "6.10. 2017" to listOf(mapOf("date" to date(6, 10, 2017))),
            "29.9.2017 text text 6.10. 2017" to listOf(mapOf("date" to date(6, 10, 2017)), mapOf("date" to date(29, 9, 2017))),
            "zeitraum juni - juli 2017" to listOf(mapOf("date2" to date(31, 7, 2017), "date1" to date(1, 6, 2017), "fuzzy" to true)),
            "03.07. - bis zum 23.07.15" to listOf(mapOf("date2" to date(23, 7, 2015), "date1" to date(3, 7, 2015))),
            "Vom 04.07 bis zum 11.07.2017" to listOf(mapOf("date2" to date(11, 7, 2017), "date1" to date(4, 7, 2017))),
            "vom 04.07. bis zum 11.07 2017" to listOf(mapOf("date2" to date(11, 7, 2017), "date1" to date(4, 7, 2017))),
            "Ab dem 23.05. bis 6.06. 2018 4 Personen" to listOf(mapOf("date2" to date(6, 6, 2018), "date1" to date(23, 5, 2018))),
            "für den 7.11/8.11 - 11.11 2015" to listOf(mapOf("date2" to date(11, 11, 2015), "date1" to date(8, 11, 2015))),
            "Unsere Preisvorstellung liegt bei 1.500-1.800 € pro Person." to listOf(),
            "Zeitraum: zwischen 1. Nov. und 18. Nov. 2018" to listOf(mapOf("date2" to date(18, 11, 2018), "date1" to date(1, 11, 2018))),
            "am 10.1. 2018 für 1 Woche" to listOf(mapOf("date2" to date(17, 1, 2018), "date1" to date(10, 1, 2018))),
            "vom 4.10. 2018 1.woche" to listOf(mapOf("date2" to date(11, 10, 2018), "date1" to date(4, 10, 2018))),
            "Hätte vor im Januar 2018 im Urlaub zu fliegen." to listOf(mapOf("date2" to date(31, 1, 2018), "date1" to date(1, 1, 2018), "fuzzy" to true)),
            "31.8.18 bis14.9.18" to listOf(mapOf("date2" to date(14, 9, 2018), "date1" to date(31, 8, 2018))),
            "6.-20. April 2015" to listOf(mapOf("date2" to date(20, 4, 2015), "date1" to date(6, 4, 2015))),
            "vom 10.08 bis zum 19.08.15." to listOf(mapOf("date2" to date(19, 8, 2015), "date1" to date(10, 8, 2015))),
            "Im Zeitraum Januar bis April 2015" to listOf(mapOf("date2" to date(30, 4, 2015), "date1" to date(1, 1, 2015), "fuzzy" to true)),
            "Hätte vor im Januar 2015 im Urlaub zu fliegen" to listOf(mapOf("date2" to date(31, 1, 2015), "date1" to date(1, 1, 2015), "fuzzy" to true)),
            "Ich will zwischen 8.11 und 15.11.2018 verreisen" to listOf(mapOf("date2" to date(15, 11, 2018), "date1" to date(8, 11, 2018))),
            "ab 14. August 2018 eine Woche" to listOf(mapOf("date2" to date(21, 8, 2018), "date1" to date(14, 8, 2018))),
            "Zeitraum Ende August/Anfang September 2018" to listOf(mapOf("date2" to date(5, 9, 2018), "date1" to date(25, 8, 2018), "fuzzy" to true)),
            "ich suche von 9.2. bis 15/16.2 2018" to listOf(mapOf("date2" to date(16, 2, 2018), "date1" to date(9, 2, 2018))),
            "vom 8.6.2019 - 22.6.19 oder 14.09.19 - 05.10.19" to listOf(mapOf("date2" to date(22, 6, 2019), "date1" to date(8, 6, 2019)),
                    mapOf("date2" to date(5, 10, 2019), "date1" to date(14, 9, 2019)))
    )

    private fun date(day:Int, month:Int, year:Int) = LocalDateTime.of(year, month, day, 0, 0)

    /*
    <test>
    <sentence>vom 8.6.2019 - 22.6.19 oder 14.09.19 - 05.10.19</sentence>
    <expectation>
    <datetime date1="2019-06-08T00:00:00" date2="2019-06-22T00:00:00" />
    <datetime date1="2019-09-14T00:00:00" date2="2019-10-05T00:00:00" />
    </expectation>
    </test>*/

}
