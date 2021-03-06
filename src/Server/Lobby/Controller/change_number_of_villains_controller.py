from Server.Lobby.lobbies import lobbies
from kao_flask.controllers.json_controller import JSONController

class ChangeNumberOfVillainsController(JSONController):
    """ Controller to handle changing the number of villains via JSON """
    
    def performWithJSON(self, lobbyId, playerId, json=None):
        lobby = lobbies[lobbyId]
        player = lobby.players[playerId]
        lobby.lobby.gameMode.setNumberOfVillains(json['index'])
        return lobbies[lobbyId].toJSONForPlayer(playerId), 201