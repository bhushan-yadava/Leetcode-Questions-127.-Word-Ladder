class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        # Helper function to attempt to transform every word into all possible single-letter variations
        # and to see if we can connect to the opposite side.
        def attempt_extend(current_mappings, opposite_mappings, queue):
            for _ in range(len(queue)):
                # get the next word in the queue
                word = queue.popleft()
                word_step_count = current_mappings[word]
                word_list = list(word)
                # try changing every letter in the word to find a match
                for i in range(len(word_list)):
                    original_char = word_list[i]
                    # replace the current character with all other possible characters
                    for j in range(26):
                        word_list[i] = chr(ord('a') + j)
                        transformed_word = ''.join(word_list)
                        # skip if the word has already been visited by the same front or doesn't exist in wordList
                        if transformed_word in current_mappings or transformed_word not in words:
                            continue
                        # if the transformed word exists on the opposite front, return the total step count
                        if transformed_word in opposite_mappings:
                            return word_step_count + 1 + opposite_mappings[transformed_word]
                        # otherwise, update the mapping and enqueue the transformed word
                        current_mappings[transformed_word] = word_step_count + 1
                        queue.append(transformed_word)
                    # change the word back
                    word_list[i] = original_char
            # return -1 if no connection between the two fronts is found
            return -1
      
        # Convert wordList to a set for O(1) lookups.
        words = set(wordList)
        # Return 0 if the target word is not even in the list.
        if endWord not in words:
            return 0
      
        # Two-ended BFS initialization
        begin_queue = deque([beginWord])
        end_queue = deque([endWord])
        begin_mappings = {beginWord: 0}
        end_mappings = {endWord: 0}
      
        # Execute BFS from both ends
        while begin_queue and end_queue:
            # Always extend the smaller front
            if len(begin_queue) <= len(end_queue):
                result = attempt_extend(begin_mappings, end_mappings, begin_queue)
            else:
                result = attempt_extend(end_mappings, begin_mappings, end_queue)
          
            # If a connection is found, return the total number of steps
            if result != -1:
                return result + 1
      
        # Return 0 if no connection has been found
        return 0
