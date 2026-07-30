import random
import time

# Player stats and setup
class Player:
    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.inventory = ["Patch Kit"]
        self.level = 1
        
        if class_type == "1":
            self.role = "Ethical Hacker"
            self.hp = 80
            self.max_hp = 80
            self.bandwidth = 120
            self.attack = 25
        elif class_type == "2":
            self.role = "Network Admin"
            self.hp = 120
            self.max_hp = 120
            self.bandwidth = 80
            self.attack = 15
        else:
            self.role = "Forensic Investigator"
            self.hp = 100
            self.max_hp = 100
            self.bandwidth = 100
            self.attack = 20

def print_status(player):
    print("\n" + "=" * 40)
    print(f" 👤 {player.name} the {player.role}")
    print(f" ❤️  Integrity (HP): {player.hp}/{player.max_hp}")
    print(f" ⚡ Bandwidth: {player.bandwidth}")
    print(f" 🎒 Inventory: {', '.join(player.inventory)}")
    print("=" * 40 + "\n")

def battle(player, enemy_name, enemy_hp, enemy_attack):
    print(f"\n🚨 ALERT! Rogue process encountered: [{enemy_name}]!")
    time.sleep(1)
    
    while enemy_hp > 0 and player.hp > 0:
        print(f"\n--- BATTLE: {enemy_name} (HP: {enemy_hp}) ---")
        print(f"Your HP: {player.hp} | Bandwidth: {player.bandwidth}")
        print("1. Launch Exploits (Basic Attack)")
        print("2. Overclock (Special Attack - Costs 30 Bandwidth)")
        print("3. Deploy Patch Kit (Heal HP)")

        choice = input("Select combat command (1-3): ").strip()

        if choice == "1":
            damage = random.randint(player.attack - 5, player.attack + 5)
            enemy_hp -= damage
            print(f"💥 You executed a script causing {damage} damage to {enemy_name}!")
        elif choice == "2":
            if player.bandwidth >= 30:
                player.bandwidth -= 30
                damage = random.randint(player.attack + 15, player.attack + 25)
                enemy_hp -= damage
                print(f"⚡ OVERCLOCK SUCCESSFUL! Dealt {damage} massive damage!")
            else:
                print("⚠️ Insufficient Bandwidth! Turn wasted!")
        elif choice == "3":
            if "Patch Kit" in player.inventory:
                player.inventory.remove("Patch Kit")
                player.hp = min(player.max_hp, player.hp + 40)
                print(f"🩹 Applied Patch Kit! Restored integrity to {player.hp} HP.")
            else:
                print("⚠️ No Patch Kits left in inventory!")
        else:
            print("❌ Invalid command! Turn missed.")
       
        # Enemy attack phase
        if enemy_hp > 0:
            e_damage = random.randint(enemy_attack - 3, enemy_attack + 5)
            player.hp -= e_damage
            print(f"🤖 {enemy_name} counter-attacked for {e_damage} damage!")
            time.sleep(1)

    if player.hp > 0:
        print(f"\n🎉 SUCCESS! You terminated {enemy_name}!")
        # Random loot drop
        if random.random() > 0.4:
            player.inventory.append("Patch Kit")
            print("🎁 Loot Dropped: Found 1x Patch Kit!")
        return True
    else:
        print("\n💥 SYSTEM CRASH! Your connection was terminated.")
        return False

def main():
    print("=" * 50)
    print("   💻 CYBER RPG: ROGUE SERVER BREACH 💻")
    print("=" * 50)

    name = input("Enter your Handler Alias: ").strip() or "Operator"
    print("\nSelect Your Class:")
    print("1. Ethical Hacker (High Attack, High Bandwidth, Low HP)")
    print("2. Network Admin (High HP, Low Attack, Balanced)")
    print("3. Forensic Investigator (Balanced Stats)")

    class_choice = input("Choice (1-3): ").strip()
    player = Player(name, class_choice)

    print(f"\nWelcome to the grid, {player.name}. Infiltrating mainframe...")
    time.sleep(1.5)

    nodes = [
        {"name": "DMZ Gateway Server", "enemy": "Trojan-Daemon", "hp": 40, "atk": 10},
        {"name": "Internal Database Node", "enemy": "Ransomeware Botnet", "hp": 70, "atk": 18},
        {"name": "Core Mainframe Vault", "enemy": "Rogue AI Core", "hp": 120, "atk": 25}
    ]

    for i, node in enumerate(nodes, start=1):
        print_status(player)
        print(f"---SECTOR {i}: {node['name']} ---")
        print("Options:")
        print("1. Infiltrate Node")
        print("2. Search sector for supplies")

        action = input("Action (1-2): ").strip()
        if action == "2":
            if random.random() > 0.5:
                player.inventory.append("Patch Kit")
                print("🔎 Scanned network memory... Found a hidden Patch Kit!")
            else:
                print("🔎 Scanned network memory... Sector empty!")

        # Run node combat
        success = battle(player, node['enemy'], node['hp'], node['atk'])
        if not success:
            break

        print(f"\n✅ Sector {i} cleared!")
        time.sleep(1.5)

    if player.hp > 0:
        print("\n" + "=" * 50)
        print(" 🏆 MISSION ACCOMPLISHED! Rogue AI purged from mainframe!")
        print("=" * 50)

if __name__ == "__main__":
    main()
