# Set context to parent folder
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

# Import library to test
from agriculture import definitive_answer
import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_the_answer_to_the_ultimate_question_of_life_the_universe_and_everything(self):
        assert definitive_answer() == 42


if __name__ == '__main__':
    unittest.main()