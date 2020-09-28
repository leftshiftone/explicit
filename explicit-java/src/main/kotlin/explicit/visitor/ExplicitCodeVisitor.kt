/*
 * Copyright (c) 2016-2018, Leftshift One
 * __________________
 * [2018] Leftshift One
 * All Rights Reserved.
 * NOTICE:  All information contained herein is, and remains
 * the property of Leftshift One and its suppliers,
 * if any.  The intellectual and technical concepts contained
 * herein are proprietary to Leftshift One
 * and its suppliers and may be covered by Patents,
 * patents in process, and are protected by trade secret or copyright law.
 * Dissemination of this information or reproduction of this material
 * is strictly forbidden unless prior written permission is obtained
 * from Leftshift One.
 */

package explicit.visitor

import explicit.antlr.ECLBaseVisitor
import explicit.antlr.ECLParser
import explicit.api.IConversion
import explicit.conversion.*
import java.math.BigDecimal
import java.util.*

class ExplicitCodeVisitor : ECLBaseVisitor<List<IConversion>>() {

    override fun visitString(ctx: ECLParser.StringContext) = listOf(StringConversion(ctx.text))
    override fun visitNumber(ctx: ECLParser.NumberContext) = listOf(NumberConversion(BigDecimal(ctx.text)))
    override fun visitBool_(ctx: ECLParser.Bool_Context) = listOf(BooleanConversion(ctx.text!!.toBoolean()))
    override fun visitVariable(ctx: ECLParser.VariableContext) = listOf(VariableConversion(ctx.getChild(1).text))
    override fun visitFunction(ctx: ECLParser.FunctionContext): List<IConversion> {
        return listOf(FunctionConversion(ctx.getChild(0).text, super.visitFunction(ctx)))
    }

    /**
     * {@inheritDoc}
     */
    override fun aggregateResult(aggregate: List<IConversion>?, nextResult: List<IConversion>?): List<IConversion> {
        val list = ArrayList<IConversion>()
        if (aggregate != null)
            list.addAll(aggregate)
        if (nextResult != null)
            list.addAll(nextResult)
        return list
    }

}
