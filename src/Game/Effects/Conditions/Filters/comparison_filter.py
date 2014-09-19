from Game.Effects.Conditions.Filters.Operations.operations import operations
from Game.Sources.source_factory import SourceFactory

class ComparisonFilter:
    """ Represents a filter that returns all the cards from a source that pass some comparison """
    
    def __init__(self, sourceType, criteria):
        """ Initialize the filter """
        self.sourceType = sourceType
        self.criteria = criteria
        
    def evaluate(self, game, event=None):
        """ Evaluate the condition """
        source = SourceFactory.getSource(self.sourceType, game, event=event)
        return [card for card in source if self.criteria.compare(card, game, event=event)]