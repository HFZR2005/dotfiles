from networkx.utils.backends import _dispatch

def tree_data(G, root, ident: str = "id", children: str = "children"): ...
@_dispatch
def tree_graph(data, ident: str = "id", children: str = "children"): ...
