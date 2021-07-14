import calendar
from datetime import date, timedelta
from datetime import datetime
from typing import Dict, Any, Callable, List

from explicit_nlu.api import IConversionBinding
from explicit_nlu.api.support import Strings


def to_date(args):
    if args[1] == "DMY":
        array = str(args[0]).split("." if "." in args[0] else "/")
        return datetime(int(array[2]) + 2000 if len(array[2]) == 2 else int(array[2]), int(array[1]), int(array[0]))
    if args[1] == "DM":
        array = str(args[0]).split(".")
        return datetime(int(args[2]), int(array[1]), int(array[0]))
    raise ValueError("cannot parse " + str(args) + " to date")


class ExplicitConversionBinding(IConversionBinding):

    def __init__(self, variables: Dict[str, Any]):
        self.variables = dict(variables)
        self.functions: Dict[str, Callable[[List[Any]], Any]] = {
            "add": lambda args: float(args[0]) + float(args[1]),
            "sub": lambda args: float(args[0]) - float(args[1]),
            "mul": lambda args: float(args[0]) * float(args[1]),
            "div": lambda args: float(args[0]) / float(args[1]),
            "uppercase": lambda args: str(args[0]).upper(),
            "lowercase": lambda args: str(args[0]).lower(),
            "toNumber": lambda args: Strings.to_number(args[0]),
            "first": lambda args: next(x for x in args if not x is None),
            "ternary": lambda args: args[1] if args[0] else args[2],
            "isPresent": lambda args: args[0] in self.variables,
            "date": lambda args: datetime(int(args[2]), int(args[1]), int(args[0])),
            "addWeeks": lambda args: args[0] + timedelta(days=int(args[1]) * 7),
            "lastDayOfMonth": lambda args: calendar.monthrange(int(args[1]), int(args[0]))[1],
            "getYear": lambda args: args[0].year,
            "curMonth": lambda args: date.today().month,
            "curDate": lambda args: date.today(),
            "substringAfter": lambda args: args[0][args[0].index(args[1]) + len(args[1]):],
            "toDate": to_date,
            "removeWhitespace": lambda args: args[0].replace(" ", ""),
            "replace": lambda args: args[0].replace(args[1], args[2]),
            "concat": lambda args: "".join(args),
        }

    def register_variable(self, name: str, value: Any):
        self.variables[name] = value

    def register_function(self, name: str, function: Callable[[List[Any]], Any]):
        self.functions[name] = function

    def get_variable(self, name: str):
        return self.variables[name] if name in self.variables else None

    def get_function(self, name: str) -> Callable[[List[Any]], Any]:
        if name in self.functions:
            return self.functions[name]
        raise ValueError("no function '" + name + "' found")
