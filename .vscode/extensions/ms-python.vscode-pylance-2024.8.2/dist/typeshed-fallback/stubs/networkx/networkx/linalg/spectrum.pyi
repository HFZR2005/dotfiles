from _typeshed import Incomplete

from networkx.utils.backends import _dispatch

@_dispatch
def laplacian_spectrum(G, weight: str = "weight"): ...
@_dispatch
def normalized_laplacian_spectrum(G, weight: str = "weight"): ...
@_dispatch
def adjacency_spectrum(G, weight: str = "weight"): ...
@_dispatch
def modularity_spectrum(G): ...
@_dispatch
def bethe_hessian_spectrum(G, r: Incomplete | None = None): ...
