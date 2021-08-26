We can put one number at the end and another at the start and the array will be sorted, we can do this with an index for 0 at the start and index for 2 at the end.

We check if x_index is above 2, then reduce by 1.
If above a 0 we change it with x and move them both forward.
and if the index is above 1 we move index forward.

Time complexity:

O(n)

Space:

O(1)