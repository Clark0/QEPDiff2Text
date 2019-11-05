from qepdiff2text.Description import InsertionDescription
from qepdiff2text.Description import DeletionDescription
from qepdiff2text.Description import SameDescription
from qepdiff2text.Description import UpdateDescription

def test_InsertionDescription():
    after_des = "Step 1: Hash join on so and so"
    diff_des = "A node is inserted."

    d = InsertionDescription(after_des=after_des, diff_des=diff_des)

    assert after_des == d.get_after_des()
    assert diff_des == d.get_diff_des()

def test_DeletionDescription():
    before_des = "Step 1: Hash"
    diff_des = "A node is deleted."

    d = DeletionDescription(before_des=before_des, diff_des=diff_des)

    assert before_des == d.get_before_des()
    assert diff_des == d.get_diff_des()

def test_SameDescription():
    before_des = "Step 3: Index Scan on R"
    after_des = "Step 4: Index Scan on R"

    d = SameDescription(before_des=before_des, after_des=after_des)

    assert before_des == d.get_before_des()
    assert after_des == d.get_after_des()

def test_UpdateDescription():
    before_des = "Step 3: Index Scan on R"
    after_des = "Step 3: Seq Scan on R"
    diff_des = "Algorithm changed from Index Scan to Seq Scan"

    d = UpdateDescription(before_des=before_des, after_des=after_des, diff_des=diff_des)

    assert before_des == d.get_before_des()
    assert after_des == d.get_after_des()
    assert diff_des == d.get_diff_des()
