import random
import time

# List of game scenarios: (Email Subject, Sender, Link, Is_Phishing, Hint)
emails = [
    (
        "Urgent: Reset your IT password now!",
        "admin@company-security-update.com",
        "http://login.company-security-update.com/reset",
        True,
        "Look closely at the domain name! 'company-security-update.com' is not your official company domain."
    ),
    (
        "Weekly Team Meeting Agenda",
        "sarah.jerkins@yourcompany.com",
        "https://docs.yourcompany.com/meeting-notes",
        False,
        "The sender domain matches your company perfectly and uses a secure HTTPSnlink."
    ),
    (
        "YOU WON A $500 GIFT CARD!",
        "rewards@free-money-now.net",
        "http://bit.ly/claim-your-prize-now",
        True,
        "Suspicious sender domain, overly hyped title, and a shortened suspicious URL."
    ),
    (
        "Payroll Direct Deposit Confirmation",
        "hr-portal@yourcompany.com",
        "https://hr.yourcompany.com/paystub",
        False,
        "Official internal HR sender address with a secure internal portal URL."
    ),
    (
        "Critical Security Alert: Suspicious Login Detected",
        "support@micros0ft-security.com",
        "https://micros0ft-security.com/verify",
        True,
        "Classic typo-squatting! Notice the number '0' instead of the letter 'o' in Microsoft."
    )
]

score = 0
lives = 3

print("=" * 50)
print(" 🛡️ CYBER DEFENSE: PHISHING INSPECTOR 🛡️ ")
print("=" * 50)
print("Analyze each email. Decide if it's SAFE or a PHISHING SCAM.\n")

# Shuffle emails so each playthrough feels different
random.shuffle(emails)

for subject, sender, link, is_phishing, hint in emails:
    if lives <= 0:
        print("🚨 CRITICAL BREACH! Too many security errors. Game Over! 🚨")
        break

    print("_" * 50)
    print(f"📧 SUBJECT : {subject}")
    print(f"👤 FROM    : {sender}")
    print(f"🔗 LINK    : {link}")
    print("-" * 50)

    choice = input("Action? Type [1] for SAFE or [2] for PHISHING SCAM: ").strip()

    # Determine player decision (1 = Safe / False phishing, 2 = Scam / True phishing)
    user_guessed_phishing = (choice == "2")

    if (choice == "1" and not is_phishing) or (choice == "2" and is_phishing):
        print("\n✅ CORRECT ANALYSIS! Threat successfully handled.")
        score += 100
    else:
        lives -= 1
        print(f"\n❌ INCORRECT! Lives remaining: {'❤️ ' * lives}")
        print(f"💡 Security Tip: {hint}")

    time.sleep(1.5)

print("\n" + "=" * 50)
print(f" 🏆 GAME OVER! Final Score: {score} PTS")
print("=" * 50)
