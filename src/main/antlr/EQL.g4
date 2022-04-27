/*
 * Lexer Rules
 */

grammar EQL;

WILDCARD    : '*';
OPTIONAL    : '?';
TILDE       : '~';
COLON       : ':';
BACKSLASH   : '\\';
HASHTAG     : '#';
BOOLEAN    : 'true' | 'false';
ROUND_LEFT  : '(';
ROUND_RIGHT : ')';
CURLY_LEFT  : '{';
CURLY_RIGHT : '}';
TEXT        : ( [\p{Alphabetic}0-9\u20AC'/-] | COMMA | DOT )+;
COMMA       : ',';
DOT         : '.';
ESCAPED    : BACKSLASH ( COLON | OPTIONAL | TILDE | WILDCARD );

fragment Digit           : '-'?[0-9];
fragment Letter          : [a-zA-Z];
fragment LetterOrDigit   : [a-zA-Z0-9_];
fragment StringCharacter :	~'"';

//
// Whitespace and comments
//
WHITESPACE   : [ \t\r\n\u000C]+ -> skip;
LINE_COMMENT : '//' ~[\r\n]*    -> skip;
SEMICOLON    : ';'              -> skip;

/*
 * Parser Rules
 */
// tokenization
token     : (text | escaped | wildcard | optional | label | group | like | not_ | slot | alias | atomic | regex)* EOF;
escaped   : ESCAPED;
group     : '[' (text | not_ | like)* ']';
like      : TILDE text;
text      : TEXT;
not_      : '!'(text | group | like);
wildcard  : WILDCARD;
optional  : (text | group | like | label | slot | atomic)OPTIONAL;
alias     : (text | group | like | label | slot | optional | atomic | wildcard) COLON TEXT;
label     : HASHTAG text;
slot      : CURLY_LEFT TEXT CURLY_RIGHT;
// quantor   : CURLY_LEFT DIGIT (COMMA DIGIT)? CURLY_RIGHT;
atomic    : '(' (text | like)* ')';
regex     : '`' (~'`' | '+' | '^')+ '`';
