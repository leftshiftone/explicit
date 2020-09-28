package explicit.conversion

import explicit.api.IConversion
import explicit.api.IConversionBinding
import java.util.*

class VariableConversion(private val name:String) : IConversion {
    override fun extract(binding: IConversionBinding) = binding.getVariable(name) ?: Optional.empty<Any>()
}
