class Solution:
    def nodesBetweenCriticalPoints(self, head):
        positions = []
        prev = head
        curr = head.next
        position = 1

        while curr and curr.next:
            next_node = curr.next

            # Check if current node is a critical point
            if (curr.val > prev.val and curr.val > next_node.val) or \
               (curr.val < prev.val and curr.val < next_node.val):
                positions.append(position)

            prev = curr
            curr = curr.next
            position += 1

        # Less than 2 critical points
        if len(positions) < 2:
            return [-1, -1]

        # Minimum distance between consecutive critical points
        min_distance = min(
            positions[i] - positions[i - 1]
            for i in range(1, len(positions))
        )

        # Maximum distance = last - first
        max_distance = positions[-1] - positions[0]

        return [min_distance, max_distance]