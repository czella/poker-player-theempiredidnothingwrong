from sys import stdout


class Player:
    VERSION = "DS.1.0.0"
    testJSon = """{u'community_cards': [], u'minimum_raise': 2, u'big_blind': 4, u'orbits': 0, u'in_action': 3, u'bet_index': 2, u'current_buy_in': 4, u'round': 0, u'players': [{u'id': 0, u'bet': 0, u'version': u'Pony 1.0.0', u'time_used': 0, u'stack': 1000, u'status': u'active', u'name': u'Bright Pony'}, {u'id': 1, u'bet': 2, u'version': u'1.0', u'time_used': 0, u'stack': 998, u'status': u'active', u'name': u'PokerMasters'}, {u'id': 2, u'bet': 4, u'version': u'ERROR: Unreachable', u'time_used': 0, u'stack': 996, u'status': u'active', u'name': u'NADagascar'}, {u'hole_cards': [{u'suit': u'hearts', u'rank': u'4'}, {u'suit': u'diamonds', u'rank': u'Q'}], u'bet': 0, u'version': u'DS.1.0.0', u'time_used': 0, u'id': 3, u'stack': 1000, u'status': u'active', u'name': u'TheEmpireDidNothingWrong'}, {u'id': 4, u'bet': 0, u'version': u'1.0', u'time_used': 0, u'stack': 1000, u'status': u'active', u'name': u'Hive'}, {u'id': 5, u'bet': 0, u'version': u'Gopnik_FM_ver_1.0', u'time_used': 0, u'stack': 1000, u'status': u'active', u'name': u'Gopnik FM'}], u'small_blind': 2, u'game_id': u'5c5d4b96a972e80004000021', u'dealer': 0, u'pot': 6, u'tournament_id': u'5c38a553b0fea40004000003'}
    """

    def betRequest(self, game_state):
        try:
            high_ranks = ['J', 'Q', 'K', 'A']
            for i in game_state['players']:
                if i['name'] == 'TheEmpireDidNothingWrong':
                    my_stack = i['stack']
                    cards = i['hole_cards']
                    for card in cards:
                        if card['rank'] in high_ranks:
                            return my_stack

            stdout(game_state)
            stdout(game_state['players'])
            return 500

        except:
            return 0

    def showdown(self, game_state):
        pass

