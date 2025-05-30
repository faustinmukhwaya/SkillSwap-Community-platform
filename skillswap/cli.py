import json
import os
from prompt_toolkit import prompt
from skillswap.models import User, Skill, Exchange
from skillswap.utils import validate_non_empty_string, validate_email, find_by_attribute

DATA_FILE = "skillswap_data.json"

users = []
skills = []
exchanges = []

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"profiles": [], "proposals": []}
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {"profiles": [], "proposals": []}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def main_menu():
    while True:
        print("\nSkillSwap Community Platform")
        print("1. Manage Users")
        print("2. Manage Skills")
        print("3. Manage Exchanges")
        print("4. Exit")
        choice = prompt("Choose an option: ")

        if choice == "1":
            manage_users()
        elif choice == "2":
            manage_skills()
        elif choice == "3":
            manage_exchanges()
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users():
    while True:
        print("\nManage Users")
        print("1. Create User")
        print("2. Delete User")
        print("3. Display All Users")
        print("4. Find User by Attribute")
        print("5. Back to Main Menu")
        choice = prompt("Choose an option: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            display_all_users()
        elif choice == "4":
            find_user_by_attribute()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_user():
    try:
        name = prompt("Enter name: ")
        validate_non_empty_string(name, "Name")
        email = prompt("Enter email: ")
        validate_email(email)
        user = User(name, email)
        users.append(user)
        print(f"User created with ID: {user.id}")
    except ValueError as e:
        print(e)

def delete_user():
    try:
        user_id = prompt("Enter User ID to delete: ")
        user = find_by_attribute(users, "id", user_id)
        if user:
            users.remove(user)
            print(f"User with ID {user_id} deleted.")
        else:
            print("User not found.")
    except ValueError as e:
        print(e)

def display_all_users():
    if not users:
        print("No users available.")
    else:
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

def find_user_by_attribute():
    try:
        attribute = prompt("Enter attribute to search by (id, name, email): ")
        value = prompt(f"Enter value for {attribute}: ")
        user = find_by_attribute(users, attribute, value)
        if user:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
        else:
            print("User not found.")
    except ValueError as e:
        print(e)

def manage_skills():
    while True:
        print("\nManage Skills")
        print("1. Create Skill")
        print("2. Delete Skill")
        print("3. Display All Skills")
        print("4. Find Skill by Attribute")
        print("5. Back to Main Menu")
        choice = prompt("Choose an option: ")

        if choice == "1":
            create_skill()
        elif choice == "2":
            delete_skill()
        elif choice == "3":
            display_all_skills()
        elif choice == "4":
            find_skill_by_attribute()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_skill():
    try:
        name = prompt("Enter skill name: ")
        validate_non_empty_string(name, "Skill name")
        user_id = prompt("Enter User ID offering the skill: ")
        user = find_by_attribute(users, "id", user_id)
        if user:
            skill = Skill(name, user_id)
            skills.append(skill)
            user.skills.append(skill.id)
            print(f"Skill created with ID: {skill.id}")
        else:
            print("User not found.")
    except ValueError as e:
        print(e)

def delete_skill():
    try:
        skill_id = prompt("Enter Skill ID to delete: ")
        skill = find_by_attribute(skills, "id", skill_id)
        if skill:
            skills.remove(skill)
            print(f"Skill with ID {skill_id} deleted.")
        else:
            print("Skill not found.")
    except ValueError as e:
        print(e)

def display_all_skills():
    if not skills:
        print("No skills available.")
    else:
        for skill in skills:
            print(f"ID: {skill.id}, Name: {skill.name}, User ID: {skill.user_id}, Offered: {skill.is_offered}")

def find_skill_by_attribute():
    try:
        attribute = prompt("Enter attribute to search by (id, name, user_id): ")
        value = prompt(f"Enter value for {attribute}: ")
        skill = find_by_attribute(skills, attribute, value)
        if skill:
            print(f"ID: {skill.id}, Name: {skill.name}, User ID: {skill.user_id}, Offered: {skill.is_offered}")
        else:
            print("Skill not found.")
    except ValueError as e:
        print(e)

def manage_exchanges():
    while True:
        print("\nManage Exchanges")
        print("1. Create Exchange")
        print("2. Delete Exchange")
        print("3. Display All Exchanges")
        print("4. Find Exchange by Attribute")
        print("5. Back to Main Menu")
        choice = prompt("Choose an option: ")

        if choice == "1":
            create_exchange()
        elif choice == "2":
            delete_exchange()
        elif choice == "3":
            display_all_exchanges()
        elif choice == "4":
            find_exchange_by_attribute()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def create_exchange():
    try:
        offerer_id = prompt("Enter Offerer ID: ")
        receiver_id = prompt("Enter Receiver ID: ")
        offered_skill_id = prompt("Enter Offered Skill ID: ")
        requested_skill_id = prompt("Enter Requested Skill ID: ")

        offerer = find_by_attribute(users, "id", offerer_id)
        receiver = find_by_attribute(users, "id", receiver_id)
        offered_skill = find_by_attribute(skills, "id", offered_skill_id)
        requested_skill = find_by_attribute(skills, "id", requested_skill_id)

        if offerer and receiver and offered_skill and requested_skill:
            exchange = Exchange(offerer_id, receiver_id, offered_skill_id, requested_skill_id)
            exchanges.append(exchange)
            offerer.exchanges.append(exchange.id)
            receiver.exchanges.append(exchange.id)
            print(f"Exchange created with ID: {exchange.id}")
        else:
            print("Invalid IDs provided.")
    except ValueError as e:
        print(e)

def delete_exchange():
    try:
        exchange_id = prompt("Enter Exchange ID to delete: ")
        exchange = find_by_attribute(exchanges, "id", exchange_id)
        if exchange:
            exchanges.remove(exchange)
            print(f"Exchange with ID {exchange_id} deleted.")
        else:
            print("Exchange not found.")
    except ValueError as e:
        print(e)

def display_all_exchanges():
    if not exchanges:
        print("No exchanges available.")
    else:
        for exchange in exchanges:
            print(f"ID: {exchange.id}, Offerer ID: {exchange.offerer_id}, Receiver ID: {exchange.receiver_id}, Offered Skill ID: {exchange.offered_skill_id}, Requested Skill ID: {exchange.requested_skill_id}, Created At: {exchange.created_at}")

def find_exchange_by_attribute():
    try:
        attribute = prompt("Enter attribute to search by (id, offerer_id, receiver_id): ")
        value = prompt(f"Enter value for {attribute}: ")
        exchange = find_by_attribute(exchanges, attribute, value)
        if exchange:
            print(f"ID: {exchange.id}, Offerer ID: {exchange.offerer_id}, Receiver ID: {exchange.receiver_id}, Offered Skill ID: {exchange.offered_skill_id}, Requested Skill ID: {exchange.requested_skill_id}, Created At: {exchange.created_at}")
        else:
            print("Exchange not found.")
    except ValueError as e:
        print(e)

def create_profile(data):
    name = input("Enter your name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return

    if any(profile["name"].lower() == name.lower() for profile in data["profiles"]):
        print("Error: A profile with this name already exists.")
        return

    teach_skills = input("Enter skills you can teach (comma-separated): ").strip()
    learn_skills = input("Enter skills you want to learn (comma-separated): ").strip()

    if not teach_skills or not learn_skills:
        print("Error: Skill lists cannot be empty.")
        return

    profile = {
        "name": name,
        "teach_skills": [skill.strip() for skill in teach_skills.split(",")],
        "learn_skills": [skill.strip() for skill in learn_skills.split(",")]
    }
    data["profiles"].append(profile)
    save_data(data)
    print(f"Profile created for {name}.")

def browse_skills(data):
    if not data["profiles"]:
        print("No skills available.")
        return

    skill_map = {}
    for profile in data["profiles"]:
        for skill in profile["teach_skills"]:
            if skill not in skill_map:
                skill_map[skill] = []
            skill_map[skill].append(profile["name"])

    print("Available Skills:")
    for skill, users in skill_map.items():
        print(f"{skill}: {', '.join(users)}")

def propose_exchange(data):
    proposer_name = input("Enter your name: ").strip()
    proposer = next((profile for profile in data["profiles"] if profile["name"].lower() == proposer_name.lower()), None)

    if not proposer:
        print("Error: Profile not found.")
        return

    print("Available profiles:")
    for idx, profile in enumerate(data["profiles"]):
        if profile["name"].lower() != proposer_name.lower():
            print(f"{idx}: {profile['name']}")

    try:
        target_index = int(input("Select a profile by index: ").strip())
        target = data["profiles"][target_index]
    except (ValueError, IndexError):
        print("Error: Invalid index.")
        return

    if target["name"].lower() == proposer_name.lower():
        print("Error: You cannot propose an exchange with yourself.")
        return

    teach_skill = input("Enter a skill you will teach: ").strip()
    if teach_skill not in proposer["teach_skills"]:
        print("Error: You do not have this skill to teach.")
        return

    learn_skill = input("Enter a skill you want to learn: ").strip()
    if learn_skill not in target["teach_skills"]:
        print("Error: The target does not have this skill to teach.")
        return

    proposal = {
        "proposer": proposer_name,
        "target": target["name"],
        "teach_skill": teach_skill,
        "learn_skill": learn_skill,
        "status": "pending"
    }
    data["proposals"].append(proposal)
    save_data(data)
    print("Skill exchange proposal created.")

def main():
    data = load_data()

    while True:
        print("\nSkillSwap Community Platform")
        print("1. Create Profile")
        print("2. Browse Skills")
        print("3. Propose Skill Exchange")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_profile(data)
        elif choice == "2":
            browse_skills(data)
        elif choice == "3":
            propose_exchange(data)
        elif choice == "4":
            print("Exiting application.")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()