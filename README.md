# Knight's Tour problem using Warnsdorff's rule

## Constraints

For an N x N matrix, a successful tour is only possible if:

* N >= 6 and N is even.
* If N = 5, only the start positions of diagonal element are guranteed to produce a successfull tour.

## Valid Moves

![validMoves](https://raw.githubusercontent.com/matt493/knights_tour/master/Moves.png)

## Algorithm

1. Set H to be a random initial position on the board
2. Mark the board at H with the move number “1”
3. Do following for each move number from 2 to the number of squares on the board:
   1. let S be the set of positions accessible from H.
   2. Set H to be the position in S with minimum accessibility
   3. Mark the board at H with the current move number
4. Print the marked board, each square will be marked with the move number on which it is visited.