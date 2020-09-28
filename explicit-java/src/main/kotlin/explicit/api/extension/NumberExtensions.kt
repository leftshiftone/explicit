package explicit.api.extension

import java.io.CharArrayWriter
import java.math.BigDecimal

fun Any.toNumber(): BigDecimal {
    var str = this.toString().replace(".", "")
    str = if (str.endsWith(",-")) str.substring(0, str.length - 2) else str
    return BigDecimal(str)
}

fun Any.toInt() = this.toNumber().toInt()
fun Any.toLong() = this.toNumber().toLong()
fun CharArrayWriter.getAndReset(c: Int): String {
    val result = this.toString()
    this.reset()
    this.write(c)
    return result
}
