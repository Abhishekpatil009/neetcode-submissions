class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Create an empty dictionary
        # It will store each number and its frequency
        freq = {}

        # Step 2: Count the frequency of each number
        for num in nums:

            # If num exists, get its current frequency.
            # Otherwise, get 0.
            # Then increase the frequency by 1.
            freq[num] = freq.get(num, 0) + 1

        # Step 3: Sort dictionary items by frequency
        # x[0] represents the number (key)
        # x[1] represents its frequency (value)
        # reverse=True sorts from highest to lowest frequency
        sortedfreq = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        # Step 4: Convert the sorted list of tuples into a dictionary
        freqsorted = dict(sortedfreq)

        # Step 5: Create an empty list to store the answer
        result = []

        # Step 6: Iterate through the sorted dictionary
        for num in freqsorted:

            # If we already have k elements, stop the loop
            if len(result) == k:
                break

            # Add the current number to the result list
            result.append(num)

        # Step 7: Return the final list containing top K frequent numbers
        return result