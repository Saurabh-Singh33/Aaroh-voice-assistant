import unittest

from assistant.listen import get_microphone_device_index
from assistant.wake_word import detect_wake_word, extract_command_from_wake_word


class WakeWordTests(unittest.TestCase):
    def test_detects_wake_word_with_punctuation(self):
        self.assertTrue(detect_wake_word("Hey, Aroha!"))

    def test_extracts_command_after_punctuated_wake_word(self):
        command = extract_command_from_wake_word("Hey, Aroha, what time is it?")
        self.assertEqual(command, "what time is it")

    def test_microphone_selection_returns_a_valid_index(self):
        index = get_microphone_device_index()
        self.assertIsInstance(index, int)
        self.assertGreaterEqual(index, 0)


if __name__ == "__main__":
    unittest.main()
