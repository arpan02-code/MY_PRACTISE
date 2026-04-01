class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        # 1. Combine into robot objects: (pos, health, direction, original_index)
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        
        # 2. Sort by physical position
        robots.sort()
        
        stack = [] # Stores robots moving Right ('R')
        
        for i in range(len(robots)):
            # If moving Right, push to stack and wait
            if robots[i][2] == 'R':
                stack.append(robots[i])
            else:
                # If moving Left, check for collisions with 'R' robots in stack
                while stack and robots[i][1] > 0:
                    top_r = stack[-1]
                    
                    if robots[i][1] > top_r[1]:
                        # Left robot wins, R robot destroyed
                        stack.pop()
                        robots[i][1] -= 1
                        top_r[1] = 0 # Mark as destroyed
                    elif robots[i][1] < top_r[1]:
                        # Right robot wins, L robot destroyed
                        top_r[1] -= 1
                        robots[i][1] = 0 # Mark as destroyed
                    else:
                        # Both destroyed
                        stack.pop()
                        robots[i][1] = 0
                        top_r[1] = 0
        
        # 3. Collect survivors and sort by original index
        survivors = [r for r in robots if r[1] > 0]
        survivors.sort(key=lambda x: x[3])
        
        return [r[1] for r in survivors]
