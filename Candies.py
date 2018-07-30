from bintrees import AVLTree

def main():
    t = int(raw_input())

    for t in range(t):
        N, O, D = raw_input().split(" ")
        X1, X2, A, B, C, M, L = raw_input().split(" ")
        N, O, D = int(N), int(O), int(D)
        X = [0 for _ in range(N)]
        X[0], X[1], A, B, C, M, L = int(X1), int(X2), int(A), int(B), int(C), int(M), int(L)

        # calculate S
        S = []
        for i in range(N):
            if i > 1:
                X[i] = (X[i - 1] * A + X[i - 2] * B + C) % M
            S.append(X[i] + L)
        # print(S)
        odd = [0 for _ in range(N)]
        sum = [0 for _ in range(N)]
        max_reward = -999999999999999999
        flag = False

        if D<0:
            print("Case #" + str(t + 1) + ": IMPOSSIBLE")
            continue


        for i in range(N):
            if i == 0:
                if S[i] % 2 == 1:
                    odd[i] = 1
                sum[i] = S[i]
            else:
                sum[i] = sum[i - 1] + S[i]
                if S[i] % 2 == 1:
                    odd[i] = odd[i - 1] + 1
                else:
                    odd[i] = odd[i - 1]

        for i in range(N):
            now_sum = 0
            now_odd = 0
            if i != 0:
                now_sum = sum[i - 1]
                now_odd = odd[i - 1]
            left = i
            right = N
            while left + 1 < right:
                mid = (left + right) / 2
                if sum[mid] - now_sum > D or odd[mid] - now_odd > O:
                    right = mid
                else:
                    left = mid
            if sum[left] - now_sum <= D and odd[left] - now_odd <= O:
                if sum[left] - now_sum > max_reward:
                    max_reward = sum[left] - now_sum
                    flag = True

        if not flag:
            print("Case #" + str(t + 1) + ": IMPOSSIBLE")
        else:
            print("Case #" + str(t + 1) + ": " + str(max_reward))


if __name__ == '__main__':
    main()
