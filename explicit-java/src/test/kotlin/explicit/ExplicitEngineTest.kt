package explicit

import explicit.parser.xml.ExplicitXmlParser
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test

class ExplicitEngineTest {

    @Test
    fun `simple string extractor`() {
        val stream = this::class.java.getResourceAsStream("/extractors.xml")
        val rulez = ExplicitXmlParser().parse(stream)

        val engine = ExplicitEngine(rulez)
        val result = engine.execute("simple string extractor")
        Assertions.assertEquals("[{one=A, two=B}]", result.toString())
    }

    @Test
    fun `simple number extractor`() {
        val stream = ExplicitXmlParser::class.java.getResourceAsStream("/extractors.xml")
        val rulez = ExplicitXmlParser().parse(stream)

        val engine = ExplicitEngine(rulez)
        val result = engine.execute("simple number extractor")
        Assertions.assertEquals("[{one=1, two=2}]", result.toString())
    }

    @Test
    fun `simple boolean extractor`() {
        val stream = ExplicitXmlParser::class.java.getResourceAsStream("/extractors.xml")
        val rulez = ExplicitXmlParser().parse(stream)

        val engine = ExplicitEngine(rulez)
        val result = engine.execute("simple boolean extractor")
        Assertions.assertEquals("[{one=true, two=false}]", result.toString())
    }

    @Test
    fun `simple variable extractor`() {
        val stream = ExplicitXmlParser::class.java.getResourceAsStream("/extractors.xml")
        val rulez = ExplicitXmlParser().parse(stream)

        val engine = ExplicitEngine(rulez)
        val result = engine.execute("simple variable extractor")
        Assertions.assertEquals("[{one=variable, two=extractor}]", result.toString())
    }

    @Test
    fun `simple function extractor`() {
        val stream = ExplicitXmlParser::class.java.getResourceAsStream("/extractors.xml")
        val rulez = ExplicitXmlParser().parse(stream)

        val engine = ExplicitEngine(rulez)
        val result = engine.execute("simple function extractor")
        Assertions.assertEquals("[{one=FUNCTION, two=EXTRACTOR}]", result.toString())
    }

}
