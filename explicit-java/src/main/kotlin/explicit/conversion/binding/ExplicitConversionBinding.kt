package explicit.conversion.binding

import explicit.api.IConversionBinding
import explicit.api.extension.removeSurroundingNonNumeric
import explicit.api.extension.toInt
import explicit.api.extension.toLong
import explicit.api.extension.toNumber
import java.math.RoundingMode
import java.time.LocalDateTime
import java.time.temporal.TemporalAdjusters
import java.util.*

class ExplicitConversionBinding(variables: Map<String, Any> = mapOf()) : IConversionBinding {

    private val variables = HashMap(variables)
    private val functions = HashMap<String, (List<Any>) -> Any>()

    init {
        functions["add"] = { it[0].toNumber().add(it[1].toNumber()) }
        functions["sub"] = { it[0].toNumber().subtract(it[1].toNumber()) }
        functions["mul"] = { it[0].toNumber().multiply(it[1].toNumber()) }
        functions["div"] = { it[0].toNumber().divide(it[1].toNumber(), RoundingMode.FLOOR) }
        functions["uppercase"] = { it[0].toString().toUpperCase() }
        functions["lowercase"] = { it[0].toString().toLowerCase() }
        functions["toNumber"] = { it[0].toNumber() }
        functions["first"] = { it.first { e -> e !is Optional<*> } }
        functions["ternary"] = { if (it[0].toString().toBoolean()) it[1] else it[2] }
        functions["isPresent"] = { variables.containsKey(it[0].toString()) }
        functions["date"] = {
            LocalDateTime.of(it[2].toInt(), it[1].toInt(), it[0].toInt(), 0, 0)
        }
        functions["addWeeks"] = { (it[0] as LocalDateTime).plusWeeks(it[1].toLong()) }
        functions["toDate"] = { args ->
            if (args.size == 2) {
                val delimiter = if (args[0].toString().contains("/")) "/" else "."
                val array = args[0].toString().split(delimiter)

                var year = ((array[2]).removeSurroundingNonNumeric()!!.toInt())
                year = if (year < 100) year + 2000 else year

                LocalDateTime.of(year, array[1].toInt(), array[0].removeSurroundingNonNumeric()!!.toInt(), 0, 0)
            } else {
                val delimiter = if (args[0].toString().contains("/")) "/" else "."
                val array = args[0].toString().split(delimiter)

                var year = args[2].toInt()
                year = if (year < 100) year + 2000 else year

                LocalDateTime.of(year, array[1].toInt(), array[0].removeSurroundingNonNumeric()!!.toInt(), 0, 0)
            }
        }
        functions["lastDayOfMonth"] = {
            val date = LocalDateTime.of(it[1].toInt(), it[0].toInt(), 1, 0, 0).with(TemporalAdjusters.lastDayOfMonth())
            date.dayOfMonth
        }
        functions["getYear"] = { it -> (it[0] as LocalDateTime).year }
        functions["curMonth"] = {LocalDateTime.now().month.value}
        functions["substringAfter"] = {it[0].toString().substringAfter(it[1].toString())}
    }

    override fun registerVariable(name: String, value: Any) {
        variables[name] = value
    }

    override fun registerFunction(name: String, function: (args: List<Any>) -> Any) {
        functions[name] = function
    }

    override fun getVariable(name: String) = variables[name]

    override fun getFunction(name: String): (List<Any>) -> Any {
        if (!functions.containsKey(name))
            throw RuntimeException("no function $name found")
        return functions[name]!!
    }
}
