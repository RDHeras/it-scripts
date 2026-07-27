import random
import time

# Setup common game network ports
ports = {
    22: "SSH (Remote Access)",
    80: "HTTP (Web Traffic)",
    443: "HTTPS (Secure Web)",
    3306: "MySQL (Database)"
}

score = 0
rounds = 5

print("=== CYBER DEFENDER: PORT SCANNER GAME ===")
print("Target: Find the infected port and close it fast!\n")

for round_num in range(1, rounds + 1):
    # Pick a random port that is "infected"
    infected_port = random.choice(list(ports.keys()))

    print(f"--- ROUND {round_num} of {rounds} ---")
    print("[ALERT] Malware detected on one of your server ports!")

    start_time = time.time()
    try:
        player_choice = int(input("Enter port number to scan and close (22, 80, 443, 3306): "))
    except ValueError:
        print("[ERROR] Invalid port entry! Turn wasted.\n")
        continue
    
    end_time = time.time()
    reaction_time = round(end_time - start_time, 2)

    if player_choice == infected_port:
        print(f"[SUCCESS] Blocked malware on Port {infected_port} ({ports[infected_port]})!")
        print(f"Response Time: {reaction_time} seconds.\n")
        score += 1
    else:
        print(f"[FAILED] Wrong port! The threat was actually on Port {infected_port}.\n")

print("=== GAME OVER ===")
print(f"Final Score: {score} / {rounds} threats blocked!")
