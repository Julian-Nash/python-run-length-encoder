## Python Run-Length Encoder

A RunLengthEncoder class with 3 available methods, all of which take an input string and return a compressed output string.

Examples:

- `encode_a`

```py3
from run_length_encoder import RunLengthEncoder

encoder = RunLengthEncoder()

result = encoder.encode_a("abc123xyzaaabbbcccd")
print(result)
```

`encode_a` Returns a compressed string from an input string.

Note: This function will not return the character count in the return string if only a single instance of the character is found.

Result:

```sh
abc123xyz3a3b3cd
```

- `encode_b`

```py3
from run_length_encoder import RunLengthEncoder

encoder = RunLengthEncoder()

result = encoder.encode_b("abc123xyzaaabbbcccd")
print(result)
```

`encode_b` Returns a run-length encoded string from an input string, with a count for each character, followed by the character itself.


Result:

```sh
1a1b1c1112131x1y1z3a3b3c1d
```

- `encode_c`

```py3
from run_length_encoder import RunLengthEncoder

encoder = RunLengthEncoder()

result = encoder.encode_c("abc123xyzaaabbbcccd")
print(result)
```

`encode_c` uses a list comprehension to build the return string.

Result:

```sh
1a1b1c1112131x1y1z3a3b3c1d
```

### Usage

Clone this repo & run:

```sh
python example.py
```

### Tests

To run the small suite of unit tests:

```sh
python test.py
```