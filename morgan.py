    #################################################
    # Each team's file must define four tokens:     #
    #   team_name: a string                         #
    #     strategy_name: a string                   #
    #     strategy_description: a string            #
    #     move: A function that returns 'c' or 'b'  #
    #################################################

team_name = 'Morgan5Wilson' # Only 10 chars displayed.
strategy_name = 'Playing it safe.'
strategy_description = 'As long as my score is higher I will always collude.'


def move(my_history, their_history, my_score, their_score): #positiveresults
    '''import random
    list = ('c', 'b')
    if my_score > their_score:
        return 'c'
        if my_score <their_score:
            return 'c'
            if their_history[-1] == 'c':
                return 'c'
                if my_history[-1] =='c':
                    return 'c'
                else:
                    return random.choice(list)'''
    return 'c'

    
    #################################################################################################################
    # Arguements Accepted:  my_history, their_history are strings; my_score, their_score are ints                   #
    # my_history:           a string with one letter (c or b) per round that has been played with this opponentself.#
    # their_history:        a string of the same length as history, possibly emptyself                              #
    # first round:          my_history[0] and their_history[0]                                                      #
    # most recent round:    my_history[-1] and their_history[-1]                                                    #
    # Analyze my_history and their_history and/or my_score and their_score                                          #
    # Make my move:         Returns 'c' or 'b'.                                                                     #
    # c =                   COLLUDE                                                                                 #
    # b =                   BETRAY                                                                                  #
    #################################################################################################################

def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
            
            ##################################################################### 
            # Note the scores are for testing move()                            #
            # The history and scores don't need to match unless                 #
            # that is relevant to the test of move(). Here,                     #
            # the simulation (if working correctly) would have awarded          #
            # 300 to me and -750 to them. This test will pass if and only if    #
            # TODO: write code...                                               #
            # move('bbb', 'ccc', 0, 0) returns 'b'.                             #
            #####################################################################
              
              my_score=0, 
              their_score=0,
              result='b')             