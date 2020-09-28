package explicit.conversion

import explicit.api.IConversion
import explicit.api.IConversionBinding

class BooleanConversion(private val bool:Boolean) : IConversion {
    override fun extract(binding: IConversionBinding)  = bool
}
