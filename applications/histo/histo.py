# Your code here
import re
# '\\\\' is required to escape backslash '\'
ignore = re.compile('[-\\\\":;,.+=\/|\[\]`{}()*^&]')


def histo(filename):
    """
    Print a histogram showing the word count for each word, one hash mark
    for every occurrence of the word.
    Output will be first ordered by the number of words, then by the word
    (alphabetically).
    The hash marks should be left justified two spaces after the longest
    word.
    Case should be ignored, and all output forced to lowercase.
    Split the strings into words on any whitespace.
    Ignore each of the following characters:
    ```
    " : ; , . - + = / \ | [ ] { } ( ) * ^ &
    ```
If the input contains no ignored characters, print nothing.
    """
    with open(filename) as f:
        # 1.Read the file
        text = f.read()
        # 2.Strip it of all ignored chars
        stripped_text = ignore.sub("", text)
        # 3.Split into a list
        words = stripped_text.split()
        # 4.Loop thorugh the list while counting words, finding out the max word length
        count_dict = {}
        max_word = 0
        for word in words:
            if len(word) > max_word:
                max_word = len(word)
            if word.lower() in count_dict:
                count_dict[word.lower()] += 1
            else:
                count_dict[word.lower()] = 1
        # 5.Sort on reverse order of priority(if we need list to be ordered by count first, then alphabetcally, sort first alphabetivally, then by count)
        kv = count_dict.items()
        #
        sorted_kv = list(kv)
        sorted_kv.sort(key=lambda x: (-x[1], x[0]))
        # 6.Build out the answer string and return it
        histo_string = ""
        for word, count in sorted_kv:
            next_line = word.ljust(
                max_word+2).ljust(max_word+2+count, '#') + '\n'
            histo_string += next_line
        return histo_string


print(histo('applications/histo/robin.txt'))
