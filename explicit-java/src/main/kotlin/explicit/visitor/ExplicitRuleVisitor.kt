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

import explicit.antlr.EQLBaseVisitor
import explicit.antlr.EQLParser.*
import explicit.api.IToken
import explicit.token.*
import explicit.token.Optional
import java.util.*

class ExplicitRuleVisitor : EQLBaseVisitor<List<IToken>>() {

    override fun visitNot_(ctx: Not_Context) = listOf(Not(super.visitNot_(ctx)[0]))

    override fun visitLike(ctx: LikeContext) = listOf(Like(ctx.text.substring(1)))

    override fun visitGroup(ctx: GroupContext): List<IToken> {
        val sublist = ctx.children.subList(1, ctx.children.size - 1)

        val list = sublist.flatMap { e -> super.visit(e) }
        return listOf(Group(list))
    }

    override fun visitAtomic(ctx: AtomicContext): List<IToken> {
        val sublist = ctx.children.subList(1, ctx.children.size - 1)

        val list = sublist.flatMap { e -> super.visit(e) }
        return listOf<IToken>(Atomic(list))
    }

    override fun visitText(ctx: TextContext) = listOf(Text(ctx.text))

    override fun visitWildcard(ctx: WildcardContext) = listOf(Wildcard())

    override fun visitSlot(ctx: SlotContext) = listOf(Slot(ctx.getChild(1).text))

    override fun visitOptional(ctx: OptionalContext) = listOf(Optional(super.visit(ctx.getChild(0))[0]))

    override fun visitLabel(ctx: LabelContext) = listOf(Label(super.visit(ctx.getChild(1))[0]))

    override fun visitAlias(ctx: AliasContext) = listOf(Alias(ctx.getChild(2).text, super.visit(ctx.getChild(0))[0]))

    override fun visitRegex(ctx: RegexContext): List<IToken> {
        val sublist = ctx.children.subList(1, ctx.children.size - 1)
        val regex = sublist.map { it.getText() }.fold("") { a, b -> a + b }
        return listOf<IToken>(Regex(regex))
    }

    override fun visitEscaped(ctx: EscapedContext) = listOf(Escaped(ctx.text.substring(1)))

    /**
     * {@inheritDoc}
     */
    override fun aggregateResult(aggregate: List<IToken>?, nextResult: List<IToken>?): List<IToken> {
        val list = ArrayList<IToken>()
        if (aggregate != null)
            list.addAll(aggregate)
        if (nextResult != null)
            list.addAll(nextResult)
        return list
    }

}
