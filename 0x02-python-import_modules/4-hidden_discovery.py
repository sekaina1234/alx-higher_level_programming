#!/usr/bin/python3
import importlib
if __name__ == "__main__":
    module = importlib.import_module('hidden_4')
    names = dir(module)
    for name in names:
        if not name.startswith("__"):
            print(name)
