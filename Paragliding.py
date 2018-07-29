def main():
    t = int(raw_input())

    for t in range(t):

        # Read n, k
        n, k = [int(s) for s in raw_input().split(" ")]

        # Tower & Balloon position  [x,y]
        tower = [[0] * 2 for _ in range(n)]
        balloon = [[0] * 2 for _ in range(k)]

        # Read para
        tower[0][0], tower[1][0], a1, b1, c1, m1 = [int(s) for s in raw_input().split(" ")]
        tower[0][1], tower[1][1], a2, b2, c2, m2 = [int(s) for s in raw_input().split(" ")]
        balloon[0][0], balloon[1][0], a3, b3, c3, m3 = [int(s) for s in raw_input().split(" ")]
        balloon[0][1], balloon[1][1], a4, b4, c4, m4 = [int(s) for s in raw_input().split(" ")]

        # Calculate tower and balloon
        for i in range(2, n):
            tower[i][0] = (a1 * tower[i - 1][0] + b1 * tower[i - 2][0] + c1) % m1 + 1
            tower[i][1] = (a2 * tower[i - 1][1] + b2 * tower[i - 2][1] + c2) % m2 + 1

        for i in range(2, k):
            balloon[i][0] = (a3 * balloon[i - 1][0] + b3 * balloon[i - 2][0] + c3) % m3 + 1
            balloon[i][1] = (a4 * balloon[i - 1][1] + b4 * balloon[i - 2][1] + c4) % m4 + 1

        # Sort tower with x-axis
        tower = sorted(tower, key=lambda x: x[0])

        # Generate relevant tower, add, remove
        relevant_tower = []
        for i in range(len(tower)):
            # empty relevant tower
            if not relevant_tower:
                relevant_tower.append(tower[i])
                continue

            # last relevant tower
            x, y = relevant_tower[-1]

            # previous tower cover ith tower
            if y - tower[i][1] >= tower[i][0] - x:
                continue

            # ith tower cover previous tower
            while tower[i][1] - y >= tower[i][0] - x:
                # remove previous tower
                relevant_tower.pop()
                # empty
                if not relevant_tower: break
                # next previous
                x, y = relevant_tower[-1]

            # add ith tower
            relevant_tower.append(tower[i])

        balloon_cover = [0 for _ in range(k)]
        # print(relevant_tower)
        # print(balloon)

        for i in range(len(balloon)):
            # x-axis < most left relevant tower
            if balloon[i][0] < relevant_tower[0][0]:
                if relevant_tower[0][1] - balloon[i][1] >= relevant_tower[0][0] - balloon[i][0]:
                    balloon_cover[i] = 1
                continue

            # x-axis > most right relevant tower
            if balloon[i][0] >= relevant_tower[-1][0]:
                if relevant_tower[-1][1] - balloon[i][1] >= balloon[i][0] - relevant_tower[-1][0]:
                    balloon_cover[i] = 1
                continue

            # x-axis between relevant tower, dichotomy
            left = 0
            right = len(relevant_tower) - 1
            while left + 1 < right:
                mid = (left + right) / 2
                if relevant_tower[mid][0] <= balloon[i][0]:
                    left = mid
                else:
                    right = mid

            # closest left relevant tower cover ith balloon
            if relevant_tower[left][1] - balloon[i][1] >= balloon[i][0] - relevant_tower[left][0]:
                balloon_cover[i] = 1
                continue

            # closest right relevant tower cover ith balloon
            if relevant_tower[right][1] - balloon[i][1] >= relevant_tower[right][0] - balloon[i][0]:
                balloon_cover[i] = 1
                continue

        print("Case #" + str(t + 1) + ": " + str(sum(balloon_cover)))


if __name__ == '__main__':
    main()
