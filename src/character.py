"""
AI Character System
"""
from typing import Dict, Optional


class Character:
    """Represents an AI-powered character in the game"""
    
    def __init__(self, name: str, personality: str, location: str, description: str = ""):
        self.name = name
        self.personality = personality
        self.location = location
        self.description = description
        self.conversation_history = []
    
    def get_description(self) -> str:
        """Get character description for when player looks around"""
        if self.description:
            return f"{self.name} is here. {self.description}"
        return f"{self.name} is here."
    
    def add_conversation(self, player_message: str, character_response: str):
        """Add a conversation to history (for context in future interactions)"""
        self.conversation_history.append({
            "player": player_message,
            "character": character_response
        })
        
        # Keep only last 5 conversations to avoid context overload
        if len(self.conversation_history) > 5:
            self.conversation_history.pop(0)
    
    def get_conversation_context(self) -> str:
        """Get recent conversation context for AI"""
        if not self.conversation_history:
            return ""
        
        context = "Recent conversation history:\n"
        for conv in self.conversation_history[-3:]:  # Last 3 conversations
            context += f"Player: {conv['player']}\n"
            context += f"{self.name}: {conv['character']}\n"
        
        return context


class CharacterManager:
    """Manages all characters in the game"""
    
    def __init__(self):
        self.characters: Dict[str, Character] = {}
        self._create_default_characters()
    
    def _create_default_characters(self):
        """Create the default set of characters"""
        
        # Village Elder - Wise and helpful
        self.add_character(
            "elder",
            "Village Elder",
            "A wise and kind elder who has lived in this village for decades. "
            "He knows many stories and is always willing to help travelers.",
            "village_center",
            "The elder is a friendly, wise person who speaks with warmth and offers guidance. "
            "He has seen many adventurers come and go, and enjoys sharing wisdom and stories."
        )
        
        # Mysterious Merchant - Cryptic and intriguing
        self.add_character(
            "merchant",
            "Mysterious Merchant",
            "A traveling merchant with an air of mystery about them. "
            "They seem to have exotic goods and knowledge from far-off lands.",
            "market_square",
            "The merchant is enigmatic and speaks in riddles sometimes. "
            "They are knowledgeable about rare items and distant places, "
            "but also enjoy being cryptic and mysterious in their responses."
        )
        
        # Forest Guardian - Nature-loving and protective
        self.add_character(
            "guardian",
            "Forest Guardian",
            "An ancient being who protects the forest and its creatures. "
            "They have a deep connection with nature.",
            "enchanted_forest",
            "The guardian is deeply connected to nature and speaks with reverence for all living things. "
            "They are protective of the forest but kind to those who respect nature. "
            "They often speak in metaphors related to plants, animals, and natural cycles."
        )
        
        # Curious Scholar - Intellectual and inquisitive
        self.add_character(
            "scholar",
            "Curious Scholar",
            "A young scholar who is always eager to learn new things. "
            "They carry books and seem fascinated by knowledge of all kinds.",
            "ancient_library",
            "The scholar is enthusiastic about learning and discovery. "
            "They ask lots of questions, share interesting facts, and get excited about new knowledge. "
            "They are friendly but can get carried away talking about their studies."
        )
    
    def add_character(self, char_id: str, name: str, description: str, location: str, personality: str):
        """Add a new character to the game"""
        character = Character(name, personality, location, description)
        self.characters[char_id] = character
    
    def get_character(self, char_id: str) -> Optional[Character]:
        """Get a character by ID"""
        return self.characters.get(char_id)
    
    def get_characters_in_location(self, location: str) -> Dict[str, Character]:
        """Get all characters in a specific location"""
        return {
            char_id: character 
            for char_id, character in self.characters.items() 
            if character.location == location
        }
    
    def list_all_characters(self) -> Dict[str, Character]:
        """Get all characters"""
        return self.characters.copy()
