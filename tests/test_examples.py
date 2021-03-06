import unittest
import subprocess

from compiler import *


class TestExamples(unittest.TestCase):
    def test_examples(self):
        file_to_ast("examples/examples.cu")

    def test_hello_world(self):
        out = run_files(["examples/hello_world.cu"], stdout=subprocess.PIPE)
        self.assertEqual(out.returncode, 0)
        self.assertEqual(out.stdout, b"Hello world\n")

    def test_linked_list(self):
        """Make sure the linked list example compiles and runs."""
        run_files(
            ["examples/linked_list/ll.cu", "examples/linked_list/ll_test.cu"],
            stdout=subprocess.PIPE
        )

    def test_learn(self):
        run_files(["examples/learn.cu"], input=b"6", stdout=subprocess.PIPE)

    def test_fib(self):
        run_files(["examples/fib.cu"], stdout=subprocess.PIPE)

    def test_class(self):
        run_files(["examples/class.cu"])


if __name__ == "__main__":
    unittest.main()
