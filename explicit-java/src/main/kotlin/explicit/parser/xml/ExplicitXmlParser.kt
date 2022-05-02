package explicit.parser.xml

import explicit.api.extension.*
import explicit.parser.AntlrParser
import explicit.parser.ExplicitRule
import explicit.parser.ExplicitRules
import org.w3c.dom.Node
import org.w3c.dom.NodeList
import java.io.InputStream
import java.util.regex.Pattern
import javax.xml.parsers.DocumentBuilderFactory

class ExplicitXmlParser {

    companion object {
        val DOCUMENT_BUILDER = ThreadLocal.withInitial {
            DocumentBuilderFactory.newInstance().newDocumentBuilder()
        }!!
    }

    private fun toMapOfPatterns(map: Map<*, *>): Map<String, Pattern> {
        val patterns = java.util.HashMap<String, Pattern>()
        map.forEach { k, v -> patterns[k.toString()] = Pattern.compile(v.toString()) }
        return patterns
    }

    fun parse(source: String) = parse(java.io.FileInputStream(source))

    fun parse(stream: InputStream): ExplicitRules {
        val document = DOCUMENT_BUILDER.get().parse(stream)
        val root = document.firstChild

        val labelMap = parseLabels(root.childNodes)
        val mappings = parseMappings(root.childNodes)
        val patterns = parsePatterns(root.childNodes)
        val features = parseFeatures(root.childNodes)
        val acronyms = parseTokens(root.childNodes)
        return ExplicitRules(root.nodeName, parseRules(root.childNodes), labelMap, acronyms, mappings, toMapOfPatterns(patterns), features)
    }

    fun parseRule(node: Node): ExplicitRule {
        val eql = node.findText("eql")
        val ner = ArrayList<Map<String, String>>()

        // explicit entities
        ner.addAll(node.find("ner")
                .childNodes
                .filter { e -> e.nodeName == "entity" }
                .map { e ->
                    val entity = HashMap<String, String>()
                    e.findAttr("repeat").ifPresent { entity[":repeat"] = it }
                    e.findAttr("foreach").ifPresent { entity[":foreach"] = it }

                    e.childNodes
                            .filter { x -> x.nodeName == "#text" }
                            .filter { x -> x.nodeName == "#comment" }
                            .forEach { x -> entity[node.nodeName] = x.textContent }
                    entity
                }.fold(ArrayList()) { list, e ->
                    list.add(e)
                    list
                })

        val nerEntries = node.find("ner")
                .childNodes
                .filter { e -> e.nodeName != "entity" && e.nodeName != "#text" }

        // implicit entities
        if (nerEntries.isNotEmpty()) {
            ner.add(nerEntries
                    .map { e ->
                        val entity = HashMap<String, String>()
                        e.childNodes
                                .filter { x -> x.nodeName == "#text" }
                                .forEach { x -> entity[e.nodeName] = x.textContent }
                        entity
                    }.reduce { a, b ->
                        a.putAll(b)
                        a
                    })
        }

        val idx = getIdx(node)
        return ExplicitRule(AntlrParser().getTokens(eql), ner, idx)
    }

    private fun parseRules(list: NodeList): List<ExplicitRule> {
        return list.filter {
            !listOf("#text", "#comment", "mappings", "patterns", "postprocessing", "labels",
                    "features", "tokens").contains(it.nodeName)
        }.map(this::parseRule)
    }

    private fun parseLabels(list: NodeList): Map<String, String> {
        return list.filter { it.nodeName == "labels" }
                .flatMap { it.childNodes.toList() }
                .filter { it.nodeName != "#text" }
                .filter { it.nodeName != "#comment" }
                .map { mapOf(it.textContent to it.nodeName) }
                .fold(HashMap()) { a, b ->
                    a.putAll(b)
                    a
                }
    }

    private fun parseMappings(list: NodeList): Map<String, String> {
        return list.filter { it.nodeName == "mappings" }
                .flatMap { it.childNodes.toList() }
                .filter { it.nodeName != "#text" }
                .map { mapOf(it.findAttr("inbound").get() to it.findAttr("outbound").get()) }
                .fold(HashMap()) { a, b ->
                    a.putAll(b)
                    a
                }
    }

    private fun parsePatterns(list: NodeList): Map<String, String> {
        return list.filter { it.nodeName == "patterns" }
                .flatMap { it.childNodes.toList() }
                .filter { it.nodeName != "#text" }
                .filter { it.nodeName != "#comment" }
                .map { mapOf(it.nodeName to it.textContent) }
                .fold(HashMap()) { a, b ->
                    a.putAll(b)
                    a
                }
    }

    private fun parseFeatures(list: NodeList): Map<String, String> {
        return list.filter { it.nodeName == "features" }
                .flatMap { it.childNodes.toList() }
                .filter { it.nodeName != "#text" }
                .filter { it.nodeName != "#comment" }
                .map { mapOf(it.nodeName to it.textContent) }
                .fold(HashMap()) { a, b ->
                    a.putAll(b)
                    a
                }
    }

    private fun parseTokens(list: NodeList): ArrayList<ExplicitRules.Token> {
        return list.filter { it.nodeName == "tokens" }
                .flatMap { it.childNodes.toList() }
                .filter { it.nodeName != "#text" }
                .filter { it.nodeName != "#comment" }
                .map {
                    val pattern = it.findAttr("pattern").get()
                    val replacement = it.findAttr("replacement").orElse(null)
                    val boundary = it.findAttr("boundary").map { it.toBoolean() }.orElse(true)
                    val regex = it.findAttr("regex").map { it.toBoolean() }.orElse(false)
                    ExplicitRules.Token(pattern, replacement, boundary, regex)
                }
                .fold(ArrayList()) { a, b ->
                    a.add(b)
                    a
                }
    }

    private fun getIdx(node: Node): List<Int> {
        val nodeList = node.childNodes
        for (i in 0 until nodeList.length) {
            if (nodeList.item(i).nodeName === "idx") {
                val value = nodeList.item(i).textContent
                return value.split(",").map(String::trim).map(Integer::parseInt)
            }
        }
        return ArrayList()
    }

}
