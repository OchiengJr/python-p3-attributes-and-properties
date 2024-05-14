#!/usr/bin/env python3

def pytest_itemcollected(item):
    """
    Modify the node ID of the collected test item to include parent and node documentation or names.

    :param item: The collected test item.
    """
    # Retrieve parent and node objects
    parent = getattr(item, 'parent', None)
    node = getattr(item, 'obj', None)

    # Retrieve the parent description
    if parent:
        parent_desc = parent.__doc__.strip() if parent.__doc__ else parent.__class__.__name__
    else:
        parent_desc = ""

    # Retrieve the node description
    if node:
        node_desc = node.__doc__.strip() if node.__doc__ else node.__name__
    else:
        node_desc = ""

    # Combine descriptions into a single node ID
    if parent_desc or node_desc:
        item._nodeid = ' '.join(filter(None, [parent_desc, node_desc]))

# Example usage with pytest would involve setting this function in a pytest plugin or conftest.py file
