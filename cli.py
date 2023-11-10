"""
### cli.py

- This library was designed to implement CLI styles for users

```
make_menu("1. Title", "Short description", "short", True)
make_menu("2. Title", "Long description", "long", newline=True)
make_menu("3. Title")
```

"""

import os

def get_terminal_size():
    size = os.get_terminal_size()
    return size.lines, size.columns

def make_menu(title, text = "", style = "default", new_line = True, separator_style = "="):
    """
    The function accepts 4 parameters: `title`, `text`, `style` and `newline`.
    The parameters `text`, `style` e `newline` are not mandatory.
    """
    rows, columns = get_terminal_size()
    
    if new_line == True:
        print()
    if style == "short":
        # print("1. Short Style Selected")
        print(f'{separator_style}' * columns)
        print(f"{title}")
        print(f"{text}")
        print(f'{separator_style}' * columns)
    elif style == "long":
        # print("2. Long Style Selected")
        print("=" * columns)
        print(f"{title}")
        print("=" * columns)
        print(f"{text}")
        print("=" * columns)
    else:
        # print("3. Default Style Selected")
        print(f'{separator_style}' * columns)
        print(f"{title}")
        print(f'{separator_style}' * columns)

def separator(style = "=", new_line = False):
    rows, columns = get_terminal_size()
    if new_line == True:
        print()
    print(f'{style}' * columns)