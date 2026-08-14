import random
import time

# Player stats and setup
class Hero:
    def __init__(self, name, class_choice):
        self.name = name
        self.inventory = ["Health Potion", "Mana Elixir"]
        
        if class_choice == "1":
            self.role = "Archmage"
            self.hp = 70
            self.max_hp = 70
            self.mp = 150
            self.max_mp = 150
            self.attack = 12
            self.spells = {"Fireball": {"cost": 30, "damage": 45}, "Ice Nova": {"cost": 20, "damage": 30}}
        elif class_choice == "2":
            self.role = "Paladin"
            self.hp = 130
            self.max_hp = 130
            self.mp = 60
            self.max_mp = 60
            self.attack = 22
            self.spells = {"Holy Light": {"cost": 25, "heal": 40}, "Smite": {"cost": 20, "damage": 35}}
        else:
            self.role = "Shadow Rogue"
            self.hp = 90
            self.max_hp = 90
            self.mp = 80
            self.max_mp = 80
            self.attack = 28
            self.spells = {"Shadow Strike": {"cost": 25, "damage": 50}}

def display_hero_stats(hero):
    print("\n" + "=" * 45)
    print(f" 🧙 HERO: {hero.name} the {hero.role}")
    print(f" ❤️  Health (HP): {hero.hp}/{hero.max_hp}")
    print(f" 🧪 Mana (MP):   {hero.mp}/{hero.max_mp}")
    print(f" 🎒 Bag:        {', '.join(hero.inevntory)}")
    print("=" * 45 + "\n")

def battle_system(hero, monster_name, monster_hp, monster_atk):
    print(f"\n⚔️ A wild [{monster_name}] emerges from the shadow!")
    time.sleep(1)

    while monster_hp > 0 and hero.hp > 0:
        print(f"\n--- ENCOUNTER: {monster_name} (HP: {monster_hp}) ---")
        print(f"Your HP: {hero.hp}/{hero.max_hp} | Mana: {hero.mp}/{hero.max_mp}")
        print("1. Weapon Strike (Melee Attack)")
        print("2. Cast Spells")
        print("3. Drink Potion")

        choice = input("Select combat action (1-3): ").strip()

        if choice == "1":
            dmg = random.randint(hero.attack - 4, hero.attack + 6)
            monster_hp -= dmg
            print(f"🗡️ You strike {monster_name} with your weapon for {dmg} damage!")
       
        elif choice == "2":
            print("\nAvailable Spells:")
            spell_list = list(hero.spells.keys())
            for idx, spell in enumerate(spell_list, start=1):
                cost = hero.spells[spell]["cost"]
                print(f"  [{idx}] {spell} (Costs {cost} MP)")
           
            spell_choice = input("Choose a spell: ").strip()
            try:
                selected_spell = spell_list[int(spell_choice) - 1]
                spell_info = hero.spells[selected_spell]

                if hero.mp >= spell_info["cost"]:
                    hero.mp -= spell_info["cost"]
                    if "damage" in spell_info:
                        dmg = random.randint(spell_info["damage"] - 5, spell_info["damage"] + 10)
                        monster_hp -= dmg
                        print(f"✨ You cast {selected_spell}! Sparks fly as it deals {dmg} damage!")
                    elif "heal" in spell_info:
                        heal_amount = spell_info["heal"]
                        hero.hp = min(hero.max_hp, hero.hp + heal_amount)
                        print(f"🌟 Radiant light bathes you, restoring {heal_amount} HP!")
                else:
                    print("⚠️ Not enough Mana! Your spell fizzles out!")
            except (IndexError, ValueError):
                print("❌ Invalid spell selection! Turn wasted.")
        
        elif choice == "3":
            print(f"Inventory: {hero.inventory}")
            use_item = input("Type 'health' for Health Potion or 'mana' for Mana Elixir: ").lower().strip()

            if use_item == "health" and "Health Potion" in hero.inventory:
                hero.inventory.remove("Health Potion")
                hero.hp = min(hero.max_hp, hero.hp + 50)
                print(f"🧪 You drink a Health Potion. HP restored to {hero.hp}!")
            elif use_item == "mana" and "Mana Elixir" in hero.inventory:
                hero.inventory.remove("Mana Elixir")
                hero.mp = min(hero.max_mp, hero.mp + 60)
                print(f"🧪 You drink a Mana Elixir. MP restored to {hero.mp}!")
            else:
                print("⚠️ Item not available in your bag!")
        else:
            print("❌ Invalid action!")

        # Enemy counter-attack
        if monster_hp > 0:
            m_dmg = random.randint(monster_atk = 3, monster_atk + 5)
            hero.hp -= m_dmg
            print(f"👹 {monster_name} attacks back dealing {m_dmg} damage!")
            time.sleep(1)

    if hero.hp > 0:
        print(f"\n🎉 VICTORY! You vanquished {monster_name}!")
        if random.random() > 0.3:
            loot = random.choice(["Health Potion", "Mana Elixir"])
            hero.inventory.append(loot)
            print(f"🎁 Found Loot: You picked up 1x {loot}!")
        return True
    else:
        print("\n💀 YOU HAVE FALLEN! Your quest ends here...")
        return False

def start_game():
    print("=" * 50)
    print("   🔮 FANTASY QUEST: REALM OF ARCANA 🔮")
    print("=" * 50)

    name = input("Enter your hero's name: ").strip() or Eldrin"
    print("\nSelect Your Archetype:")
    print("1. Archmage        (High Spell Damage, High Mana, Low HP)")
    print("2. Paladin         (High HP, Defensive, Holy Magic)")
    print("3. Shadow Rogue    (High Melee Attack, Swift)")

    class_choice = input("Choice (1-3): ").strip()
    hero = Hero(name, class_choice)

    print(f"\nWelcome to Arcane, {hero.name}. You venture into the Whispering Dungeon...")
    time.sleep(1.5)

    dungeon = [
        {"location": "Forgotten Crypt", "monster": "Cave Goblin", "hp": 45, "atk": 10},
        {"location": "Sunken Temple", "monster": "Shadow Specter", "hp": 80, "atk": 16},
        {"location": "Dragon's Sanctum", "monster": "Ancient Red Dragon", "hp": 150, "atk": 24}
    ]

    for step, zone in enumerate(dungeon, start=1):
        display_hero_stats(hero)
        print(f"--- FLOOR {step}: {zone['location']} ---")
        print("1. Press onward")
        print("2. Search surroundings for ancient chest")

        act = input("Action (1-2): ").strip()
        if act == "2":
            if random.random() > 0.4:
                loot = random.choice(["Health Potion", "Mana Elixir"])
                hero.inventory.append(loot)
                print(f"🔍 You opened an ancient chest and discovered a {loot}!")
            else:
                print("🔍 You searched the room, but only dust and rocks.")
        
        victory = battle_system(hero, zone["monster"], zone["hp"], zone["atk"])
        if not victory:
            break
        
        print(f"\n✨ Floor {step} cleared!")
        time.sleep(1.5)
 
    if hero.hp > 0:
        print("\n" + "=" * 50)
        print(" 🏆 REALM SAVED! You defeated the Ancient Dragon and restored peace!")
        print("=" * 50)

if __name__ == "__main__":
    start_game()   
