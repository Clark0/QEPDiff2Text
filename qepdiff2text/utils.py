from typing import Iterator, TypeVar

from .Node import Node

def post_order_tree_traversal(node: Node) -> Iterator[Node]:
    """
    Returns a iterator that traverses the tree in post order
    :param node:
    :return:
    """
    for child in node.children:
        for grand_child in post_order_tree_traversal(child):
            yield grand_child
    yield node

T = TypeVar('T')

def infinite_none_suffix(generator: Iterator[T]) -> Iterator[T]:
    for i in generator:
        yield i
    while True:
        yield None
