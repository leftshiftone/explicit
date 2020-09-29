package explicit.de

import explicit.ExplicitEngine
import explicit.parser.xml.ExplicitXmlParser
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.DynamicTest
import java.io.FileInputStream

abstract class AbstractExplicitRulesTest(name:String) {

    private val engine = ExplicitEngine(ExplicitXmlParser()
            .parse(FileInputStream(System.getProperty("user.dir") + "/../src/main/resources/$name.xml")))

    protected fun register(vararg pairs:Pair<String, List<Map<String, Any>>>):List<DynamicTest> {
        return pairs.map { pair ->
            DynamicTest.dynamicTest(pair.first) {
                val result = engine.execute(pair.first)
                Assertions.assertEquals(pair.second.toString(), result.toString())
            }
        }
    }

}
