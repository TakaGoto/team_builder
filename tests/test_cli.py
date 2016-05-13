from src.cli       import Cli
from tests.io_mock import InputMock, OutputMock

import unittest

class ConsoleUiTests(unittest.TestCase):
  def test_promptsForNumberOfTeams(self):
    expectedPrompt = "Enter number of teams: "
    cli = Cli(InputMock(), OutputMock())

    cli.ask_team_number()

    output = cli.ui_output.output
    self.assertEqual(expectedPrompt, output)

  def test_ReadsUserInputAfterBeingPromptedForNumberOfTeams(self):
    cli = Cli(InputMock(), OutputMock())

    result = cli.ask_team_number()

    self.assertIsNotNone(result)

if __name__ == '__main__':
  unittest.main()

