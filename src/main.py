#!/usr/bin/env python3
"""
AI RPG Chat Game - Main Entry Point

A simple text-based RPG where you explore a world and chat with AI characters.
"""
import asyncio
import sys
from typing import List, Optional

from world import World
from character import CharacterManager
from ai_service import AIService

try:
    import config
except ImportError:
    print("🚨 Configuration Error!")
    print("Please copy config.example.py to config.py and set your API key.")
    print("\nExample:")
    print("  cp config.example.py config.py")
    print("  # Then edit config.py with your API key")
    sys.exit(1)


class Game:
    """Main game class that handles the game loop and commands"""
    
    def __init__(self):
        self.world = World()
        self.character_manager = CharacterManager()
        self.ai_service = AIService()
        self.running = True
        self.player_name = "Adventurer"
    
    def display_welcome(self):
        """Display the welcome message and game introduction"""
        print("=" * 60)
        print(f"🌟 欢迎来到 {config.GAME_TITLE}! 🌟")
        print("=" * 60)
        print()
        print("您是一位刚刚来到神秘境界的冒险者。")
        print("探索这个世界，与AI驱动的角色聊天吧！")
        print()
        print("💡 输入 'help' 或 '帮助' 查看可用命令。")
        print("💡 输入 'quit' 或 '退出' 退出游戏。")
        print()
        print("-" * 60)
        print()
    
    def display_help(self):
        """Display available commands"""
        print("📚 可用命令:")
        print("  look / 看             - 查看当前位置")
        print("  go <方向> / 走 <方向>   - 移动 (north/south/east/west 或 北/南/东/西)")
        print("  talk <角色> / 说 <角色> - 与AI角色聊天")
        print("  characters / 角色     - 列出当前位置的角色")
        print("  where / 位置          - 显示当前位置")
        print("  help / 帮助           - 显示此帮助信息")
        print("  quit / 退出           - 退出游戏")
        print()
        print("💡 示例:")
        print("  看                   - 查看周围")
        print("  北 或 go north       - 向北移动")
        print("  说 elder 你好        - 与长老打招呼")
        print()
    
    def look_around(self):
        """Display the current location description and characters"""
        location_desc = self.world.get_location_description()
        print(location_desc)
        
        # Show characters in this location
        characters = self.character_manager.get_characters_in_location(self.world.current_location)
        if characters:
            print()
            for char_id, character in characters.items():
                print(f"👤 {character.get_description()}")
        print()
    
    def list_characters(self):
        """List characters in the current location"""
        characters = self.character_manager.get_characters_in_location(self.world.current_location)
        if characters:
            print("这里的角色:")
            for char_id, character in characters.items():
                print(f"  • {character.name} (可用: talk {char_id} 或 说 {char_id})")
        else:
            print("这里没有其他人。")
        print()
    
    async def talk_to_character(self, char_id: str, message: str):
        """Handle conversation with a character"""
        character = self.character_manager.get_character(char_id)
        
        if not character:
            print(f"这里没有叫 '{char_id}' 的人。")
            return
        
        # Check if character is in current location
        if character.location != self.world.current_location:
            print(f"{character.name} 不在这里。")
            return
        
        print(f"💬 您对 {character.name} 说: \"{message}\"")
        print()
        print("🤔 ({character.name} 正在思考...)")
        
        try:
            # Get context for the AI
            location = self.world.get_current_location()
            context = f"当前在 {location.name}。{location.description}"
            
            # Add conversation history context
            conv_context = character.get_conversation_context()
            if conv_context:
                context += f"\n\n{conv_context}"
            
            # Get AI response
            response = await self.ai_service.get_character_response(
                character.name,
                character.personality,
                message,
                context
            )
            
            print(f"💭 {character.name}: \"{response}\"")
            
            # Add to conversation history
            character.add_conversation(message, response)
            
        except Exception as e:
            if config.DEBUG_MODE:
                print(f"获取AI回复时出错: {e}")
            print(f"💭 {character.name}: \"我现在好像有点想不起来要说什么...\"")
        
        print()
    
    def move_player(self, direction: str):
        """Move the player in a direction"""
        # 中文方向映射
        direction_names = {
            "north": "北方", "south": "南方", 
            "east": "东方", "west": "西方"
        }
        
        success, message = self.world.move_to(direction)
        
        if success:
            dir_name = direction_names.get(direction, direction)
            print(f"您向{dir_name}走去。")
        else:
            print(message)
        
        if success:
            print()
            self.look_around()
        else:
            print()
    
    def parse_command(self, command: str) -> tuple[str, List[str]]:
        """Parse a command into action and arguments"""
        parts = command.strip().lower().split()
        if not parts:
            return "", []
        
        action = parts[0]
        args = parts[1:]
        return action, args
    
    async def handle_command(self, command: str):
        """Handle a player command"""
        action, args = self.parse_command(command)
        
        # 退出命令 (中英文)
        if action in ["quit", "q", "退出", "再见"]:
            self.running = False
            print("👋 感谢游玩！再见！")
            
        # 帮助命令 (中英文)
        elif action in ["help", "h", "帮助", "命令"]:
            self.display_help()
            
        # 查看命令 (中英文)
        elif action in ["look", "l", "看", "查看", "观察"]:
            self.look_around()
            
        # 位置命令 (中英文)
        elif action in ["where", "位置", "我在哪"]:
            location = self.world.get_current_location()
            print(f"📍 您当前在: {location.name}")
            print()
            
        # 角色命令 (中英文)
        elif action in ["characters", "chars", "角色", "人物", "npc"]:
            self.list_characters()
            
        # 移动命令 (中英文)
        elif action in ["go", "move", "走", "去", "移动"]:
            if args:
                # 支持中文方向
                direction_map = {
                    "北": "north", "南": "south", "东": "east", "西": "west",
                    "上": "north", "下": "south", "左": "west", "右": "east"
                }
                direction = direction_map.get(args[0], args[0])
                self.move_player(direction)
            else:
                print("去哪里？(north/south/east/west 或 北/南/东/西)")
                print()
        
        # 直接方向命令 (中英文)
        elif action in ["north", "n", "south", "s", "east", "e", "west", "w", 
                       "北", "南", "东", "西", "上", "下", "左", "右"]:
            direction_map = {
                "n": "north", "s": "south", "e": "east", "w": "west",
                "北": "north", "南": "south", "东": "east", "西": "west",
                "上": "north", "下": "south", "左": "west", "右": "east"
            }
            direction = direction_map.get(action, action)
            self.move_player(direction)
            
        # 对话命令 (中英文)
        elif action in ["talk", "说", "聊", "对话", "交谈"]:
            if len(args) >= 1:
                char_id = args[0]
                message = " ".join(args[1:]) if len(args) > 1 else "你好"
                await self.talk_to_character(char_id, message)
            else:
                print("和谁说话？使用: talk <角色ID> <消息>")
                print("或者: 说 <角色ID> <消息>")
                print()
                
        # 简单说话命令 (中英文)
        elif action in ["say", "讲"]:
            # 尝试在消息中找到角色名
            characters = self.character_manager.get_characters_in_location(self.world.current_location)
            if characters:
                # 如果有多个角色，使用第一个
                char_id = list(characters.keys())[0]
                message = " ".join(args)
                await self.talk_to_character(char_id, message)
            else:
                print("这里没有人可以交谈。")
                print()
                
        else:
            print(f"未知命令: {action}")
            print("输入 'help' 或 '帮助' 查看可用命令。")
            print()
    
    async def game_loop(self):
        """Main game loop"""
        self.display_welcome()
        self.look_around()
        
        while self.running:
            try:
                command = input("🎮 > ").strip()
                
                if command:
                    await self.handle_command(command)
                    
            except KeyboardInterrupt:
                print("\n\n👋 Thanks for playing! Goodbye!")
                break
            except EOFError:
                print("\n\n👋 Thanks for playing! Goodbye!")
                break
            except Exception as e:
                if config.DEBUG_MODE:
                    print(f"Error: {e}")
                    import traceback
                    traceback.print_exc()
                else:
                    print("Something went wrong. Please try again.")
                print()


async def main():
    """Main function"""
    try:
        game = Game()
        await game.game_loop()
    except Exception as e:
        print(f"Fatal error: {e}")
        if config.DEBUG_MODE:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
