package explicit.conversion

import explicit.api.IConversion
import explicit.api.IConversionBinding

class FunctionConversion(private val name:String, private val args:List<IConversion>) : IConversion {
    override fun extract(binding: IConversionBinding):Any {
        return binding.getFunction(name)(args.map { it.extract(binding) })
    }
}
