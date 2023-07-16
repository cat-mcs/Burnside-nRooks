
# ♖ Burnsides Lemma : 𝑛 Rooks ♖

Consider an 𝑛 × 𝑛 chessboard. A rook is a piece that may move any number of squares horizontally or vertically on this board. Hence, a rook threatens another if they are placed on the same row or column. Suppose we are dealing with a rook free-for-all. 

##### can 𝑛 rooks be placed on the board such that none are threatened?

Certainly, placing them along the 𝑛 squares of the main diagonal yields a valid arrangement. Furthermore, every valid arrangement is such that each rook is assigned a unique row and unique column. Hence, to find an arrangement we can iterate through the columns and place a rook in a non-occupied row. There are 𝑛 choices of row in first column , 𝑛 − 1 choices of row in the second column and so on. Therefore, there are 𝑛! valid arrangements in total. These correspond bijectively to the 𝑛! permutations of the symmetric group.

##### how many rook arrangements exist up to symmetry of the chessboard?

This program is able to compute an answer for reasonable values of 𝑛. The formula used is based on that presented by Martin Aigner in 'A Course in Enumeration' - Chapter 6 (https://epdf.tips/a-course-in-enumeration.html) which is an application of Burnside's Lemma. This is the integer sequence A000903 (https://oeis.org/A000903).

## how to use:
Enter a board dimension. Rook configuration count from 𝑛 = 5 to 𝑛 = input is printed.