"""
World and Location Management
"""
from typing import Dict, List, Optional


class Location:
    """Represents a location in the game world"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.exits: Dict[str, str] = {}  # direction -> location_id
        self.items: List[str] = []  # Simple items that can be found here
    
    def add_exit(self, direction: str, location_id: str):
        """Add an exit to another location"""
        self.exits[direction] = location_id
    
    def get_exit(self, direction: str) -> Optional[str]:
        """Get the location ID for a direction"""
        return self.exits.get(direction.lower())
    
    def get_exits_description(self) -> str:
        """Get a description of available exits"""
        if not self.exits:
            return "没有明显的出口。"
        
        # 转换方向为中文
        direction_names = {
            "north": "北方", "south": "南方", 
            "east": "东方", "west": "西方"
        }
        
        exits = [direction_names.get(direction, direction) for direction in self.exits.keys()]
        
        if len(exits) == 1:
            return f"有一个出口通向{exits[0]}。"
        elif len(exits) == 2:
            return f"有出口通向{exits[0]}和{exits[1]}。"
        else:
            return f"有出口通向{', '.join(exits[:-1])}和{exits[-1]}。"


class World:
    """Manages the game world and locations"""
    
    def __init__(self):
        self.locations: Dict[str, Location] = {}
        self.current_location = "village_center"
        self._create_world()
    
    def _create_world(self):
        """Create the game world with locations and connections"""
        
        # Village Center - Starting location
        village_center = Location(
            "Village Center",
            "You are in the heart of a peaceful village. A stone fountain sits in the center, "
            "surrounded by cobblestone paths. Cozy houses with thatched roofs line the square, "
            "and you can hear the gentle chatter of villagers going about their daily lives."
        )
        village_center.add_exit("north", "ancient_library")
        village_center.add_exit("east", "market_square")
        village_center.add_exit("south", "enchanted_forest")
        village_center.add_exit("west", "crystal_cave")
        self.locations["village_center"] = village_center
        
        # Ancient Library - Place of knowledge
        library = Location(
            "Ancient Library",
            "You stand in a grand library with towering shelves that reach up to vaulted ceilings. "
            "Thousands of books, scrolls, and manuscripts are carefully organized here. "
            "Dust motes dance in shafts of sunlight streaming through tall windows. "
            "The air smells of old parchment and leather bindings."
        )
        library.add_exit("south", "village_center")
        library.add_exit("east", "wizard_tower")
        self.locations["ancient_library"] = library
        
        # Market Square - Place of commerce
        market = Location(
            "Market Square",
            "A bustling marketplace filled with colorful stalls and the sounds of commerce. "
            "Merchants display their wares on wooden tables covered with bright cloth. "
            "The aroma of fresh bread, exotic spices, and roasted nuts fills the air. "
            "People from near and far come here to trade and socialize."
        )
        market.add_exit("west", "village_center")
        market.add_exit("north", "wizard_tower")
        market.add_exit("south", "riverside_dock")
        self.locations["market_square"] = market
        
        # Enchanted Forest - Mystical nature area
        forest = Location(
            "Enchanted Forest",
            "You enter a magical forest where ancient trees tower overhead, their branches "
            "intertwining to form a natural cathedral. Soft, ethereal light filters through "
            "the canopy, and you can hear the gentle whisper of leaves and distant bird songs. "
            "There's a sense of old magic in the air here."
        )
        forest.add_exit("north", "village_center")
        forest.add_exit("east", "riverside_dock")
        forest.add_exit("west", "moonlit_grove")
        self.locations["enchanted_forest"] = forest
        
        # Crystal Cave - Mysterious underground
        cave = Location(
            "Crystal Cave",
            "You are inside a stunning crystal cave where the walls sparkle with embedded gems. "
            "Soft, multicolored light emanates from the crystals, creating a dreamlike atmosphere. "
            "The cave is surprisingly warm, and there's a gentle humming sound that seems to "
            "come from the crystals themselves."
        )
        cave.add_exit("east", "village_center")
        cave.add_exit("south", "moonlit_grove")
        self.locations["crystal_cave"] = cave
        
        # Wizard Tower - Place of arcane study
        tower = Location(
            "Wizard Tower",
            "You stand at the base of a tall, spiraling tower made of dark stone. "
            "Strange symbols are carved into the walls, and an aura of magic surrounds the place. "
            "Through windows high above, you can see the flicker of candlelight and "
            "occasionally, colorful magical sparks."
        )
        tower.add_exit("west", "ancient_library")
        tower.add_exit("south", "market_square")
        self.locations["wizard_tower"] = tower
        
        # Riverside Dock - Peaceful water area
        dock = Location(
            "Riverside Dock",
            "A peaceful wooden dock extends into a clear, flowing river. "
            "Small boats are moored here, gently bobbing in the current. "
            "You can hear the soothing sound of water lapping against the dock, "
            "and fish occasionally jump, creating ripples in the water."
        )
        dock.add_exit("north", "market_square")
        dock.add_exit("west", "enchanted_forest")
        self.locations["riverside_dock"] = dock
        
        # Moonlit Grove - Mystical clearing
        grove = Location(
            "Moonlit Grove",
            "A circular clearing in the forest where moonlight seems to shine even during the day. "
            "Ancient standing stones are arranged in a circle, covered with glowing runes. "
            "The grass here is unusually soft and green, and there's a sense of timeless peace. "
            "This feels like a place where magic and nature are one."
        )
        grove.add_exit("north", "crystal_cave")
        grove.add_exit("east", "enchanted_forest")
        self.locations["moonlit_grove"] = grove
    
    def get_location(self, location_id: str) -> Optional[Location]:
        """Get a location by ID"""
        return self.locations.get(location_id)
    
    def get_current_location(self) -> Location:
        """Get the current location"""
        return self.locations[self.current_location]
    
    def move_to(self, direction: str) -> tuple[bool, str]:
        """
        Try to move in a direction
        Returns (success, message)
        """
        current_loc = self.get_current_location()
        destination_id = current_loc.get_exit(direction)
        
        if destination_id:
            if destination_id in self.locations:
                self.current_location = destination_id
                return True, f"您向{direction}方向走去。"
            else:
                return False, "那条路似乎被堵住了。"
        else:
            direction_names = {
                "north": "北方", "south": "南方", 
                "east": "东方", "west": "西方"
            }
            dir_name = direction_names.get(direction, direction)
            return False, f"您无法从这里向{dir_name}走。"
    
    def get_location_description(self, include_exits: bool = True) -> str:
        """Get the full description of the current location"""
        location = self.get_current_location()
        description = f"{location.name}\n\n{location.description}"
        
        if include_exits:
            description += f"\n\n{location.get_exits_description()}"
        
        return description
