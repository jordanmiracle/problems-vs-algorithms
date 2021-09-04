Oh my gosh this was a bit more involved.

Getting there though.

So, first we init the root node and a handler.
We split the path into sub or child paths with "/". Then, we check whether the sub path is in the dict of RouteTrieNode. If it is then we go to the child and next path.

If not the sub will be added to dict, then a fresh RouteTrieNode will be built. as then next node of the child.

Build an insert function in the RouteTrieNode class.

Router class:

Build a new Route Trie for holding routes. Add handler path.

**Time Complexity**
O(n), because of the for loop, both functions have O(n).

**Space**:

O(m*n), because we depend on the # of words, and the length of them.