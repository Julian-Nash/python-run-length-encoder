from run_length_encoder import RunLengthEncoder

encoder = RunLengthEncoder()

string_to_compress = "abc123xyzaaabbbcccd"
print(f"Compressing string: {string_to_compress}")

# result = encoder.encode_a(string_to_compress)
# print(result)

result = encoder.encode_b(string_to_compress)
print(result)

# result = encoder.encode_c(string_to_compress)
# print(result)
