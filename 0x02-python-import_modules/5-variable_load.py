#!/usr/bin/python3

if __name__ == "__main__":
    import variable_load_5
    

    names = dir(variable_load_5)
    for name in names:
        if name == 'a':
            value = getattr(variable_load_5, name)
            print(value)
