"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########

# Problem 1 
def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.    # 这个题的意思是说, 将参数段落中所有满足selet条件的段落找出来, 组成一个新的list, 然后返回新段落中的第k个元素,如果K大于组成新段落的长度, 则返回空字符串
                         # 这里面属于有个问题,就是说PARAGRAPHS是代表了存储字符串的列表,而paragraphs仅仅只是PARAGRAPHS中的字符串
    Arguments:
        paragraphs: a list of strings        # 一个都是字符串的的列表
        select: a function that returns True for paragraphs that can be selected    # 一个函数, 返回真. 如果这个段落可以被选择(我理解的是相当于一个选择段落的条件)
        k: an integer           # 一个整数

    >>> ps = ['hi', 'how are you', 'fine']     # 一个都是字符串的列表
    >>> s = lambda p: len(p) <= 4             # 判断字符串是否满足长度小于等于4的条件, 如果满足返回true, 
    >>> pick(ps, s, 0)              # PS这个段落中, 判断第0个元素, 是否满足S的条件, 如果满足就PICK, 如果不满足就返回空集
    'hi'                        # PS的第0个元素,满足长度小于等于4这个条件,所以就返回
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)      
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    #if select(paragraphs[k]) == True:
    #    return paragraphs[k]
    #else:
    #    return ''
    list = []
    for index in range(len(paragraphs)):
        if select(paragraphs[index]) == True:
            list.append(paragraphs[index])
            # print(list)    # only for debug
    if k > len(list) - 1:
        # print("k is too large!") # only for debug
        return ''
    else:
        return list[k]     
    # END PROBLEM 1           # PROBLEM 1 finish


def about(subject):
    """Return a select function that returns whether
    a paragraph contains one of the words in SUBJECT.    # 它返回一个函数，该函数接受一个段落并返回一个布尔值，指示该段落是否包含主题中的任何单词。
                                                         # 这里面的 paragraph 术语是说大的PARAGRAPHS中的字符串
    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def myfunction(paragraph):
        #for text in paragraph:
        #    list = split(text)
        #    for element in list:
        #        if remove_punctuation(element) in subject:
        #            print(text)     # only for debug
        #            return True
        list = split(paragraph)    # 首先将字符串转换成列表，每个元素是一个单词包括标点
        for element in list:     # 遍历列表
            word = lower(remove_punctuation(element))  # 将list中的元素去除标点得到单词, 然后再小写化，得到最终单词
            if word in subject:
                # print(word)       # only for debug
                return True
        return False

    return myfunction
    # END PROBLEM 2                # END PROBLEM 2 finished

#临时区域，用来写一个函数作为测试用

def check(paragraph,  subject):  # 写一个函数，输入是段落，和主题词，如果段落中有含有subject中的单词，则返回true以及段落中的单词
#    for x in paragraph:
#        for y in subject:
            #if y in list(x):
#            if y in split(x):
#                print(x)
#                return True
#            return False
    for string in paragraph:
        #print(string)  # only for debug
        #print(type(string))
        list = split(string)
        #print(list)     # only for debug
        for element in list:
        #for element in subject:
            #if element in list:
            if remove_punctuation(element) in subject:             # 如果去掉标点之后的元素，在subject中可以找到
            #    print(element)     # only for debug
                #print(remove_punctuation(element))      # only for debug   打印去掉标点之后的元素
                #print(list)
                print(string)
                #return True
            #print(element)        # only for debug
    #return False
# subject = ['dog', 'dogs', 'pup', 'puppy', 'cat']
# subject = ['dog', 'dogs', 'cat']
# paragraph = ['Cute dog!', 'That is a cat.', 'Nice pup!']
# paragraph = ['Cute dog', 'That is a cat', 'Nice pup!']
# paragraph = ['Cute', 'That is a cat', 'Nice pup!']
# paragraph = 'Cute dog!'
# check(paragraph, subject)
#临时区域结束


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if (typed == '' and source != '') or (typed != '' and source == ''):
        return float(0)
    elif typed == '' and source == '':
        return float(100)
    else:
        result = 0
        count = 0
        for i in range(len(typed_words)):
            if i >= len(source_words):
                break
            elif typed_words[i] == source_words[i]:
                count += 1
        #elif i >= len(source_words):
         #   break
        result = float( count / len(typed_words) * 100)
        return result
    # END PROBLEM 3                # PROBLEM 3 finish


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string                     # 官方的文档里是说WPM计算不是用多少个字,而是总共多少个字符再除以5
        elapsed: an amount of time in seconds        # WPM 的M是分钟的意思,这里的参数都是秒, 要换算

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    result = 0
    total = len(typed) / 5      # 先找到一共打了多少字符，并除以5
    minutes = float(elapsed / 60)
    result = float(total / minutes)
    return result 
    # END PROBLEM 4    # PROBLEM 4 finished
             
    



############
# Phase 2A #
############


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.

    Arguments:
        typed_word: a string representing a word that may contain typos  # 一个字符串代表了一个单词里面可能包括了错误的拼写
        word_list: a list of strings representing source words          # 一个清单,元素都是字符串 代表了源单词
        diff_function: a function quantifying the difference between two words    # 一个函数确定两个单词之间的差异
        limit: a number            # 一个数字

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10         # 差异始终为10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)      # hwllo与["butter", "hello", "potato"]中的所有项差异都为10, 小于20,返回第一个元素
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # 计算输入单词和单词列表的所有的差异difference，存进一个新的list，
    # 将这个list中最小的项对应的元素位置在 word_list 中找到返回即可，如果最小的这个值也大于limit返回元单词即可
    dif_list = []
    for element in word_list:
        difference = diff_function(typed_word, element, limit)   # 得到输入单词和每一个单词之间的差异
        dif_list.append(difference)             # 将所有差异存入列表
    min_dif = min(dif_list, key = abs)      # 找到差异最小的首个元素
    if min_dif > limit:     # 如果最小差异值比限制条件要大
        return typed_word     # 无法自动纠错，
    else: 
        for index in range(len(dif_list)):
            if dif_list[index] == min_dif:
                return word_list[index]           # END PROBLEM 5 finished
    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change    # 这个LIMIT参数有什么实际作用,我暂时没看明白

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    #assert False, 'Remove this line'        # 另外这道题要求用递归解决, 我暂时用迭代解决
    result = 0
    count = 0
    # 先得到两者共同长度的部分
    length = min(len(typed), len(source))
    # 对于共同长度的部分，先进行比较
    for i in range(length):
        if typed[i] != source[i]:
            count += 1
    # 最后再加上多出的部分
    result = max(len(typed), len(source)) - length + count
    return result
    # END PROBLEM 6         END PROBLEM 6 finished
    





############
# Phase 2B #
############

# Problem 7 (3 pts)
def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    #assert False, 'Remove this line'
    #if ___________: # Base cases should go here, you may add more base cases as needed.
    #    # BEGIN
    #    "*** YOUR CODE HERE ***"
    #    # END
    # Recursive cases should go below here
    #if ___________: # Feel free to remove or add additional cases
    #    # BEGIN
    #    "*** YOUR CODE HERE ***"
    #    # END
    #else:
    #    add = ... # Fill in these lines
    #    remove = ...
    #    substitute = ...
    #    # BEGIN
    #    "*** YOUR CODE HERE ***"
    #    # END
    ## 上面给出的模板全部不看
    
##练习区域：    
##首先我要写一个函数，找到cats和scat中重合的部分
#def find_common(string1, string2):
#    list = []    #建立一个空列表
#    for s1_index in range(len(string1)):
##            if string1[s1_index] == string2[s1_index]:         # Problem 7 finished

    
        
        




def final_diff(typed, source, limit):
    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function.'

FINAL_DIFF_LIMIT = 6 # REPLACE THIS WITH YOUR LIMIT


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    #get the progress so far
    count = 0
    for index in range(len(typed)):
        if typed[index] == source[index]:
            count += 1
        elif typed[index] != source[index]:
            break
    progress = float(count / len(source))
    # upload id and progress
    dict = {
        'id': user_id, 
        'progress': progress
    }
    upload(dict) 
    return progress
    # END PROBLEM 8       # PROBLEM 8 finished

# 第九题和第十题用到了“DATA ABSTRACTION”的概念，是后面要学习的内容，暂时性跳过
def time_per_word(words, timestamps_per_player):
    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(get_all_words(match)), "word_index out of range of words"
    return get_all_words(match)[word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(get_all_words(match)), "word_index out of range of words"
    assert player_num < len(get_all_times(match)), "player_num out of range of players"
    return get_all_times(match)[player_num][word_index]

def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]

def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match data abstraction and returns a string representation of it"""
    return f"match({get_all_words(match)}, {get_all_times(match)})"

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)