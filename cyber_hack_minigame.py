import random
import time

# List of target server nodes
target_nodes = ["FIREWALL_ALPHA", "MAIN_DATABASE", "SECURITY_CORE"]

print("--- CYBER SECURITY SYSTEM: TERMINAL HACK ---\n")
print(f"Targeting Node: {random.choice(target_nodes)}")
print("Decrypting access key... Please wait. \n")

# Simulate a quick terminal delay
time.sleep(1)

#Generate a random 4-digit secret passcode
secret_code = str(random.randint(1000, 9999))
attempts = 15

while attempts > 0:
    guess = input(f"Enter 4-digit bypass code ({attempts} attempts remaining): ")

    if guess == secret_code:
        print("\n[SUCCESS] ACCESS GRANTED! System bypassed.")
        break
    else:
        attempts -= 1
        # Give a small hint comparing the player's guess to the actual code
        if attempts > 0:
            if int(guess) < int(secret_code):
                print("[WARNING] Access Denied: Code is TOO LOW.\n")
            else:
                print("[WARNING] Access Denied: Code is TOO HIGH.\n")

if attempts == 0:
    print(f"\n[SYSTEM LOCKDOWN] Out of attempts! Correct key was: {secret_code}")
print("\n--- Session Closed ---")
