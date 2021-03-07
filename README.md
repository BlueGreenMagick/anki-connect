# Headless Anki Connect

This project lets you use Anki-connect with [Headless Anki](https://github.com/blueGreenMagick/headless-anki).
Obviously, any actions related to gui won't work. This program will probably crash if you do that.

See [Original anki-connect repo](https://github.com/FooSoft/anki-connect) for documentation on requests and actions.

## How to use

```python
from plugin import AnkiConnect

ac = AnkiConnect()
ac.listen()
```

It requires `headlessanki` package to be in the PYTHONPATH. You can download the package from [github repo](https://github.com/blueGreenMagick/headless-anki) and put it in this directory.

There is currently no way to stop anki-connect from listening. Kill the process manually (Ctrl + C).
