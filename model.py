from dataclasses import dataclass


@dataclass
class Product:
    ref:str
    description:str
    price:float