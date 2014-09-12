from Game.Sources.source_factory import SourceFactory, DISCARD_PILE

class BuyCard:
    """ Represents a command to buy a card """
    
    def __init__(self, card, owner, source):
        """ Initialize the Buy Card Command """
        self.card = card
        self.owner = owner
        self.source = source
        
    def perform(self):
        """ Perform the command """
        self.owner.spendPower(self.card.calculateCost())
        self.owner.gainCard(self.card, self.source, destinationSource=SourceFactory.getSource(DISCARD_PILE, self.owner.game))