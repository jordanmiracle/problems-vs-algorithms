TrieNode: insert operation is O(1) and is simply checking is char/item is not in children. Defaultdict takes care of this.

Suffix: O(n * m), iterate over the children and children of each child.

Trie:

Insert Takes O(n) and iterates over each char in word creating a new trienode.
Then loop completes, set node.is_word to true.

Find:
Takes O(n), and iterates over each char in word. assign child[char/item] as node for next loop.

Time Complexity:

insert and find both take O(n), or 1 iteration per character.

Suffix take O(n * m), need to iterate over children + suffix, with child of each children (same as explained up top).

Space complexity:

insert: O(n), the space used by the algorithm keep it updated while it is being run.

suffix: O(n * m), varying results will occupy the variables, of the stack (n * m).