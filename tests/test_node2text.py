import json
from qepdiff2text.Node import Node


def test_unique():
    with open('tests/test.json') as f:
        attr = json.loads(f.read())[0]['Plan']
    node = Node(attr)
    print_text(node)


def print_text(node, indent=0):
    print(' ' * indent, end='')
    print(node.to_text())
    indent += 2
    for child in node.children:
        print_text(child, indent)


if __name__ == '__main__':
    test_unique()
