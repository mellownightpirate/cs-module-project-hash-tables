import re
# '\\\\' is required to escape backslash '\'
ignore = re.compile('[-\\\\":;,.+=\/|\[\]`{}()*^&]')

def word_count(s):
    # Your code here
    strip_ignored = ignore.sub("", s)
    word_list = strip_ignored.split()
    ans = {}
    for word in word_list:
        lower_word = word.lower()
        if lower_word in ans:
            ans[lower_word] += 1
        else:
            ans[lower_word] = 1
    return ans


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))