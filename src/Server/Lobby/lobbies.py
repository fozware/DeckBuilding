from lobby_wrapper import LobbyWrapper
from Lobby.lobby import Lobby
from helpers.incrementer import Incrementer

lobbyIdProvider = Incrementer(startAt=1)
lobbies = {}
lobbyIdToPlayers = {}
lobbyIdToIncrementer = {}

def StartNewLobby():
    """ Start a New Lobby """
    global lobbies
    
    lobby = Lobby()
    currentId = lobbyIdProvider.next()
    lobby.id = currentId
    lobbies[currentId] = lobby
    id += 1
    return lobbies[currentId]
        
def AddPlayerToLobby(lobbyId):
    """ Add a player to the Lobby """
    global lobbies
    global lobbyIdToIncrementer
    global lobbyIdToPlayers
    
    if lobbyId not in lobbyIdToIncrementer:
        lobbyIdToIncrementer[lobbyId] = Incrementer(startAt=1)
    if lobbyId not in lobbyIdToPlayers:
        lobbyIdToPlayers[lobbyId] = {}
        
    playerIdProvider = lobbyIdToIncrementer[lobbyId]
    playerId = playerIdProvider.next()
    player = PlayerInLobby()
    player.id = playerId
    lobbyIdToPlayers[lobbyId][playerId] = player
    lobbies[lobbyId].addPlayer(player)
    return playerId