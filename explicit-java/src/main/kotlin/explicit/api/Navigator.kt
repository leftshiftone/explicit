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

package explicit.api

import java.util.*
import java.util.concurrent.atomic.AtomicInteger

/**
 * Utility class for Iterator instances.
 *
 * @since 1.0.0
 */
class Navigator<T>(val list: List<T>) : Iterator<T>, Iterable<T> {

    private val index = AtomicInteger()

    override fun hasNext() = index.get() < list.size

    override fun next() = list[index.getAndIncrement()]

    fun prev() = index.getAndDecrement()

    fun reset() = index.set(0)

    fun getIndex() = index.get()

    fun setIndex(index: Int) = this.index.set(index)

    fun getCurr() = list[index.get() - 1]

    fun getPrev(): Optional<T> {
        if (index.get() >= 2)
            return Optional.of(list[index.get() - 1])
        return Optional.empty()
    }

    fun getRemaining() = list.size - index.get()

    override fun iterator(): Iterator<T> {
        return object : Iterator<T> {
            private var index = 0
            override fun hasNext() = index < list.size
            override fun next() = list[index++]
        }
    }
}
