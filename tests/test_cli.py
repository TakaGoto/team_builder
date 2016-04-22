from src.cli import Cli

import unittest

class ConsoleUiTests(unittest.TestCase):
  def test_promptsForNumberOfTeams(self):
    expectedPrompt = "Enter number of teams: "
    cli = Cli(IoMock())

    cli.ask_team_number()

    output = cli.io.output
    self.assertEqual(expectedPrompt, output)

class IoMock:
  def __init__(self):
    self.output = ""

  def write(self, output):
    self.output = output

  def readline(self):
    return "5"

if __name__ == '__main__':
  unittest.main()

