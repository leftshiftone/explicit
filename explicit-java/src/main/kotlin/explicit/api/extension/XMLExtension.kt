package explicit.api.extension

import org.w3c.dom.Node
import org.w3c.dom.NodeList
import java.util.*

fun NodeList.toList(): List<Node> {
    return IntRange(0, this.length - 1).map { this.item(it) }
}

fun NodeList.filter(function: (Node) -> Boolean): List<Node> {
    return IntRange(0, this.length - 1)
            .map { this.item(it) }
            .filter { e -> function(e) }
}

fun Node.find(tag: String): Node {
    val nodeList = this.childNodes
    for (i in 0 until nodeList.length - 1) {
        if (nodeList.item(i).nodeName === tag) {
            return nodeList.item(i)
        }
    }
    throw RuntimeException("An error occurred while parsing GQL file. Check validity.")
}

fun Node.findAttr(name: String): Optional<String> {
    if (this.attributes == null)
        return Optional.empty()
    val attrNode = this.attributes.getNamedItem(name)
    return if (attrNode != null) Optional.of(attrNode.textContent) else Optional.empty()
}

fun Node.findText(tag: String): String {
    return this.find(tag).textContent
}
