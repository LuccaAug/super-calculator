import unittest
import subprocess
import platform


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        python_script_path = "main.py"

        if platform.system() == "Windows":
            self.cmd_process = subprocess.Popen(
                ["cmd"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.cmd_process.stdin.write(f"python {python_script_path}\n")

        else:
            self.cmd_process = subprocess.Popen(
                ["bash"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            self.cmd_process.stdin.write(f"python3 {python_script_path}\n")

        self.cmd_process.stdin.flush()

    def run_cmd_commands(self, *commands):
        # Run the commands on terminal
        for cmd in commands:
            self.cmd_process.stdin.write(f'{cmd}\n')

    def get_answer_from_cmd(self):
        # Get the entire output of the terminal
        output, error = self.cmd_process.communicate()

        # Extract the answer of the calculator inside the output depending on the system
        outputs = output.split('\n')
        if platform.system() == "Windows":
            line_with_answer = outputs[-10]
        else:
            line_with_answer = outputs[-9]

        str_value = line_with_answer.split()[-1]
        return float(str_value)

    def test_computation(self):
        self.run_cmd_commands('C', '1', '13')
        output = self.get_answer_from_cmd()

        self.assertEqual(output, 13)

    def test_medicine(self):
        self.run_cmd_commands('M', '1', '1.9', '75')
        output = self.get_answer_from_cmd()

        self.assertEqual(output, 20.78)

    def test_physic(self):
        self.run_cmd_commands('P', '2', '13', '1.3')
        output = self.get_answer_from_cmd()

        self.assertEqual(output, 10)

    def test_trigonometric(self):
        self.run_cmd_commands('T', '4', '45')
        output = self.get_answer_from_cmd()

        self.assertEqual(output, 1.41)

    def test_exit(self):
        self.run_cmd_commands('E')

        # Get the entire output of the terminal
        output, error = self.cmd_process.communicate()

        # Extract the last line based on the system
        if platform.system() == "Windows":
            last_line = output.split('\n')[-3]
        else:
            last_line = output.split('\n')[-2]

        self.assertEqual(last_line, 'Thanks for using the super-calculator! :D')


if __name__ == '__main__':
    unittest.main()
