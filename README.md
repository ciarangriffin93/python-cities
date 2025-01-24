
## Features
- Reads city connections from a text file.
- Checks if two specified cities are connected.
- Handles invalid file paths or missing data gracefully.
- Includes unit tests for verification.

---

## Requirements
- Python 3.6 or later.

---

## File Format
The input file should contain pairs of city names separated by commas, with one pair per line. For example:

```
Bengaluru, Hyderabad
Chennai, Bengaluru
Hyderabad, Nagpur
Hyderabad, Vijayawada
Bengaluru, Kochi
```

---

## Installation and Setup
1. Save the program code in a file named `connected_cities.py`.
2. Ensure Python is installed on your system.
3. Create a text file (e.g., `cities.txt`) containing city pairs as per the specified format.

---

## Usage
Run the program from the command line:

```bash
python connected_cities.py <file_path> <city1> <city2>
```

### Example
Given a `cities.txt` file with the following content:

```
Bengaluru, Hyderabad
Chennai, Bengaluru
Hyderabad, Nagpur
Hyderabad, Vijayawada
Bengaluru, Kochi
```

Run the command:

```bash
python connected_cities.py cities.txt Bengaluru Nagpur
```

Output:

```
Yes, Bengaluru and Nagpur are connected.
```

If the cities are not connected, the output will be:

```
No, <city1> and <city2> are not connected.
```

---

## Unit Testing
### Running Tests
1. Save the test code in a file named `test_connected_cities.py`.
2. Run the tests using:

```bash
python -m unittest test_connected_cities.py
```

### Test Example
Tests verify:
- Direct connections between cities.
- Indirect connections through intermediate cities.
- Cities that are not connected.
- Non-existent cities.

Expected output after running the tests:

```
...
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

---

