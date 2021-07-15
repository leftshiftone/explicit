# explicit

[![CircleCI branch](https://img.shields.io/circleci/project/github/leftshiftone/explicit/master.svg?style=flat-square)](https://circleci.com/gh/leftshiftone/explicit)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/leftshiftone/explicit.svg?style=flat-square)](https://github.com/leftshiftone/explicit/tags)
[![Bintray](https://img.shields.io/badge/dynamic/json.svg?label=bintray&query=name&style=flat-square&url=https%3A%2F%2Fapi.bintray.com%2Fpackages%2Fleftshiftone%2Fexplicit%2Fone.leftshift.explicit.explicit-java%2Fversions%2F_latest)](https://bintray.com/leftshiftone/explicit/one.leftshift.explicit.explicit-java/_latestVersion)
[![PyPI](https://img.shields.io/pypi/v/explicit-nlu?style=flat-square)](https://pypi.org/project/explicit-nlu/)


Explicit is a cross platform library for rule based named entity recognition.
Although machine learning is the often preferred way to solve this kind of tasks
a rule based approach can lead for specific tasks to faster and more accurate results.

## Usage Named Entity Recognition (Kotlin)
````kotlin
val config = ExplicitXmlParser().parse("./explicit-config.xml")
val engine = ExplicitEngine(config)

engine.execute("a sentence for named entity recognition")
````

## Supported programming languages
* Java
* Python

## Setup
In order to generate the ANTLR sources invoke the gradle tasks generateGrammarSource and generateGrammarSourcePython.

# Explicit Configuration File
For the use of named entity recognition, a configuration file is used to define the explicit rules.
The library has a canonical data format where configuration from different file formats can be transferred to.
At the moment only the xml file format is supported.

An explicit configuration file starts with an <explicit /> tag which contains the name of the NER entity class.

````xml
<explicit name="price" />
````

## Rules
Explicit configuration files can contain multiple explicit rules.
Each rule defines an EQL (explicit query language) expression in combination with a group of ECL
(explicit conversion language) expressions.
If the EQL expression matches the input text, each ERL expression is resolved to a variable value
which is stored and returned as a result value.

For example the following rule matches input texts like **"100 euro"** or **"20 €"** and stores the variables
amount as well as currency in the result object.

````xml
<rule>
    <eql>{number}:amount #currency</eql>
    <ner>
        <amount>toNumber($amount)</amount>
        <currency>first($currency, "euro")</currency>
    </ner>
</rule>
````

## Tokens

The tokenizer splits the text at every whitespace, special character and char type switch.
For example the text **"abc 123 abc§$%"** is tokenized to **[abc, 123, abc, §, $, %]**.
This behaviour can be extended by configuring custom tokens. A token can be a static character sequence
or a regex. Tokens can automatically be replaced with a "replacement" character sequence. Also tokens
can be defined as a boundary token which means that the token is allowed to be at the end of the text.

**Token attributes:**
pattern:     the token pattern
replacement: the character sequence which replaces the matched token
regex:       indicates whether the pattern is a regex (default false)
boundary:    indicates whether the matched token can be at the end of the text (default true)

````xml
<tokens>
    <token pattern="p.p" replacement="pro person" />
    <token pattern="[0-9]+\.[0-9]+,\-" regex="true" />
    <token pattern="früh." boundary="false" />
    <token pattern="spät." boundary="false" />
</tokens>
````

## Labels
Labels can be used to apply a label tag on a static character sequence. This labels can be used within the
explicit query language by using the hashtag prefix e.g. #labelName

So a input text **"ten euro"** matches the EQL expression **"ten #currency"**.

````xml
<labels>
    <currency>euro</currency>
    <currency>€</currency>
    <currency>eur</currency>
    <currency>dollar</currency>
    <currency>$</currency>
</labels>
````

#Mappings
Mappings can be used to convert an input character sequence to another character sequence. This can be used
in combination with the alias EQL token. For example the alias in the EQL pattern **"ten #currency:currency"** stores 
the matching character sequence at default. This character sequence can be converted by a mapping configuration.

````xml
<mappings>
    <mapping inbound="€" outbound="euro" />
    <mapping inbound="eur" outbound="euro" />
    <mapping inbound="$" outbound="dollar" />
</mappings>
````

## Features
Features defines static entities which can be used in an ECL expression.

For example: first($currency, $defaultCurrency)

````xml
<features>
    <defaultCurrency>euro</defaultCurrency>
</features>
````

## Patterns
Patterns can be used to define global regex values. This regex values can be resolved by using Slot tokens.

````xml
<patterns>
    <dateDMY>[0-9]{1,2}[\.\\/\-][0-9]{1,2}[\.\\/\-] ?[0-9]{2,4}[\.\\/\-]?</dateDMY>
    <dateYDM>[0-9]{2,4}[\.\\/\-][0-9]{1,2}[\.\\/\-] ?[0-9]{1,2}[\.\\/\-]?</dateYDM>
    <dateDM>[0-9]{1,2}[\.\\/\-][0-9]{1,2}[\.\\/\-]?</dateDM>
    <year>[0-9]{4}</year>
    <dateNumber2>[0-9]{1,2}</dateNumber2>
    <dateNumber4>[0-9]{4}</dateNumber4>
</patterns>
````

## Explicit Query Language (EQL)
EQL is an expression language which is used to describe patterns in a natural text. So the EQL defines token types 
of a character sequence which has to be present in order to match the expression. The EQL format
is composed of different tokens types.
 
### Alias
The alias token can be used to give a certain part of a text an alias name. This name can be used as a reference
to the part when using it in an ECL expression. An alias token matches with a text token when the
token before the colon equals the text input.
 
 ````
text:aliasName
````

### Atomic
By the use of an atomic token a set of text tokens can be grouped to an atomic unit. An atomic token matches a 
text token when the entire atomic is equal to the text token.

 ````
(all as one)
````

### Escaped
If one of the special symbols of the EQL format like :!~? should be used as a part of the query language, the
symbol has to be escaped by a backslash.

````
\: \! \~ \?
````

### Group
A group segment can be used to define a collection of alternatives. This group matches to a specific text token
when one element of the group is equal to the input text.

````
[a b c d]
````

### Label
A label token can be used to reference a predefined label. This token matches if the input text is equal to the 
predefined label value. See **Explicit Configuration File/Labels**

````
#customLabel
````

### Like
This token type is used to apply a fuzzy text comparison to the input string. This token matches if the input
text levenshtein distance is lower equals 1.

````
~text
````

### Not
This token type is used to define if an input text token must not be present in the character sequence.

````
!text
````

### Optional
An optional token type can be used to define optional tokens within the input text sequence.

````
text?
````

### Regex
The regex token can be used to define an in-place regex expression.

````
`[a-z]*`
````

### Slot
A slot token type can be used to define a placeholder within the EQL expression. The token matches if one of the 
following conditions are met:

 * The input character sequence is numeric and the {number} slot is used
 * The input character sequence is mapped to an numeric value (see **Explicit configuration File/mappings**) and the {number} slot is used
 * The slot name matches the input character sequence
 * The input character sequence matches a predefined pattern

````
{text}
````

### Text
This token type matches if the input text sequence is equal to the token.

````
text
````

### Wildcard
A wildcard can be used to skip tokens in the input character sequence until another token matches. 

````
*
````

# Explicit Conversion Language (ECL)
The explicit conversion language is used to convert an input text which matches an EQL expression to ner entities.
Within an ECL expression matched EQL alias tokens can be referenced with a leading Dollar symbol before the name
e.g. $aliasName

**Example:**
input -> 100 euro
EQL   -> {number}:amount euro
ECL   -> $amount

The ECL expression returns 100

## ECL Build-in-functions
Within ECL expressions build-in-functions can be used.

````javascript
add(a, b) // can be used to add numeric value b to numeric value a
sub(a, b) // can be used to subtract numeric value b to numeric value a
mul(a, b) // can be used to multiply numeric value b with numeric value a
div(a, b) // can be used to divide numeric value a by b
uppercase(s) // converts the string value to an uppercase string
lowercase(s) // converts the string value to a lowercase string
toNumber(s) // converts the string value to a numeric value
first(a, b) // returns the first value which is not null
ternary(e, a, b) // returns a if e is true otherwise returns b
isPresent(s) // returns true if the variable key s is present within the variables
date(day, month, year)  // converts the day, month and year values to a date instance
addWeeks(date, amount) // increment/decrement the week value of the date amount times
toDate(s) // converts the string to a date instance. The string must match the pattern day.month.year
toDate(s, y) // converts the string to a date instance with y as the year value. s must match the pattern day.month
lastDayOfMonth(m) // returns the last day of the given month m
getYear(d) // returns the year value of the date value d
curMonth() // returns the current month value of the system date
substringAfter(s, i) // returns the substring of s beginning at index i 
````

## Development

### Release
Releases are triggered locally. Just a tag will be pushed and CI takes care of the rest.

#### Major
Run `./gradlew final -Prelease.scope=major` locally.

#### Minor
Run `./gradlew final -Prelease.scope=minor` locally.

#### Patch
Must be released from branch (e.g. `release/1.0.x`)

Run `./gradlew final -Prelease.scope=patch` locally.
