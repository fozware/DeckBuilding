from Game.Effects.Conditions.Filters.Operations.operations import operations
from Game.Sources.source_factory import SourceFactory

class SourceCriteria:
    """ Represents a Criteria based on values from a source """
    
    def __init__(self, field, sourceType):
        """ Initialize the Fixed Criteria """
        self.field = field
        self.sourceType = sourceType
        self.operation = operations["IN"]
        
    def compare(self, card, game, event=None):
        """ Compare the card with the Matching Condition """
        source = SourceFactory.getSource(self.sourceType, game, event=event)
        value = getattr(card, self.field)
        return self.operation(value, [getattr(sourceCard, self.field) for sourceCard in source])