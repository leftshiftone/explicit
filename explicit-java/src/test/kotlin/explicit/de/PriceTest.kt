package explicit.de

import org.junit.jupiter.api.TestFactory

class PriceTest : AbstractExplicitRulesTest("de/price") {

    @TestFactory
    fun test() = register(
            "800 / 900 euro" to listOf(mapOf("amountMax" to 900, "amountMin" to 800, "scope" to "total", "currency" to "euro")),
            "800 bis 900 euro" to listOf(mapOf("amountMax" to 900, "amountMin" to 800, "scope" to "total", "currency" to "euro")),
            "900 euro" to listOf(mapOf("amount" to 900, "scope" to "total", "currency" to "euro")),
            "800 / 900 €" to listOf(mapOf("amountMax" to 900, "amountMin" to 800, "scope" to "total", "currency" to "euro")),
            "800 / 900 dollar" to listOf(mapOf("amountMax" to 900, "amountMin" to 800, "scope" to "total", "currency" to "dollar")),
            "800 / 900 $" to listOf(mapOf("amountMax" to 900, "amountMin" to 800, "scope" to "total", "currency" to "dollar")),
            "800 euro / 900 euro" to listOf(mapOf("amountMax" to 900, "amountMin" to 800, "scope" to "total", "currency" to "euro")),
            "800 euro" to listOf(mapOf("amount" to 800, "scope" to "total", "currency" to "euro")),
            "vom 10 april bis zum 5 mai 2016 um 900 €" to listOf(mapOf("amount" to 900, "scope" to "total", "currency" to "euro")),
            "bis 1.000,- €" to listOf(mapOf("amount" to 1000, "scope" to "total", "currency" to "euro")),
            "bis 1.000,- euro" to listOf(mapOf("amount" to 1000, "scope" to "total", "currency" to "euro")),
            "1000euro" to listOf(mapOf("amount" to 1000, "scope" to "total", "currency" to "euro")),
            "550-600€" to listOf(mapOf("amountMax" to 600, "amountMin" to 550, "scope" to "total", "currency" to "euro")),
            "bis 550€" to listOf(mapOf("amount" to 550, "scope" to "total", "currency" to "euro")),
            "das Hotel ca. 1.200€ kostet" to listOf(mapOf("amount" to 1200, "scope" to "total", "currency" to "euro")),
            "Unsere Preisvorstellung liegt bei 1.500-1.800 € pro Person." to listOf(mapOf("amountMax" to 1800, "amountMin" to 1500, "scope" to "person", "currency" to "euro")),
            "Unsere Preisvorstellungen liegen bei 300 euro pro Person." to listOf(mapOf("amount" to 300, "scope" to "person", "currency" to "euro")),
            "Und pro Kopf 2000€ wäre schön" to listOf(mapOf("amount" to 2000, "scope" to "person", "currency" to "euro")),
            "3000 p.P" to listOf(mapOf("amount" to 3000, "scope" to "person", "currency" to "euro")),
            "Preis bis ca. 900 Euro pro Person Gesamtpreis also ca. 3600" to listOf(mapOf("amount" to 900, "scope" to "person", "currency" to "euro")),
            "für 2 personen nicht mehr als 2000€" to listOf(mapOf("amount" to 2000, "negation" to false, "scope" to "total", "currency" to "euro")),
            "nicht über 4.000 eur" to listOf(mapOf("amount" to 4000, "negation" to false, "scope" to "total", "currency" to "euro")),
            "pro person nicht mehr als 1000 eur" to listOf(mapOf("amount" to 1000, "negation" to false, "scope" to "person", "currency" to "euro")),
            "nicht mehr als 1000 euro pro person" to listOf(mapOf("amount" to 1000, "negation" to false, "scope" to "person", "currency" to "euro")),
            "für 5 personen nicht mehr als 1000 euro" to listOf(mapOf("amount" to 1000, "negation" to false, "scope" to "total", "currency" to "euro")),
            "pro person bis 1000,- euro" to listOf(mapOf("amount" to 1000, "scope" to "person", "currency" to "euro")),
            "1000 euro pro kopf" to listOf(mapOf("amount" to 1000, "scope" to "person", "currency" to "euro")),
            "es soll günstig sein" to listOf(mapOf("sensibility" to "high", "priceCategory" to "cheap", "currency" to "euro"))
    )

}
