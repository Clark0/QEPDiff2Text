import unittest
import json
from qepdiff2text.node import Node


class TestNodeToText(unittest.TestCase):
    def test_general(self):
        attrs = {
            "Node Type": "Hash Join",
            "Parent Relationship": "Outer",
            "Parallel Aware": False,
            "Join Type": "Inner",
            "Startup Cost": 112769.09,
            "Total Cost": 158319.28,
            "Plan Rows": 202,
            "Plan Width": 16,
            "Actual Startup Time": 1027.052,
            "Actual Total Time": 1443.842,
            "Actual Rows": 234990,
            "Actual Loops": 1,
            "Hash Cond": "((i.proceeding_key)::text = (p.pub_key)::text)",
            "Plans": [
                {
                    "Node Type": "Seq Scan",
                    "Parent Relationship": "Outer",
                    "Parallel Aware": False,
                    "Relation Name": "inproceedings",
                    "Alias": "i",
                    "Startup Cost": 0.00,
                    "Total Cost": 37892.67,
                    "Plan Rows": 2041467,
                    "Plan Width": 16,
                    "Actual Startup Time": 0.041,
                    "Actual Total Time": 185.190,
                    "Actual Rows": 2041467,
                    "Actual Loops": 1
                },
                {
                    "Node Type": "Hash",
                    "Parent Relationship": "Inner",
                    "Parallel Aware": False,
                    "Startup Cost": 112764.24,
                    "Total Cost": 112764.24,
                    "Plan Rows": 388,
                    "Plan Width": 23,
                    "Actual Startup Time": 1026.985,
                    "Actual Total Time": 1026.985,
                    "Actual Rows": 3788,
                    "Actual Loops": 1,
                    "Hash Buckets": 4096,
                    "Original Hash Buckets": 1024,
                    "Hash Batches": 1,
                    "Original Hash Batches": 1,
                    "Peak Memory Usage": 213,
                    "Plans": [
                        {
                            "Node Type": "Seq Scan",
                            "Parent Relationship": "Outer",
                            "Parallel Aware": False,
                            "Relation Name": "publication",
                            "Alias": "p",
                            "Startup Cost": 0.00,
                            "Total Cost": 112764.24,
                            "Plan Rows": 388,
                            "Plan Width": 23,
                            "Actual Startup Time": 3.994,
                            "Actual Total Time": 1025.785,
                            "Actual Rows": 3788,
                            "Actual Loops": 1,
                            "Filter": "(title ~~ '%July%'::text)",
                            "Rows Removed by Filter": 3888711
                        }
                    ]
                }
            ]
        }
        node = Node(attrs)
        print(node.to_text())
        self.assertTrue(True)

    def test_unique(self):
        with open('tests/test.json') as f:
            attr = json.loads(f.read())[0]['Plan']

        node = Node(attr)
        node.to_text()


if __name__ == '__main__':
    unittest.main()
