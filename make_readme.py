import qbit

README = "# pyqbit" + "\n"

README += '\n## Circuit'+ "\n" + qbit.Circuit.__doc__
README += '\n## Zero'+ "\n" + qbit.Zero.__doc__
README += '\n## One'+ "\n" + qbit.One.__doc__
README += '\n## Plus'+ "\n" + qbit.Plus.__doc__
README += '\n## Minus'+ "\n" + qbit.Minus.__doc__
README += '\n## Measure'+ "\n" + qbit.Measure.__doc__
README += '\n## Combine'+ "\n" + qbit.Combine.__doc__
README += '\n## Identity'+ "\n" + qbit.Identity.__doc__
README += '\n## H'+ "\n" + qbit.H.__doc__
README += '\n## PauliX'+ "\n" + qbit.PauliX.__doc__
README += '\n## PauliY'+ "\n" + qbit.PauliY.__doc__
README += '\n## PauliZ'+ "\n" + qbit.PauliZ.__doc__
README += '\n## Phase'+ "\n" +  qbit.Phase.__doc__
README += '\n## R'+ "\n" + qbit.R.__doc__
README += '\n## CNOT'+ "\n" + qbit.CNOT.__doc__
README += '\n## CPauliZ'+ "\n" + qbit.CPauliZ.__doc__
README += '\n## SWAP'+ "\n" + qbit.SWAP.__doc__


with open('README.md', 'wt') as readme_file:
    readme_file.write(README)