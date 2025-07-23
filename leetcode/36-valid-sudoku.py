from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]

        sub = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            row = board[i]
            row_seen = row_sets[i]

            for j in range(len(row)):
                el = row[j]

                if el == '.':
                    continue

                col_seen = col_sets[j]
                s_seen = sub[i // 3][j // 3]

                if el in row_seen or el in col_seen or el in s_seen:
                    print(el, row_seen, col_seen, s_seen)
                    return False

                row_seen.add(el)
                col_seen.add(el)
                s_seen.add(el)

        return True

