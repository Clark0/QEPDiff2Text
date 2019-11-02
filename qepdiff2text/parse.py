import json
from node import Node
from constants import NodeAttrs


def parse_json(json_str):
    attrs = json.loads(json_str)[0][NodeAttrs.PLAN]
    root = Node(attrs)
    return root


if __name__ == '__main__':
    with open('sample_json/query1.json') as f:
        json_str = f.read()
    root = parse_json(json_str)
    print(root.attributes)
