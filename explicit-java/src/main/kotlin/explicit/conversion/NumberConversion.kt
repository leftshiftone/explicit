package explicit.conversion

import explicit.api.IConversion
import explicit.api.IConversionBinding

class NumberConversion(private val num:Number) : IConversion {
    override fun extract(binding: IConversionBinding)  = num
}
