from Game.Effects.effect_runner import PerformEffect
from Game.Effects.Conditions.has_cards import HasCards
from Game.Events.top_card_event import TopCardEvent
from Game.Sources.source_factory import SourceFactory

class LookAtTop:
    """ Represents an effect to Look at the top Card of a source """
    
    def __init__(self, sourceType, thenEffect):
        """ Initialize the Effect with the source to look at """
        self.sourceType = sourceType
        self.thenEffect = thenEffect
        self.condition = HasCards(self.sourceType)
        
    def perform(self, args):
        """ Perform the Game Effect """
        if self.condition.evaluate(args.game, event=args.event):
            source = SourceFactory.getSource(self.sourceType, args.game, event=args.event)
            card = source[0]
            event = TopCardEvent(card, source, args.game)
            coroutine = PerformEffect(self.thenEffect, event.args)
            response = yield coroutine.next()
            while True:
                response = yield coroutine.send(response)