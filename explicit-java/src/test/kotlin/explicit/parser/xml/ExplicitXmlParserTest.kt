package explicit.parser.xml

import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test

class ExplicitXmlParserTest {

    @Test
    fun test1() {
        val stream = ExplicitXmlParser::class.java.getResourceAsStream("/test1.xml")
        val rulez = ExplicitXmlParser().parse(stream)

        Assertions.assertEquals(rulez.rulez.size, 3)
    }

}
