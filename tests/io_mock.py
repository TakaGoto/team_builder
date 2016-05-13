class InputMock:
  def __init__(self):
    pass

  def readline(self):
    return "5"

class OutputMock:
  def __init__(self):
    self.output = ""
    pass

  def write(self, output):
    self.output = output
