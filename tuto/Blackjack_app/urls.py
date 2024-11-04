from ninja import NinjaAPI, ModelSchema
from .models import Game, Player
import services

api = NinjaAPI()

class GameSchema(ModelSchema):
    class Meta:
        model = Game
        fields = ["id", "name", "turn", "ended"]
        
class PlayerSchema(ModelSchema):
    class Meta:
        model = Player
        fields = ["id", "name", "score", "game"]

@api.post("/create_game")
def add(request):
    name = request.data.get("name")
    players = request.data.get("players")
    game = services.create_game(name, players)    
    return game
