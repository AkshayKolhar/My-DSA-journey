class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def count(x):
            total = 0

            # Generate every non-empty subset
            for mask in range(1, 1 << n):

                lcm_value = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1

                        # Calculate LCM
                        lcm_value = lcm(
                            lcm_value,
                            coins[i]
                        )

                        if lcm_value > x:
                            break

                if bits % 2 == 1:
                    total += x // lcm_value
                else:
                    total -= x // lcm_value

            return total

        left = 1
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left