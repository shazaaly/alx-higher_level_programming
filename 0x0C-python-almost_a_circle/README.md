0x0C. Python - Almost a circle
# Almost a Circle

This repository contains the implementation of a series of classes in Python that are part of the "Almost a Circle" project. The project focuses on various aspects of Python programming, including object-oriented programming, unit testing, file handling, serialization, and more.

## Getting Started

To use these classes, follow the instructions below:

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/alx-higher_level_programming.git
```

2. Navigate to the project directory:

```
cd alx-higher_level_programming/0x0C-python-almost_a_circle/
```

3. Use the classes in your own Python scripts by importing the necessary modules. For example, to use the `Rectangle` class, you can import it as follows:

```python
from models.rectangle import Rectangle
```

## Contents

The project consists of the following files and directories:

- `models`: Directory containing the implementation of the classes.
- `tests`: Directory containing unit tests for the classes.
- `README.md`: Readme file explaining the project and providing instructions.
- `1-main.py`, `2-main.py`, ..., `18-main.py`: Example scripts demonstrating the usage of the classes and methods.
- `base.py`: Implementation of the `Base` class.
- `rectangle.py`: Implementation of the `Rectangle` class.
- `square.py`: Implementation of the `Square` class.

## Classes

The project includes the following classes:

### Base Class

- `Base`: Base class for all other classes in the project. Manages the `id` attribute and provides methods for JSON serialization and deserialization.

### Rectangle Class

- `Rectangle`: Represents a rectangle. Inherits from the `Base` class. Includes methods for calculating the area, displaying the rectangle, updating attributes, and more.

### Square Class

- `Square`: Represents a square. Inherits from the `Rectangle` class. Includes methods for updating attributes specific to squares.

## Testing

The project includes unit tests for each class. To run the tests, use the following command:

```
python3 -m unittest discover tests
```

Make sure you are in the project directory when running the command.
Copyright © 2023 ALX, All rights reserved.
