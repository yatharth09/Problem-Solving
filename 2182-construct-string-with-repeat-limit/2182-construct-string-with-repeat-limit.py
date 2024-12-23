# Gist
# We are using a greedy approach to solve this problem
# We are using a frequency array to store the frequency of each character
# We are using a while loop to iterate through the frequency array
# Once we get out char we add it in the string for repeatLimit times
# Then we search for the char with the highest frequency which is less than the current character ascii value
# We add that character once and then come back to the current element and repeat the process
# We repeat the process till we get out of the while loop i.e the current character becomes -1 

# Time Complexity: O(n)


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26 # Initialize the frequency array (size is 26 because we have 26 letters in the alphabet)
        for char in s: # Update the frequency array
            freq[ord(char) - ord("a")] += 1 # Using the ASCII values of the character to do our work

        result = [] # This is out result subarray in which we will store the final string
        current_char_index = 25  # Start from the largest character
        while current_char_index >= 0: # Iterate through the frequency array
            if freq[current_char_index] == 0: # If the frequency of the current character is 0 we reduce the index and iterate back
                current_char_index -= 1       # As we dont have that character in the string
                continue

            use = min(freq[current_char_index], repeatLimit) # here we Find the number of times we can use the current character
            result.append(chr(current_char_index + ord("a")) * use) # Add the current character to the result "use" number of times
            freq[current_char_index] -= use # Reduce the frequency of the current character as the character has been used

            if freq[current_char_index] > 0:  # Need to add a smaller character as repeatLimit has been hit
                smaller_char_index = current_char_index - 1 # We start from the character right before the current character
                while smaller_char_index >= 0 and freq[smaller_char_index] == 0: # We iterate through the array to find a character with freq > 0
                    smaller_char_index -= 1
                if smaller_char_index < 0: # If there is no smaller character we break out of the loop
                    break
                result.append(chr(smaller_char_index + ord("a"))) # if we find a smaller character we add it to the result only once and repeat the process
                freq[smaller_char_index] -= 1 # Reduce the frequency of the smaller character

        return "".join(result) # Convert the result array to a string