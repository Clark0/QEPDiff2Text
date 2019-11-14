# QEPDiff2Text

QEPDiff2Text generates natural language description of two QEPs and differences between them. In its core, QEPDiff2Text generates the QEP trees of the two queries using a PostgreSQL server and uses APTED algorithm\[1\]\[2\] to find the tree edit distance and a homeomorphism between the two QEP trees. The program also includes a Graphical User Interface that allows users to input and change a SQL, commit its changes overtime and generate description of difference of two versions of the query.

## Setup

### Prerequisites

A PostgreSQL database server should be accessible\
This project requires Python3. To verify the correct Python version, run

```
python -V
```

(optional) It will be great if you have a virtual environment

```
python -m venv ./venv
source ./venv/bin/activate
```

### Installation
1. clone the project and enter the project directory

```
git clone https://github.com/Clark0/QEPDiff2Text.git
cd QEPDiff2Text
```

2. install Python packages

```
pip install -r requirements.txt
```

### Run

Under the project root directory, run

```
python main.py
```

to start the main program.

## References

1.	M. Pawlik and N. Augsten, “Efficient Computation of the Tree Edit Distance,” ACM Transactions on Database Systems, vol. 40, no. 1. pp. 1–40, 2015.
2.	M. Pawlik and N. Augsten, “Tree edit distance: Robust and memory-efficient,” Information Systems, vol. 56. pp. 157–173, 2016.