from json import load

from buttonlayout import ButtonLayout
from game import Game
from hint import Hint

class ALBW(Game):

    def __init__(self):
        super().__init__()

    def getGameNameText(self) -> str:
        return "The Legend of Zelda: A Link Between Worlds"

    def getHintList(self) -> list[Hint]:
        return [  Hint('LR Fortune', '/supportedGames/albw/images/ghost.png', 'Lorule Fortune-Teller Ghost'),
            Hint('HY Graveyard', '/supportedGames/albw/images/ghost.png', 'Hyrule Graveyard Ghost'),
            Hint('S Bridge', '/supportedGames/albw/images/ghost.png', 'Southern Bridge Ghost'),
            Hint('DR N', '/supportedGames/albw/images/ghost.png', 'Dark Ruins North Ghost'),
            Hint('Des E', '/supportedGames/albw/images/ghost.png', 'Desert East Ghost'),
            Hint('ZD', '/supportedGames/albw/images/ghost.png', 'Zoras Domain Ghost'),
            Hint('TR Out', '/supportedGames/albw/images/ghost.png', 'Turtle Rock Outside Ghost'),
            Hint('SW Cucco', '/supportedGames/albw/images/ghost.png', 'Skull Woods Cuccos Ghost'),
            Hint('StyleWoman', '/supportedGames/albw/images/ghost.png', 'Stylish Woman Ghost'),
            Hint('KakWell', '/supportedGames/albw/images/ghost.png', 'Kakariko Well Ghost'),
            Hint('HY Rupee', '/supportedGames/albw/images/ghost.png', 'Hyrule Rupee Rush Ghost'),
            Hint('DP Out', '/supportedGames/albw/images/ghost.png', 'Dark Palace Outside Ghost'),
            Hint('VetThief', '/supportedGames/albw/images/ghost.png', 'Veteran Thief Ghost'),
            Hint('LR Rupee', '/supportedGames/albw/images/ghost.png', 'Lorule Rupee Rush Ghost'),
            Hint('Vacant', '/supportedGames/albw/images/ghost.png', 'Vacant House Ghost'),
            Hint('LR Graveyard', '/supportedGames/albw/images/ghost.png', 'Lorule Graveyard Ghost'),
            Hint('GY Ledge', '/supportedGames/albw/images/ghost.png', 'Graveyard Ledge Ghost'),
            Hint('SpecRock', '/supportedGames/albw/images/ghost.png', 'Spectacle Rock Ghost'),
            Hint('ShadyGuy', '/supportedGames/albw/images/ghost.png', 'Shady Guy Ghost'),
            Hint('WaterfallCave', '/supportedGames/albw/images/ghost.png', 'Waterfall Cave Ghost'),
            Hint('LostWoods', '/supportedGames/albw/images/ghost.png', 'Lost Woods Ghost'),
            Hint('GRF', '/supportedGames/albw/images/ghost.png', 'Great Rupee Fairy Ghost'),
            Hint('TurtleBully', '/supportedGames/albw/images/ghost.png', 'Turtle Bullied Ghost'),
            Hint('HoGIsle', '/supportedGames/albw/images/ghost.png', 'House of Gales Island Ghost'),
            Hint('SmithCave', '/supportedGames/albw/images/ghost.png', 'Blacksmith Cave Ghost'),
            Hint('IceRuin Out', '/supportedGames/albw/images/ghost.png', 'Ice Ruins Outside Ghost'),
            Hint('MoldormCave', '/supportedGames/albw/images/ghost.png', 'Moldorm Cave Ghost"'),
            Hint('HY Hotfoot', '/supportedGames/albw/images/ghost.png', 'Hyrule Hotfoot Ghost'),
            Hint('SP OutsideL', '/supportedGames/albw/images/ghost.png', 'Swamp Palace Outside Left Ghost'),
            Hint('SP OutsideR', '/supportedGames/albw/images/ghost.png', 'Swamp Palace Outside Right Ghost'),
            Hint('OctoDerby', '/supportedGames/albw/images/ghost.png', 'Octoball Derby Ghost'),
            Hint('HY CastleRock', '/supportedGames/albw/images/ghost.png', 'Hyrule Castle Rocks Ghost'),
            Hint('S Ruins', '/supportedGames/albw/images/ghost.png', 'Southern Ruins Ghost'),
            Hint('HY Fortune', '/supportedGames/albw/images/ghost.png', 'Hyrule Fortune-Teller Ghost'),
            Hint('SW S', '/supportedGames/albw/images/ghost.png', 'Skull Woods South Ghost'),
            Hint('LW Maze1', '/supportedGames/albw/images/ghost.png', 'Lost Woods Maze Ghost 1'),
            Hint('ER Peg', '/supportedGames/albw/images/ghost.png', 'Eastern Ruins Pegs Ghost'),
            Hint('FloatIsle', '/supportedGames/albw/images/ghost.png', 'Floating Island Ghost'),
            Hint('ER Cave', '/supportedGames/albw/images/ghost.png', 'Eastern Ruins Cave Ghost'),
            Hint('Des SW', '/supportedGames/albw/images/ghost.png', 'Desert Southwest Ghost'),
            Hint('Witch', '/supportedGames/albw/images/ghost.png', 'Witchs House Ghost'),
            Hint('MM Bridge', '/supportedGames/albw/images/ghost.png', 'Misery Mire Bridge Ghost'),
            Hint('CuccoDodge', '/supportedGames/albw/images/ghost.png', 'Dodge the Cuccos Ghost'),
            Hint('FireCave', '/supportedGames/albw/images/ghost.png', 'Fire Cave Ghost'),
            Hint('MM Ledge', '/supportedGames/albw/images/ghost.png', 'Misery Mire Ledge Ghost'),
            Hint('TreacherousTower', '/supportedGames/albw/images/ghost.png', 'Treacherous Tower Ghost'),
            Hint('LW Maze3', '/supportedGames/albw/images/ghost.png', 'Lost Woods Maze Ghost 3'),
            Hint('BehindSmith', '/supportedGames/albw/images/ghost.png', 'Behind Blacksmith Ghost'),
            Hint('Sanctuary', '/supportedGames/albw/images/ghost.png', 'Santuary Ghost'),
            Hint('DarkMaze', '/supportedGames/albw/images/ghost.png', 'Dark Maze Ghost'),
            Hint('StreetPass', '/supportedGames/albw/images/ghost.png', 'StreetPass Tree Ghost'),
            Hint('ToH Out', '/supportedGames/albw/images/ghost.png', 'Outside Tower of Hera Ghost'),
            Hint('ER Entrance', '/supportedGames/albw/images/ghost.png', 'Eastern Ruins Entrance Ghost'),
            Hint('FortuneChoice', '/supportedGames/albw/images/ghost.png', 'Fortunes Choice Ghost'),
            Hint('TurtleWall', '/supportedGames/albw/images/ghost.png', 'Turtle Wall Ghost'),
            Hint('Des Center', '/supportedGames/albw/images/ghost.png', 'Desert Center Ghost'),
            Hint('LW Maze2', '/supportedGames/albw/images/ghost.png', 'Lost Woods Maze Ghost 3'),
            Hint('BottleLetter', '/supportedGames/albw/images/ghost.png', 'Letter in a Bottle Ghost'),
            Hint('LightBow', '/supportedGames/albw/images/ghost.png', 'Bow of Light Hint')
        ]

   
    def readFromSpoilerLog(self, f) -> dict:
        with open(f) as myFile:
            data = load(myFile)
        gossipStoneJson = dict(data['gossip_stones'].items())
        result = {k: v['text'].replace('#', '').replace('They say that ', '') for k, v in gossipStoneJson.items()}
        result = {k: v[0].upper() + v[1:] for k, v in result.items()}
        return result

    def getButtonLayout(self) -> list[ButtonLayout]:
        return [
            ButtonLayout('All', 40)
        ]

    def getWidthGapBetweenButtons(self) -> int:
        return 8

    def getHeightGapBetweenButtons(self) -> int:
        return 8

    def getMaxButtonsPerRow(self) -> int:
        return 10

    def getButtonWidth(self) -> int:
        return 75

    def getButtonHeight(self) -> int:
        return 75

    def isRowBasedLayout(self) -> bool:
        return True

    def isUsingSectionHeaders(self) -> bool:
        return False

    def isUsingTooltips(self) -> bool:
        return False