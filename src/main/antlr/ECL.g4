/*
 * Lexer Rules
 */

grammar ECL;

ROUND_LEFT  : '(';
ROUND_RIGHT : ')';
BOOLEAN    : 'true' | 'false';
COMMA       : ',';
STRING     : '"' StringCharacter* '"';
NUMBER     : [0-9]+;
DOLLAR     : '$';
IDENTIFIER : Letter LetterOrDigit*;

fragment Digit           : '-'?[0-9];
fragment Letter          : [a-zA-Z];
fragment LetterOrDigit   : [a-zA-Z0-9_];
fragment StringCharacter :	~'"';

//
// Whitespace and comments
//
WHITESPACE   : [ \t\r\n\u000C]+ -> skip;

/*
 * Parser Rules
 */
extractor : (string | number | bool_ | variable | function)+ EOF;
string    : STRING;
number    : NUMBER;
bool_     : BOOLEAN;
variable  : DOLLAR IDENTIFIER;
function  : IDENTIFIER ROUND_LEFT (argument (COMMA argument)*)? ROUND_RIGHT;
argument  : (string | number | bool_ | variable | function);
