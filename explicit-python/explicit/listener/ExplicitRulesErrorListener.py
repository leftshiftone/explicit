from antlr4.error.ErrorListener import ErrorListener


class ExplicitRulesErrorListener(ErrorListener):

    def __init__(self):
        self.error = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error = "compilation error: " + str(msg) + "\nat line " + str(line) + " char " + str(column)
