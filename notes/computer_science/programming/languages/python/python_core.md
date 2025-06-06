# Python core

## **Strings**

In Python string of **str** type represents **single characters** each of which is an object of str type with length is **1**. This means that each character in string is an individual object of **str** type whether how much string contain characters

## Generators

You can omit the parentheses surrounding **generator-expression** if expression is used as **single** argument of function.

```python
>>> sum((x * 2 for x in range(10)))
90
## Compare with
>>> sum(x * 2 for x in range(10))
90
```

## Classes

### Dataclasses

#### Converting to tuple or dictionary

```python
from dataclass import astuple, asdict

ahmed = Person()
print(astuple(ahmed)
# ('Ahmed', 'Besbes', 30, 'Data Scientist')

print(asdict(ahmed)
# {'first_name': 'Ahmed',
# 'last_name': 'Besbes',
# 'age': 30,
# 'job': 'Data Scientist'}
```


#### Frozen objects

You can create `frozen` read-only objects

```python
@dataclass(frozen=True)
class Person:
     first_name: str = "Ahmed"
     last_name: str = "Besbes"
     age: int = 30
     job: str = "Data Scientist"
```
If you can change the attribute of frozen instance to new value you will get the error `FrozenInstanceError`



## Debugging

```python
>>> print(f"{widget_count=}")
widget_count=9001
```
We aren’t limited to variable names with `=`. We can use any expression:
```python
>>> print(f"{(widget_count / factories)=}")
(widget_count / factories)=750.0833333333334
```

## Scope

If your function starts with underscore like `_some_name` then it will not be imported by `from <module_name> import *`

## Modules

something about module reload

```python
import importlib

importlib.reload(foo)
```


## Errors and Exceptions
### Exceptions
Ordering of `try/except/else/finnaly`
![[assets/drawing-python-exceptions-ordering.excalidraw]]

## Data

[Check...](https://github.com/mCodingLLC/VideosSampleCode/blob/master/videos/079_which_dataclass_is_best/dataclasses_comparison.py)

![](./attachments/python_data_store_structures_pic.png)
