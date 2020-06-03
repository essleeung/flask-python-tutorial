from pymongo import MongoClient

import datetime
import pprint

client = MongoClient()
db = client.python_tutorial
collection = db.operators

floor_div = {
    "name": "Floor Division",
    "description": "Division that rounds down to the nearest integer. Also known as integer division.",
    "symbol": "//",
    "example": "3 // 2 == 1",
    "uses": "A common situation we might see this operator is when we need to calcuate a list index, which will need to be a whole number. For example, perhaps we are trying to find the middle index of a list, but there are an even number of elements. In this case, we could use floor division to select the leftmost element in the list by default."
}

add = {
    "name": "Addition",
    "description": "Arithmetic operator used with numeric values to find the remainder after dividing one number by another.",
    "symbol": "%",
    "example": "100 % 9 == 1",
    "uses": "A common arithmetic operator to sum up two values."
}

modulus = {
    "name": "Modulus",
    "description": "Arithmetic operator used with numeric values to find the remainder.",
    "symbol": "+",
    "example": "3 + 2 == 5",
    "uses": "Common when trying to split pieces of pizza in a group  🍕."
}

db.operators.insert_many([floor_div, add, modulus])