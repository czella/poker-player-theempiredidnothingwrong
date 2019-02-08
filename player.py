import sys

class Player:
    VERSION = "DS.2.1.0"
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
        sys.stdout("_______ WE'RE ON!!4!4 ______")
        sys.stdout("_______ NEXT LINE ______")
        high_ranks = ['J', 'Q', 'K', 'A']
        current_buy_in = int(game_state['current_buy_in'])
        our_bet = 0

        try:
            # searching for our player
            for player in game_state['players']:
                if player['name'] == 'TheEmpireDidNothingWrong':
                    # getting our data
                    my_stack = int(player['stack'])
                    my_cards = player['hole_cards']
                    # checking our cards
                    for card in my_cards:
                        if card['rank'] in high_ranks:
                            if current_buy_in + 10 > my_stack:
                                our_bet = my_stack
                            else:
                                our_bet = current_buy_in + 10
        except:
            our_bet = 0

        return our_bet

    def showdown(self, game_state):
        pass

