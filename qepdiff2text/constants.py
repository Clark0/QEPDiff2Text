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
    NODE_TYPE = 'Node Type'
    PLAN = 'Plan'
    PLANS = 'Plans'
    RELATION_NAME = 'Relation Name'
    SCHEMA = 'Schema'
    ALIAS = 'Alias'
    GROUP_KEY = 'Group Key'
    SORT_KEY = 'Sort Key'
    JOIN_TYPE = 'Join Type'
    INDEX_NAME = 'Index Name'
    HASH_COND = 'Hash Cond'
    FILTER = 'Filter'
    INDEX_COND = 'Index Cond'
    MERGE_COND = 'Merge Cond'
    RECHECK_COND = 'Recheck Cond'
    JOIN_FILTER = 'Join Filter'
    ACTUAL_ROWS = 'Actual Rows'
    ACTUAL_TOTAL_TIME = 'Actual Total Time'
    SUBPLAN_NAME = 'Subplan Name'
    RETURNS = 'returns'


class NodeTypes(_const):
    SEQ_SCAN = 'Seq Scan'
    INDEX_SCAN = 'Index Scan'
    INDEX_ONLY_SCAN = 'Index Only Scan'
    BITMAP_HEAP_SCAN = 'Bitmap Heap Scan'
    BITMAP_INDEX_SCAN = 'Bitmap Index Scan'
    CTE_SCAN = 'CTE Scan'
    HASH_JOIN = 'Hash Join'
    MERGE_JOIN = 'Merge Join'
    NESTED_LOOP = 'Nested Loop'
    AGGREGATE = 'Aggregate'
    HASH_AGGREGATE = 'Hash Aggregate'
    SORT = 'Sort'
    LIMIT = 'Limit'
    UNIQUE = "Unique"
