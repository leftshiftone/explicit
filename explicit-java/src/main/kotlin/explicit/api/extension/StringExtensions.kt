package explicit.api.extension

import java.math.BigDecimal

fun String?.removeSurroundingNonNumeric(): String? {
    if (this == null)
        return null

    var index1 = 0
    var index2 = this.length

    val chars = this.toCharArray()
    for (c in chars) {
        if (Character.isDigit(c)) {
            break
        }
        index1++
    }
    chars.reverse()
    for (c in chars) {
        if (Character.isDigit(c)) {
            break
        }
        index2--
    }
    return this.substring(index1, index2)
}


fun String.getLevenshteinDistance(t: String): Int {
    var s = this
    var t = t
    if (s == null || t == null) {
        throw IllegalArgumentException("Strings must not be null")
    }

    var n = s.length
    var m = t.length

    if (n == 0) {
        return m
    } else if (m == 0) {
        return n
    }

    if (n > m) {
        // swap the input strings to consume less memory
        val tmp = s
        s = t
        t = tmp
        n = m
        m = t.length
    }

    val p = IntArray(n + 1)
    // indexes into strings s and t
    var i: Int // iterates through s
    var j: Int // iterates through t
    var upper_left: Int
    var upper: Int

    var t_j: Char // jth character of t
    var cost: Int

    i = 0
    while (i <= n) {
        p[i] = i
        i++
    }

    j = 1
    while (j <= m) {
        upper_left = p[0]
        t_j = t[j - 1]
        p[0] = j

        i = 1
        while (i <= n) {
            upper = p[i]
            cost = if (s[i - 1] == t_j) 0 else 1
            // minimum of cell to the left+1, to the top+1, diagonally left and up +cost
            p[i] = Math.min(Math.min(p[i - 1] + 1, p[i] + 1), upper_left + cost)
            upper_left = upper
            i++
        }
        j++
    }

    return p[n]
}

fun String.isNumeric(): Boolean {
    var str = this
    try {
        str = str.replace("\\.".toRegex(), "")
        str = if (str.endsWith(",-")) str.substring(0, str.length - 2) else str
        BigDecimal(str)
        return true
    } catch (e: Exception) {
        return false
    }

}
