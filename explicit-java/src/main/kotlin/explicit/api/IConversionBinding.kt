package explicit.api

interface IConversionBinding {
    fun registerVariable(name:String, value:Any)
    fun registerFunction(name:String, function:(args:List<Any>) -> Any)

    fun getVariable(name:String):Any?
    fun getFunction(name:String):(List<Any>) -> Any
}
