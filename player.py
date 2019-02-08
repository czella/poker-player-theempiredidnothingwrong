import os
import sys
import math


class Player:
    VERSION = "DS.5.6.0"
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
        sys.stdout.write(str(game_state) + "\n")
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                 '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        high_ranks = ['J', 'Q', 'K', 'A']
        current_buy_in = int(game_state['current_buy_in'])
        minimum_raise = int(game_state['minimum_raise'])
        community_cards = game_state['community_cards'] if 'community_cards' in game_state else None
        players = game_state['players']
        our_bet = 0
        still_close = 2
        sys.stdout.write("Initialized round\n")

        try:
            sys.stdout.write("Inside try statement\n")
            # searching for our player
            my_player = dict()
            for player in players:
                if player['name'] == 'TheEmpireDidNothingWrong':
                    my_player = player

            # getting our data
            my_stack = int(my_player['stack'])
            my_cards = my_player['hole_cards']
            my_high_cards = [card for card in my_cards if card['rank'] in high_ranks]
            all_cards = my_cards + community_cards
            my_ranks = [card['rank'] for card in my_cards]
            all_ranks = [card['rank'] for card in all_cards]
            all_suit_frequencies = self.get_suit_frequencies(all_cards)
            hand_suit_frequencies = self.get_suit_frequencies(my_cards)
            community_suit_frequencies = self.get_suit_frequencies(community_cards)

            # checking how many players there are
            if self.get_active_players(players) <= 6:

                # checking if we have a high rank pair
                if my_ranks[0] == my_ranks[1] and my_ranks[0] in high_ranks:
                    our_bet = self.handle_high_rank_pair(all_cards, my_stack)

                # checking if we have a high rank pair with one of the community cards
                elif len(my_high_cards) > 0:
                    for high_card in my_high_cards:
                        if self.is_there_pair_with_community_deck(high_card, community_cards):
                            if current_buy_in>my_stack:
                                our_bet = my_stack
                            else:
                                our_bet = current_buy_in
                        elif len(my_high_cards) >= 2:
                            if current_buy_in>my_stack:
                                our_bet = my_stack
                            else:
                                our_bet = current_buy_in

                # checking if there are 3 cards on the table and 4 identical suits
                elif len(community_cards) == 3 and max(all_suit_frequencies.values()) >= 4:
                    our_bet = current_buy_in + 200

                #checking if flush
                elif len(community_cards) == 5 and max(hand_suit_frequencies.values()) >= 2:
                    if community_suit_frequencies[my_cards[0]["suit"]] >= 3:
                        our_bet = my_stack

                # checking if our ranks are close
                #elif abs(ranks[my_ranks[0]] - ranks[my_ranks[1]]) <= still_close:
                    #our_bet = self.handle_close_ranks(current_buy_in, my_stack)

                # checking if all community cards are dealt
                elif community_cards is not None and len(community_cards) >= 4:
                    our_bet = current_buy_in
                    sys.stdout.write("Bet calculated based on ALL CARDS ON TABLE: " + str(our_bet) + "\n")

                else:
                    sys.stdout.write("We don't have any high ranks I guess :/")
            else:
                our_bet = 0
                sys.stdout.write("Too many players for us :( \n")

        except Exception as e:
            our_bet = 0

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            sys.stdout.write(str(e) + "\n")
            # print call stack
            sys.stdout.write(", ".join([str(exc_type), str(fname), str(exc_tb.tb_lineno)]) + "\n")
            sys.stdout.write("Bet calculated based on caught exception: " + str(our_bet) + "\n")

        # log state
        sys.stdout.write("Our bet: " + str(our_bet) + "\n")
        sys.stdout.write("Bet value type: " + str(type(our_bet)) + "\n")

        return our_bet

    def handle_close_ranks(self, current_buy_in, my_stack):
        our_bet = min(my_stack, current_buy_in)
        sys.stdout.write("Bet calculated based on CLOSE RANKS: " + str(our_bet) + "\n")
        return our_bet

    def handle_high_ranks(self, current_buy_in, high_ranks, my_ranks, my_stack):
        if my_ranks[0] in high_ranks and my_ranks[1] in high_ranks:
            our_bet = min(min(my_stack, current_buy_in), my_stack)
            sys.stdout.write("Bet calculated based on TWO HIGH RANKS: " + str(our_bet) + "\n")
        else:
            if False:
                our_bet = current_buy_in
                sys.stdout.write("Bet calculated based on ONE HIGH RANK: " + str(our_bet) + "\n")
            else:
                our_bet = 0
                sys.stdout.write("Bet calculated based on ONE HIGH RANK: " + str(our_bet) + "\n")
        return our_bet

    def handle_high_rank_pair(self, cards, my_stack):
        our_bet = my_stack
        sys.stdout.write("Bet calculated based on PAIR: " + str(our_bet) + "\n")
        return our_bet

    def is_there_pair_with_community_deck(self, my_high_card, community_cards):
        for community_card in community_cards:
            if my_high_card['rank'] == community_card['rank']:
                return True
        return False

    def is_there_drill(self, my_cards):
        pass

    def get_suit_frequencies(self, list_of_cards):
        freq = dict()
        for item in list_of_cards:
            if item['suit'] in freq:
                freq[item['suit']] += 1
            else:
                freq[item['suit']] = 1
        return freq


    def get_active_players(self, players):
        active_players = [player for player in players if player['status'] == 'active']
        return len(active_players)

    def showdown(self, game_state):
        pass

