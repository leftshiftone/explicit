package explicit.parser

import explicit.api.IToken

data class ExplicitRule(val rule:List<IToken>, val ner:List<Map<String, String>>, val idx: List<Int>)
