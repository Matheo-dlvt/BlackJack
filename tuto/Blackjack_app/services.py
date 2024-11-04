from Blackjack_app.models import Game
from Blackjack_app.models import Player

def create_game(game_name:str, players: list[str]):
    game = Game.objects.create(name=game_name)
    
    for p in players:
        Player.objects.create(name=p, game=game_name)

def get_players(game_id):
    game = Game.object.get(pk=game_id)
    players = game.players.all()
    return players

def get_score(player_id):
    player = Player.objects.get(pk=player_id)
    return player.score

def change_score(player_id, score):
    player = Player.objects.get(pk=player_id)
    player.score = score

def get_winner(game_id):
    pass