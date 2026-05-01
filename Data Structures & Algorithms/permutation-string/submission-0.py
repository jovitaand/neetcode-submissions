class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)  # length of s1
        r = len(s2)  # length of s2
        
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if l > r:
            return False
        
        # Create frequency maps for s1 and the initial window in s2
        s1_map = {}
        window = {}
        
        # Fill the frequency map for s1
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1
        
        # Fill the frequency map for the first window in s2
        for i in range(l):
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        # Helper function to check if the two frequency maps are equal
        def matches(map1, map2):
            for key in map1:
                if map1.get(key, 0) != map2.get(key, 0):
                    return False
            return True
        
        # Slide the window over s2 one character at a time
        for i in range(r - l):
            if matches(s1_map, window):
                return True
            # Slide the window: remove the leftmost character and add the next character
            left_char = s2[i]
            right_char = s2[i + l]
            
            # Remove the leftmost character from the window map
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            
            # Add the next character in the sequence to the window map
            window[right_char] = window.get(right_char, 0) + 1
        
        # Check the last window
        return matches(s1_map, window)
