def interval_search(word, intervals):
    # Determine which interval the word is located in
    first_letter = word[0].upper()
    interval = intervals.get(first_letter)
    if not interval:
        return -1
    # Perform binary search within the interval
    left = 0
    right = len(interval) - 1
    while left <= right:
        mid = (left + right) // 2
        if interval[mid][0] == word:
            return interval[mid][1]
        elif interval[mid][0] < word:
            left = mid + 1
        else:
            right = mid - 1
    return -1
#Function to determine the intervals for the search
def create_intervals(dictionary):
    intervals = {}
    with open(dictionary, 'r') as file:
        for i,line in enumerate(file):
            word = line.strip().upper()
            if word[0] not in intervals:
                intervals[word[0]] = []
            intervals[word[0]].append((word, i))
    return intervals

def find_word_position(word, dictionary):
    intervals = create_intervals(dictionary)
    return interval_search(word.upper(), intervals)

def main():
    # Import and read the given dictionary
    dictionary = f = open("words.txt", "r")
    print(f.read())
    try:
        word = input("Enter the word you want to search for: ")
        position = find_word_position(word, dictionary)
        if position != -1:
            print(f"The word '{word}' is located at line {position + 1} in the dictionary.")
        #Error routine
        else:
            print(f"The word '{word}' was not found in the dictionary.")
    except FileNotFoundError:
        print(f"The file {dictionary} could not be found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()