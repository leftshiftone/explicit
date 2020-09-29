from typing import Dict, List

from xml.dom import minidom
from xml.dom.minidom import Element, Text

from explicit_nlu.parser import ExplicitRule
from explicit_nlu.parser.AntlrParser import AntlrParser
from explicit_nlu.parser.ExplicitRules import ExplicitRules, Token


class ExplicitXmlParser:
    def parse(self, file_path: str) -> ExplicitRules:
        xdom = minidom.parse(file_path)
        root = xdom.childNodes[0]

        return ExplicitRules(root.tagName,
                             self._parse_rules(root),
                             self._parse_labels(root),
                             self._parse_tokens(root),
                             self._parse_mappings(root),
                             self._parse_patterns(root),
                             self._parse_features(root))

    def _parse_rules(self, root: Element) -> List[ExplicitRule]:
        result: List[ExplicitRule] = []
        rules = root.getElementsByTagName("rule")

        for rule in rules:
            eql = self._to_text(rule.getElementsByTagName("eql")[0])
            idx = [self._to_text(x) for x in rule.getElementsByTagName("idx")]
            ner: List[Dict[str, str]] = []

            for element in rule.getElementsByTagName("ner"):

                # explicit entities
                for entity in element.childNodes:
                    if isinstance(entity, Text):
                        continue
                    if entity.tagName != "entity":
                        continue

                    entity_map: Dict[str, str] = {}

                    if entity.hasAttribute("repeat"):
                        entity_map[":repeat"] = entity.getAttribute("repeat")
                    if entity.hasAttribute("foreach"):
                        entity_map[":foreach"] = entity.getAttribute("foreach")

                    for attribute in entity.childNodes:
                        entity_map[attribute.tagName] = self._to_text(attribute)

                    ner.append(entity_map)

                # implicit entities
                entity_map: Dict[str, str] = {}
                for entity in element.childNodes:
                    if isinstance(entity, Text):
                        continue
                    if entity.tagName == "entity":
                        continue

                    for attribute in entity.childNodes:
                        entity_map[entity.tagName] = self._to_text(attribute)

                if len(entity_map) > 0:
                    ner.append(entity_map)

            result.append(ExplicitRule(AntlrParser().get_tokens(eql), ner, list(map(lambda x: int(x), idx))))

        return result

    def _parse_labels(self, xdom: Element) -> Dict[str, str]:
        result: Dict[str, str] = dict()
        labels = xdom.getElementsByTagName("labels")

        for label in labels:
            for node in label.childNodes:
                if not isinstance(node, Text):
                    result[self._to_text(node)] = node.tagName

        return result

    def _parse_mappings(self, xdom: Element) -> Dict[str, str]:
        result: Dict[str, str] = dict()
        mappings = xdom.getElementsByTagName("mappings")

        for mapping in mappings:
            for node in mapping.childNodes:
                if not isinstance(node, Text):
                    result[node.getAttribute("inbound")] = node.getAttribute("outbound")

        return result

    def _parse_patterns(self, xdom: Element) -> Dict[str, str]:
        result: Dict[str, str] = dict()
        patterns = xdom.getElementsByTagName("patterns")

        for pattern in patterns:
            for node in pattern.childNodes:
                if not isinstance(node, Text):
                    result[node.tagName] = self._to_text(node)

        return result

    def _parse_features(self, xdom: Element) -> Dict[str, str]:
        result: Dict[str, str] = dict()
        patterns = xdom.getElementsByTagName("features")

        for pattern in patterns:
            for node in pattern.childNodes:
                if not isinstance(node, Text):
                    result[node.tagName] = self._to_text(node)

        return result

    def _parse_tokens(self, xdom: Element) -> List[Token]:
        result: List[Token] = list([])
        tokens = xdom.getElementsByTagName("tokens")

        for token in tokens:
            for node in token.childNodes:
                if not isinstance(node, Text):
                    if node.nodeName != "#text" and node.nodeName != "#comment":
                        result.append(Token(node.getAttribute("pattern"),
                                            node.getAttribute("replacement"),
                                            str(node.getAttribute("boundary")) != "false",
                                            str(node.getAttribute("regex")) == "true"))

        return result

    def _to_text(self, node: Element) -> str:
        if node.nodeType == node.TEXT_NODE:
            return node.data
        else:
            text_string = ""
            for child_node in node.childNodes:
                text_string += self._to_text(child_node)
            return text_string
