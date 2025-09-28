from unittest import case


class PhoneBook:
    def menu(self):
        print("""
        ---- PhoneBook ----
        1. Search
        2. Service Nos
        3. Add Name
        4. Erase
        5. Edit
        6. Assign Tone
        7. Send b'card
        8. Options
        9. Speed Dials
        10. Voice Tags
        """)
        choice = int(input("Select PhoneBook option: "))
        match choice:
            case 1: print("Search")
            case 2: print("Service Nos")
            case 3: print("Add Name")
            case 4: print("Erase")
            case 5: print("Edit")
            case 6: print("Assign Tone")
            case 7: print("Send b'card")
            case 8:
                print("""
                1. Type of View
                2. Memory Status
                """)
                sub = int(input("Select Option: "))
                match sub:
                    case 1: print("Search")
                    case 2: print("Service Nos")
            case 9: print("Speed Dials")
            case 10: print("Voice Tags")
            case _: print("Invalid Input")


class Messages:
    def menu(self):
        print("""
        ---- Messages ----
        1. Write Message
        2. Inbox
        3. Outbox
        4. Picture Message
        5. Template
        6. Smileys
        7. Message Settings
        8. Info Service
        9. Voice MailBox Number
        10. Service Command Editor
        """)
        choice = int(input("Select Message option: "))
        match choice:
            case 1: print("Write Message")
            case 2: print("Inbox")
            case 3: print("Outbox")
            case 4: print("Picture Message")
            case 5: print("Template")
            case 6: print("Smileys")
            case 7:
                print("""
                1. Set
                2. Common
                """)
                setting = int(input("Enter Message Setting: "))
                if setting == 1:
                    print("""
                    1. Message Center Number
                    2. Message Sent As
                    3. Message Validity
                    """)
                elif setting == 2:
                    print("""
                    1. Delivery Report
                    2. Reply Via Same Center
                    3. Character Support
                    """)
            case 8: print("Info Service")
            case 9: print("Voice MailBox Number")
            case 10: print("Service Command Editor")
            case _: print("Invalid Input")


class CallRegister:
    def menu(self):
        print("""
        ---- Call Register ----
        1. Missed Calls
        2. Received Calls
        3. Dialled Numbers
        4. Erase Recent Call Lists
        5. Show Call Duration
        6. Show Call Cost
        7. Call Cost Settings
        8. Prepaid Credit
        """)
        choice = int(input("Select Call Register option: "))
        match choice:
            case 1: print("Missed Calls")
            case 2: print("Received Calls")
            case 3: print("Dialled Numbers")
            case 4: print("Erase Recent Call Lists")
            case 5: print("Show Call Duration")
            case 6: print("Show Call Cost")
            case 7: print("Call Cost Settings")
            case 8: print("Prepaid Credit")
            case _: print("Invalid Input")


class Tones:
    def menu(self):
        print("""
        ---- Tones ----
        1. Ringing tone
        2. Ringing Volume
        3. Incoming call alert
        4. Composer
        5. Message alert tone
        6. Keypads tones
        7. Warning and game tones
        8. Vibrating alert
        9. Screen saver
        """)
        choice = int(input("Select Tones option: "))
        match choice:
            case 1: print("Ringing tone")
            case 2: print("Ringing Volume")
            case 3: print("Incoming call alert")
            case 4: print("Composer")
            case 5: print("Message alert")
            case 6: print("Keypads tones")
            case 7: print("Warning and game tones")
            case 8: print("Vibrating alert")
            case _: print("Invalid Input")


class Settings:
    def menu(self):
        print("""
        ---- Settings ----
        1. Call Settings
        2. Phone Settings
        3. Security settings
        4. Restore factory settings
        """)
        choice = int(input("Select Settings option: "))
        match choice:
            case 1: print("""
                  call settings menu
                  1. Automatic Redial
                  2. Speed dialing
                  3. Call Waiting
                  4. Own Number Sending
                  5. Phone in use
                  6. Automatic answer
            """)
            choice = int(input("call settings menu: "))
            match choice:
                case 1: print("Automatic Redial")
                case 2: print("Speed dialing")
                case 3: print("Call Waiting")
                case 4: print("Own Number Sending")
                case 5: print("Phone in use")
                case 6: print("Automatic answer")
                case _: print("Invalid Input")

            case 2: print("""
                phone settings menu
                 1. Language
                 2. Cell info display
                 3. Welcome note
                 4. Network selection
                 5. Lights
                 6. Confirm SIM service actions
                 """)
            sub = int(input("phone settings menu: "))
            match sub:
                case 1: print("Language")
                case 2: print("Cell info display")
                case 3: print("Welcome note")
                case 4: print("Network selection")
                case 5: print("Lights")
                case 6: print("Confirm SIM service actions")
                case _: print("Invalid Input")
            



class Nokia3310:
    def __init__(self):
        self.phonebook = PhoneBook()
        self.messages = Messages()
        self.callregister = CallRegister()
        self.tones = Tones()
        self.settings = Settings()



    def main_menu(self):
        while True:
            print("""
            ==== NOKIA 3310 MENU ====
            1. PhoneBook
            2. Messages
            3. Chat
            4. Call Register
            5. Tones
            6. Settings
            7. Call Divert
            8. Games
            9. Calculator
            10. Reminders
            11. Clock
            12. Profiles
            13. SIM Services
            0. Exit
            """)
            try:
                choice = int(input("Choose an option: "))
                match choice:
                    case 1: self.phonebook.menu()
                    case 2: self.messages.menu()
                    case 3: print("Chat")
                    case 4: self.callregister.menu()
                    case 5: self.tones.menu()
                    case 6: self.settings.menu()
                    case 7: print("Call Divert")
                    case 8: print("Games")
                    case 9: print("Calculator")
                    case 10: print("Reminders")
                    case 11: print("Clock")
                    case 12: print("Profiles")
                    case 13: print("SIM Services")
                    case 0:
                        print("Exiting Nokia 3310...")
                        break
                    case _: print("Invalid Input")
            except ValueError:
                print(" Please enter a valid number.")


if __name__ == "__main__":
    phone = Nokia3310()
    phone.main_menu()

