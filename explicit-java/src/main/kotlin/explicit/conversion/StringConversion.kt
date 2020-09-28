package explicit.conversion

import explicit.api.IConversion
import explicit.api.IConversionBinding

class StringConversion(private val str:String) : IConversion {
    override fun extract(binding: IConversionBinding)  = str.substring(1, str.length - 1)
}
