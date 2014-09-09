from Game.Effects.Conditions.Operations.operations import operations
from Game.Sources.source_factory import SourceFactory

class Filter:
    """ Represents a filter that returns all the matching cards from a source """
    
    def __init__(self, field, values, sourceType):
        """ Initialize the filter """
        self.field = field
        self.values = values
        self.sourceType = sourceType
        self.operation = operations["IN"]
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        source = SourceFactory.getSource(self.sourceType, game, event=event)
        return [card for card in source if self.compare(card)]
        
    def compare(self, card):
        """ Compare the card with the Matching Condition """
        value = getattr(card, self.field)
        return self.operation.compare(value, self.values)