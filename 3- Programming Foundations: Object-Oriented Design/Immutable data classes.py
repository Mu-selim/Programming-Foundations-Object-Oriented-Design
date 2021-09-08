from dataclasses import dataclass

# 'The "frozen' parameter makes the class immutable """
@dataclass(frozen = True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    """
    def tryToChange(self, value):
        self.value2 = value
    """

obj = ImmutableClass()
print(obj.value1)

""" attempting to change the value of an immutable class throws an exception """

# obj.value1 = "Value Change" --> this will cause an error as it is Immutable

""" even functions within the class can't change anything """
"""
obj.tryToChange(40) --> this will cause an error as it is Immutable
"""
print(obj.value2)