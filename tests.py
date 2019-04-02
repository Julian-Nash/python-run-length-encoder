import unittest
from run_length_encoder import RunLengthEncoder


class TestRunLengthEncoders(unittest.TestCase):

    # Tests for encoder_a
    def test_encoder_a(self):
        encoder = RunLengthEncoder()
        text = "aaabbcdddd"
        expected_result = "3a2bc4d"
        self.assertEqual(encoder.encode_a(text), expected_result)

    def test_encoder_a2(self):
        encoder = RunLengthEncoder()
        text = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnoooppp"
        expected_result = "3a3b3c3d3e3f3g3h3i3j3k3l3m3n3o3p"
        self.assertEqual(encoder.encode_a(text), expected_result)

    def test_encoder_a3(self):
        encoder = RunLengthEncoder()
        text = "abcabcabcabcabcabc"
        expected_result = "abcabcabcabcabcabc"
        self.assertEqual(encoder.encode_a(text), expected_result)

    def test_encoder_a4(self):
        encoder = RunLengthEncoder()
        text = "1223334444"
        expected_result = "1223344"
        self.assertEqual(encoder.encode_a(text), expected_result)

    def test_encoder_a5(self):
        encoder = RunLengthEncoder()
        text = "abc123xyz"
        expected_result = "abc123xyz"
        self.assertEqual(encoder.encode_a(text), expected_result)

    # Tests for encoder_b
    def test_encoder_b(self):
        encoder = RunLengthEncoder()
        text = "aaabbcdddd"
        expected_result = "3a2b1c4d"
        self.assertEqual(encoder.encode_b(text), expected_result)

    def test_encoder_b2(self):
        encoder = RunLengthEncoder()
        text = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnoooppp"
        expected_result = "3a3b3c3d3e3f3g3h3i3j3k3l3m3n3o3p"
        self.assertEqual(encoder.encode_b(text), expected_result)

    def test_encoder_b3(self):
        encoder = RunLengthEncoder()
        text = "abcabcabcabcabcabc"
        expected_result = "1a1b1c1a1b1c1a1b1c1a1b1c1a1b1c1a1b1c"
        self.assertEqual(encoder.encode_b(text), expected_result)

    def test_encoder_b4(self):
        encoder = RunLengthEncoder()
        text = "1223334444"
        expected_result = "11223344"
        self.assertEqual(encoder.encode_b(text), expected_result)

    def test_encoder_b5(self):
        encoder = RunLengthEncoder()
        text = "abc123xyz"
        expected_result = "1a1b1c1112131x1y1z"
        self.assertEqual(encoder.encode_b(text), expected_result)

    # Tests for encoder_c
    def test_encoder_c(self):
        encoder = RunLengthEncoder()
        text = "aaabbcdddd"
        expected_result = "3a2b1c4d"
        self.assertEqual(encoder.encode_c(text), expected_result)

    def test_encoder_c2(self):
        encoder = RunLengthEncoder()
        text = "aaabbbcccdddeeefffggghhhiiijjjkkklllmmmnnnoooppp"
        expected_result = "3a3b3c3d3e3f3g3h3i3j3k3l3m3n3o3p"
        self.assertEqual(encoder.encode_c(text), expected_result)

    def test_encoder_c3(self):
        encoder = RunLengthEncoder()
        text = "abcabcabcabcabcabc"
        expected_result = "1a1b1c1a1b1c1a1b1c1a1b1c1a1b1c1a1b1c"
        self.assertEqual(encoder.encode_c(text), expected_result)

    def test_encoder_c4(self):
        encoder = RunLengthEncoder()
        text = "1223334444"
        expected_result = "11223344"
        self.assertEqual(encoder.encode_c(text), expected_result)

    def test_encoder_c5(self):
        encoder = RunLengthEncoder()
        text = "abc123xyz"
        expected_result = "1a1b1c1112131x1y1z"
        self.assertEqual(encoder.encode_c(text), expected_result)


if __name__ == "__main__":
    unittest.main()
