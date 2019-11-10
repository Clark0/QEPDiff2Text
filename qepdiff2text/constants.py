class _const():
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value

    @classmethod
    def all(cls):
        return [value for name, value in cls.__dict__.items()
                if not name.startswith('_')]


class NodeAttrs(_const):
    NODE_TYPE = 'Node Type' #x
    PLAN = 'Plan' #x
    PLANS = 'Plans' #x
    RELATION_NAME = 'Relation Name' #
    SCHEMA = 'Schema' #x
    ALIAS = 'Alias' #x
    GROUP_KEY = 'Group Key' #
    SORT_KEY = 'Sort Key' #
    JOIN_TYPE = 'Join Type' #
    INDEX_NAME = 'Index Name' #
    HASH_COND = 'Hash Cond' #
    FILTER = 'Filter' #
    INDEX_COND = 'Index Cond' #
    MERGE_COND = 'Merge Cond' #
    RECHECK_COND = 'Recheck Cond' #
    JOIN_FILTER = 'Join Filter' #
    ACTUAL_ROWS = 'Actual Rows' #x
    ACTUAL_TOTAL_TIME = 'Actual Total Time' #x
    SUBPLAN_NAME = 'Subplan Name' #x
    RETURNS = 'returns' #x


class Algos(_const):
    PROJECT_SET = "Project_Set"
    APPEND = "Append"
    MERGE_APPEND = "Merge Append"
    RECURSIVE_UNION = "Recursive Union"
    BITMAP_AND = "Bitmap_And"
    BITMAP_OR = "Bitmap_Or"
    NEST_LOOP = "Nested Loop"
    MERGE_JOIN = "Merge Join"
    HASH_JOIN = "Hash Join"
    SEQ_SCAN = "Seq Scan"
    SAMPLE_SCAN = "Sample Scan"
    GATHER = "Gather"
    GATHER_MERGE = "Gather Merge"
    INDEX_SCAN = "Index Scan"
    INDEX_ONLY_SCAN = "Index Only Scan"
    BITMAP_INDEX_SCAN = "Bitmap Index Scan"
    BITMAP_HEAP_SCAN = "Bitmap Heap Scan"
    TID_SCAN = "Tid Scan"
    SUBQUERY_SCAN = "Subquery Scan"
    FUNCTION_SCAN = "Function Scan"
    TABLE_FUNC_SCAN = "Table Function Scan"
    VALUES_SCAN = "Values Scan"
    CTE_SCAN = "CTE Scan"
    NAMED_TUPLESTORE_SCAN = "Named Tuplestore Scan"
    WORK_TABLE_SCAN = "Work_Table Scan"

    # Operation - "Select", "Insert", "Update", "Delete"
    FOREIGN_SCAN = "Foreign Scan"

    CUSTOM_SCAN = "Custom Scan"
    MATERIAL = "Materialize"
    SORT = "Sort"
    GROUP = "Group"

    # Strategy - "Plain", "Sorted", "Hashed", "Mixed"
    AGG = "Aggregate"

    WINDOW_AGG = "Window_Agg"
    UNIQUE = "Unique"
    LOCK_ROWS = "Lock_Rows"
    LIMIT = "Limit"
    HASH = "Hash"

class Operations(_const):
    PROJECT_SET = "PROJECT_SET"
    APPEND = "APPEND"
    MERGE_APPEND = "MERGE_APPEND"
    RECURSIVE_UNION = "RECURSIVE_UNION"
    BITMAP_AND = "BITMAP_AND"
    BITMAP_OR = "BITMAP_OR"
    SCAN = "SCAN"
    JOIN = "JOIN"
    MATERIAL = "MATERIAL"
    SORT = "SORT"
    GROUP = "GROUP"
    AGG = "AGG"
    WINDOW_AGG = "WINDOW_AGG"
    UNIQUE = "UNIQUE"
    LOCK_ROWS = "LOCK_ROWS"
    LIMIT = "LIMIT"
    HASH = "HASH"

####################################
# Operation: Algorithms mapping
####################################
OP_ALGS = {
    Operations.PROJECT_SET: [Algos.PROJECT_SET],
    Operations.APPEND: [Algos.APPEND],
    Operations.MERGE_APPEND: [Algos.MERGE_APPEND],
    Operations.RECURSIVE_UNION: [Algos.RECURSIVE_UNION],
    Operations.BITMAP_AND: [Algos.BITMAP_AND],
    Operations.BITMAP_OR: [Algos.BITMAP_OR],
    Operations.SCAN: [
        Algos.SEQ_SCAN,
        Algos.SAMPLE_SCAN,
        Algos.INDEX_SCAN,
        Algos.INDEX_ONLY_SCAN,
        Algos.BITMAP_INDEX_SCAN,
        Algos.BITMAP_HEAP_SCAN,
        Algos.TID_SCAN,
        Algos.SUBQUERY_SCAN,
        Algos.FUNCTION_SCAN,
        Algos.TABLE_FUNC_SCAN,
        Algos.VALUES_SCAN,
        Algos.CTE_SCAN,
        Algos.NAMED_TUPLESTORE_SCAN,
        Algos.WORK_TABLE_SCAN,
        Algos.FOREIGN_SCAN,
        Algos.CUSTOM_SCAN
    ],
    Operations.JOIN: [
        Algos.NEST_LOOP,
        Algos.MERGE_JOIN,
        Algos.HASH_JOIN
    ],
    Operations.MATERIAL: [Algos.MATERIAL],
    Operations.SORT: [Algos.SORT],
    Operations.GROUP: [Algos.GROUP],
    Operations.AGG: [Algos.AGG],
    Operations.WINDOW_AGG: [Algos.WINDOW_AGG],
    Operations.UNIQUE: [Algos.UNIQUE],
    Operations.LOCK_ROWS: [Algos.LOCK_ROWS],
    Operations.LIMIT: [Algos.LIMIT],
    Operations.HASH: [Algos.HASH]
}

