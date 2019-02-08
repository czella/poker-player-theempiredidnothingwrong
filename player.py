import sys
import math

class Player:
    VERSION = "DS.2.2.0"
    testJSon = """{'community_cards': [], 
'minimum_raise': 2, 
'big_blind': 4, 
'orbits': 0, 
'in_action': 3, 
'bet_index': 2, 
'current_buy_in': 4, 
'round': 0, 
'players': [{'id': 0, 'bet': 0, 'version': 'Pony 1.0.0', 'time_used': 0, 'stack': 1000, 'status': 'active', 'name': 'Bright Pony'}, 
            {'id': 1, 'bet': 2, 'version': '1.0', 'time_used': 0, 'stack': 998, 'status': 'active', 'name': 'PokerMasters'}, 
            {'id': 2, 'bet': 4, 'version': 'ERROR: Unreachable', 'time_used': 0, 'stack': 996, 'status': 'active', 'name': 'NADagascar'}, 
            {'hole_cards': [{'suit': 'hearts', 'rank': '4'}, 
                            {'suit': 'diamonds', 'rank': 'Q'}], 
              'bet': 0, 
              'version': 'DS.1.0.0', 
              'time_used': 0, 
              'id': 3, 
              'stack': 1000, 
              'status': 'active', 
              'name': 'TheEmpireDidNothingWrong'}, 
            {'id': 4, 
            'bet': 0, 
            'version': '1.0', 
            'time_used': 0, 
            'stack': 1000, 
            'status': 'active', 
            'name': 'Hive'}, 
            {'id': 5, 'bet': 0, 'version': 'Gopnik_FM_ver_1.0', 'time_used': 0, 'stack': 1000, 'status': 'active', 'name': 'Gopnik FM'}], 
'small_blind': 2, 
'game_id': '5c5d4b96a972e80004000021', 
'dealer': 0, 
'pot': 6, 
'tournament_id': '5c38a553b0fea40004000003'}
    """

    def betRequest(self, game_state):
        sys.stdout.write("_______ WE'RE ON!!4!4 ______" + "\n")
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                 '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        high_ranks = ['10', 'J', 'Q', 'K', 'A']
        current_buy_in = int(game_state['current_buy_in'])
        minimum_raise = int(game_state['minimum_raise'])
        our_bet = 0
        still_close = 2

        try:
            # searching for our player
            my_player = dict()
            for player in game_state['players']:
                if player['name'] == 'TheEmpireDidNothingWrong':
                    my_player = player

            # getting our data
            my_stack = int(my_player['stack'])
            my_cards = my_player['hole_cards']

            # checking if we have a pair
            my_ranks = [card['rank'] for card in my_cards]
            if my_ranks[0] == my_ranks[1]:
                our_bet = my_stack
                sys.stdout.write("Bet calculated based on PAIR: " + str(our_bet) + "\n")

            # checking if we have high ranks
            elif my_ranks[0] in high_ranks or my_ranks[1] in high_ranks:
                if my_ranks[0] in high_ranks and my_ranks[1] in high_ranks:
                    our_bet = min(my_stack, current_buy_in + minimum_raise)
                    sys.stdout.write("Bet calculated based on TWO HIGH RANKS: " + str(our_bet) + "\n")
                else:
                    if current_buy_in < 100:
                        our_bet = current_buy_in + minimum_raise
                        sys.stdout.write("Bet calculated based on ONE HIGH RANK: " + str(our_bet) + "\n")

            # checking if our ranks are close
            elif abs(my_ranks[0] - my_ranks[1]) <= still_close:
                our_bet = min(my_stack, current_buy_in + minimum_raise)
                sys.stdout.write("Bet calculated based on CLOSE RANKS: " + str(our_bet) + "\n")

        except Exception as e:
            our_bet = 0
            sys.stdout.write(str(e))
            sys.stdout.write("Bet calculated based on caught exception: " + str(our_bet) + "\n")
        sys.stdout.write("Our bet: " + str(our_bet) + "\n")
        sys.stdout.write("Bet value type: " + str(type(our_bet)) + "\n")
        return our_bet

    def showdown(self, game_state):
        pass

