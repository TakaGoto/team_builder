class Cli:

  def __init__(self, ui_input, ui_output):
    self.ui_input = ui_input
    self.ui_output = ui_output

  def ask_team_number(self):
    self.ui_output.write("Enter number of teams: ")
    return self.ui_input.readline()
