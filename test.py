import player
import json

testJSon = json.loads("""{"community_cards": [],
"minimum_raise": 2, 
"big_blind": 4, 
"orbits": 0, 
"in_action": 3, 
"bet_index": 2, 
"current_buy_in": 4, 
"round": 0, 
"players": [{"id": 0, "bet": 0, "version": "Pony 1.0.0", "time_used": 0, "stack": 1000, "status": "active", "name": "Bright Pony"}, 
            {"id": 1, "bet": 2, "version": "1.0", "time_used": 0, "stack": 998, "status": "active", "name": "PokerMasters"}, 
            {"id": 2, "bet": 4, "version": "ERROR: Unreachable", "time_used": 0, "stack": 996, "status": "active", "name": "NADagascar"}, 
            {"hole_cards": [{"suit": "hearts", "rank": "4"}, 
                            {"suit": "diamonds", "rank": "Q"}], 
              "bet": 0, 
              "version": "DS.1.0.0", 
              "time_used": 0, 
              "id": 3, 
              "stack": 1000, 
              "status": "active", 
              "name": "TheEmpireDidNothingWrong"}, 
            {"id": 4, 
            "bet": 0, 
            "version": "1.0", 
            "time_used": 0, 
            "stack": 1000, 
            "status": "active", 
            "name": "Hive"}, 
            {"id": 5, "bet": 0, "version": "Gopnik_FM_ver_1.0", "time_used": 0, "stack": 1000, "status": "active", "name": "Gopnik FM"}], 
"small_blind": 2, 
"game_id": "5c5d4b96a972e80004000021", 
"dealer": 0, 
"pot": 6, 
"tournament_id": "5c38a553b0fea40004000003"}
    """)

if __name__ == "__main__":
    player = player.Player();
    print(player.betRequest(testJSon))