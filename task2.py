from __future__ import annotations
from typing import Dict
from abc import ABC, abstractmethod


class Printer(ABC):
    _registry: Dict[str, Printer] = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if cls.model in Printer._registry:
            raise RuntimeError(f"Printer with model {cls.model} already defined")

        Printer._registry[cls.model] = cls

    @classmethod
    def get_by_model(cls, model: str):
        try:
            return cls._registry[model]()
        except KeyError:
            raise RuntimeError(f"No printer with model {model} found")

    @abstractmethod
    def print(self):
        """Printing behaviour must be overriden"""
        pass


class Canon(Printer):
    model = "Canon EL727"

    def print(self):
        return "Canon"


class HP(Printer):
    model = "HP MFP127"

    def print(self):
        return "HP"


class Order:
    def __init__(self, content: str, printer_model: str):
        self.content = content
        self.printer = Printer.get_by_model(printer_model)

    def print(self):
        return self.printer.print()
