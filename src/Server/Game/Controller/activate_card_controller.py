from Game.Commands.activate_card import ActivateCard
from Game.Sources.source_factory import SourceFactory
from Server.Game.games import games

from kao_flask.controllers.json_controller import JSONController

class ActivateCardController(JSONController):
    """ Controller to activate a card """
    
    def performWithJSON(self, gameId):
        game = games[gameId]
        cardIndex = self.json['index']
        sourceType = self.json['source']
        
        card = None
        source = SourceFactory.getSource(sourceType, game.game)
        card = source[cardIndex]
        
        game.game.currentTurn.perform(ActivateCard(card, game.game.currentTurn))
        return game.toJSON()