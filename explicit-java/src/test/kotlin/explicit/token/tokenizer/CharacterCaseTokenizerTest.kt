package explicit.token.tokenizer

import explicit.parser.ExplicitRules.Token
import explicit.parser.xml.ExplicitXmlParser
import org.junit.jupiter.api.Assertions
import org.junit.jupiter.api.Test
import java.io.FileInputStream

class CharacterCaseTokenizerTest {

    @Test
    fun test() {
        val tokenizer = CharacterCaseTokenizer()
        Assertions.assertEquals(listOf("abc", "/", "xyz").toString(), tokenizer.tokenize("abc/xyz").toString())
    }

    @Test
    fun test1() {
        val tokenizer = CharacterCaseTokenizer()
        Assertions.assertEquals(listOf("2018", ".").toString(), tokenizer.tokenize("2018.").toString())
    }

    @Test
    fun testAbbreviations() {
        val tokenizer = CharacterCaseTokenizer()
        Assertions.assertEquals(listOf("a", "früh", ".", "b", "spät", ".", "c").toString(), tokenizer.tokenize("a früh. b  spät. c").toString())
    }

    @Test
    fun testSpecialCharacterGroup() {
        val tokenizer = CharacterCaseTokenizer()
        Assertions.assertEquals(listOf("bis", "1", ".", "000", ",", "-", "euro").toString(), tokenizer.tokenize("bis 1.000,- euro").toString())
    }

    @Test
    fun testTokenizerWithCustomTokens() {
        val tokenizer = CharacterCaseTokenizer()
        val rulez = ExplicitXmlParser().parse(FileInputStream(System.getProperty("user.dir") + "/../src/main/resources/de/price.xml"))
        Assertions.assertEquals(listOf("bis", "1.000", "€", ".").toString(), tokenizer.tokenize("bis 1.000€.", rulez.tokens).toString())
        Assertions.assertEquals(listOf("bis", "1.000,-", "€").toString(), tokenizer.tokenize("bis 1.000,- €", rulez.tokens).toString())
    }

    @Test
    fun testTokenizerWithDatetimeTokens() {
        val tokenizer = CharacterCaseTokenizer()
        val rulez = ExplicitXmlParser().parse(FileInputStream(System.getProperty("user.dir") + "/../src/main/resources/de/datetime.xml"))
        Assertions.assertEquals(listOf("ich", "suche", "von", "9.2.", "bis", "16.2", "2018").toString(), tokenizer.tokenize("ich suche von 9.2. bis 15/16.2 2018", rulez.tokens).toString())
    }

    @Test
    fun testTokenizeCompoundWord() {
        val tokenizer = CharacterCaseTokenizer()
        Assertions.assertEquals(listOf("sommer", "regen"), tokenizer.tokenize("sommerregen", listOf(Token(
                pattern = "sommer",
                replacement = "",
                boundary = true,
                regex = true))))
    }

}
