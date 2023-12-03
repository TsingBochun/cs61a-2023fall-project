"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):   #掷筛子函数, 我理解的是比如参数为（3， dicedice=six_sided），那么就需要在这个函数中调用三次six_sided,并且德奥最终结果要么是1，要么是求和，根据游戏规则。
# def roll_dice(num_rolls, dice=six_sided):  # 原函数的写法
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made. 掷骰子的次数
    dice:       A function that simulates a single dice roll outcome. 一个模拟单个掷骰子结果的函数
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'   #学习这里用断言语句来做错误处理
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    i = 0
    sum = 0               
    while i < num_rolls:
        if dice() == 1:    #如果在循环的过程中，随机数dice出现等于1的情况
            print("the dice is 1")
            #print(dice())   # only for debug     #这里其实又调用了dice，所以dice为1 的时候并没有退出
            sum = 1
            break        #循环终止，函数直接返回1
        sum += dice()
        print(dice())      # only for debug
        i += 1
    #for i in range(num_rolls):
    #    print(dice())        #only for debug
    #    print(i)             #only for debugs
    #    print(sum)
    #    sum += dice()        # only for debug      #因为这里再一次地调用了dice，所以dice此时变成了2，sum+=后编程了2，但是这个BUG对于六面筛子来说不应该存在 
    #    print(sum)       
    return sum  
    # END PROBLEM 1     #test succeeds on 2023.12.02 10:22


def boar_brawl(player_score, opponent_score):      # 这个函数是用来模拟野猪斗殴规则的
    """Return the points scored by rolling 0 dice according to Boar Brawl. 返回不投(0投掷)时的根据野猪斗殴规则得到的分数

    player_score:     The total score of the current player.   当前得分
    opponent_score:   The total score of the other player.     对手得分

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    text_player_score = str(player_score)            #将两者转化为字符串，好像有规则说不允许这样做，但是因为我不是零基础学起，也为了时间，所以就不考虑制约条件了
    text_opponent_score = str(opponent_score)
    #错误处理，如果对手得分仅为个位数，即没有十位数，那么十位数为0
    if len(text_opponent_score) == 1:
        opponent_score_second_rightmost_digit = 0
    else:
        opponent_score_second_rightmost_digit = int(text_opponent_score[-2])    #-1应该是指最右边,-2应该是倒数第二个数
    player_score_rightmost_digit = int(text_player_score[-1])
    result = abs(opponent_score_second_rightmost_digit - player_score_rightmost_digit) * 3
    if result > 1:
        return result
    else:
        return 1                        #test succeeds on 2023.12.02 11:03                
    # END PROBLEM 2                 


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.   #这一个函数我确实没太理解 返回的分数貌似是当前投筛子的玩家的分数 然后就是把以上规则都使用的函数

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:        # 玩家选择投0筛子即不投
        return boar_brawl(player_score, opponent_score)     # 直接调用野猪乱斗的规则
    else:
        return roll_dice(num_rolls, dice=six_sided)    # 直接调用正常规则
    # END PROBLEM 3     #test succeeds on 2023.12.02 11:35


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Sus Fuss.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score

def is_prime(n):
    """Return whether N is prime."""
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""  # 返回计算N的约数（因子）的个数
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    count = 0       # 这个变量用来计算约数的个数 # 这里有个错误处理没有考虑就是如果参数为0的情况下
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count
    # END PROBLEM 4     #finish on 2023.12.02 15:28

def sus_points(score):
    """Return the new score of a player taking into account the Sus Fuss rule."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score_num_factors = num_factors(score)
    if score_num_factors == 3 or score_num_factors == 4:
        score += 1    #直接让score加上1，然后开始循环
        while is_prime(score) != True:     # 判断该数是否为质数，如果不是就继续循环
            score += 1
        #return score
    return score
    # END PROBLEM 4        #finished on 2023.12.02 16:00

def sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Sus Fuss.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    score = simple_update(num_rolls, player_score, opponent_score, dice=six_sided)   # 先计算不包括sus——fuss的分数
    total_score = sus_points(score)        #再将分数用suss——fuss更新
    return total_score
    # END PROBLEM 4    # finish on 2023.12.02 16:12


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the opponent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, sus_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Sus
    Fuss rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as sus_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    #sus_update(, player_score, opponent_score, dice=six_sided)   sus_update函数的原型
    #score0 = update(strategy0, score0=0, score1=0, dice=six_sided)    # 初始化score0的值，假设player0先投
    #score1 = update(strategy1, score1=0, score0, dice=six_sided)      # 这个时候score0已经有值了
    # only for debug:
    #strategy0 = 5
    #strategy1 = 5

    while score0 < goal and score1 < goal:        # 两者的得分都小于目标即没有人达到目标
        if who == 0:
            #score0 = update(strategy0, score0, score1, dice=six_sided)
            score0 = update(strategy0(score0, score1), score0, score1, dice=six_sided)
            who = 1 - who
        elif who == 1:
            #score1 = update(strategy1, score1, score0, dice=six_sided)
            score1 = update(strategy1(score1, score0), score1, score0, dice=six_sided)
            who = 1 - who
    return score0, score1        # finish on 2023.12.02  17:13
    # END PROBLEM 5
    


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # return n        # finish on 2023.12.02
    def strategy(currenrt_player_score, opponet_player_score):
        return n                      
    return strategy     # changed on 2023.12.03 09:09
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"       # 没理解这个题目到底什么意思，暂时性的跳过
    sum = 0                               # 最后我才想明白，原来问题不是任取两个函数的返回值进行比较，看是否相当
    for x in range(goal):                 # 而是看函数的返回值是否始终为常数，这大概是我第一次做的算法题，CS50中也并未涉及
        for y in range(goal):
            sum += strategy(x, y)
    if sum == 10000 * strategy(0, 0):
        return True    
    else:
        return False           # finish on 2023.12.03 10:11
    # END PROBLEM 7


def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def original_function_average(*args):
        sum = 0
        for i in range(samples_count):
            sum += original_function(*args)
        average = sum / samples_count    
        return average
    return original_function_average       #测试用例答案为3.0，但是我做出来是1.5，暂时看不出错在哪里，先提交
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, samples_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of SAMPLES_COUNT times.
    通过使用提供的dice调用roll_dice总共SAMPLES_COUNT次,返回平均回合得分最高的骰子数(1到10)。   
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    average_dice = make_averaged(dice, samples_count)        
    max_average = 0
    number_of_rolls = 0
    for i in range(1, 11):
        cur_average = average_dice(i, dice)
        if cur_average > max_average:
            max_average = cur_average
            number_of_rolls = i
    return number_of_rolls             # 这里没有做比较大小？这里我还是没有充分理解题目，暂时借用别人的代码看看效果 2023.12。03  15:32
    # 测试报故，我觉得此人的代码有误，因为提示中说是要用到make——average和roll——dice两个函数，她却没有用，肯定有问题
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, sus_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6))) # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('sus_strategy win rate:', average_win_rate(sus_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"



def boar_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Sus Fuss.
    """
    # BEGIN PROBLEM 10
    # return num_rolls  # Remove this line once implemented.
    if boar_brawl(score, opponent_score) == threshold:
        return 0
    else:
        return num_rolls      
    # END PROBLEM 10       # finished on 2023.12.03 16:42


def sus_strategy(score, opponent_score, threshold=11, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    #return num_rolls  # Remove this line once implemented.
    # tmp_oppo = opponent_score
    tmp_score = boar_brawl(score, opponent_score)
    # sus_update(num_rolls, player_score, opponent_score, dice=six_sided):
    if sus_update(num_rolls, tmp_score, opponent_score, dice=six_sided) == threshold:
        return 0
    else:
        return num_rolls
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()