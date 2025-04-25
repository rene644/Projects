import os
import json
import time
import random
import logging
import argparse
from logging.handlers import RotatingFileHandler
import signal  # For timeout
import pyttsx3  # Import the text-to-speech library
import speech_recognition as sr  # Import the speech recognition library
from collections import deque

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")




SESSION_TIMEOUT = 300  # 5 minutes in seconds
TIMEOUT_WARNING_DELAY = SESSION_TIMEOUT - 60 # 4 minutes for warning
start_time = 0.0 # Initialize session start time
verification_attempts = 0 # Track verification attempts per call
caller_risk_level = "Safe" # Initialize caller risk level
caller_id = None  # Initialize caller_id as global
call_selections = [] # Initialize call_selections as global
# Simulate a simple in-memory risk database
caller_risk_database = {}
# Simulate call metadata tracking
caller_metadata = {}
CALL_FREQUENCY_THRESHOLD = 3 # Number of calls within FREQUENCY_WINDOW to flag
FREQUENCY_WINDOW = 60 # Seconds
ERRATIC_BEHAVIOR_THRESHOLD = 3 # Number of erratic actions to flag
# Global variables (if any)
ivr_prompts = {} # Example
customer_name = "Guest" # Global to store customer name



def speak_text(text):
    """Converts text to speech using pyttsx3."""
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logging.error(f"Error initializing or using pyttsx3: {e}")
        print("Text-to-speech functionality is unavailable due to an error.")



def recognize_speech():
    """Captures speech input and converts it into text while filtering noise."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak your response...")
        speak_text("Please speak your response.")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)  # Longer calibration for noisy environments
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)  # Limit speech duration
        except sr.WaitTimeoutError:
            print("No speech detected.")
            return None

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text.lower().strip()  # Remove unwanted spaces
    except sr.UnknownValueError:
        print("Couldn't understand, please try again.")
        speak_text("Couldn't understand, please try again.")
        return None
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        speak_text("Speech recognition service unavailable.")
        return None



def standardize_voice_response(response):
    """Maps common voice responses to standard input values."""
    voice_map = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
        "yes": "1", "yeah": "1", "yep": "1",
        "no": "0", "nope": "0",
        "exit": "0",
        "main menu": "9", "main": "9",
        "account information": "1", "account": "1",
        "company information": "2", "company": "2",
        "operator": "0" # Added operator mapping
    }
    return voice_map.get(response.lower(), response.lower())  # Default to original input



def retry_voice_input(prompt_key, max_retries=3):
    """Prompts user with a voice message and retries if no valid response is received."""
    retries = 0
    while retries < max_retries:
        display_message("en", ivr_prompts, prompt_key) # Access the global ivr_prompts
        response = recognize_speech()
        if response:
            return standardize_voice_response(response) # Standardize the response
        speak_text("I didn't catch that. Please try again.")
        retries += 1
    speak_text("Returning to the previous menu.")
    return None



def setup_logging(verbose=False):
    """Sets up logging with file rotation and verbosity control."""
    log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    log_handler = RotatingFileHandler("ivr_system.log", maxBytes=10240, backupCount=5, encoding="utf-8")
    log_handler.setFormatter(log_formatter)

    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    if verbose:
        logging.debug("Verbose mode enabled.")



def load_prompts(filepath="ivr_simulator_RT.json"):
    """Loads the IVR prompts and configuration from the JSON file and checks for essential keys."""

    # Dynamically determine the correct absolute path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, filepath)  # Use filepath dynamically

    try:
        # Open the file using json_path, NOT filepath
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Check for missing top-level keys
        required_keys = ["ivr_config", "ivr_prompts", "customers"]
        missing_keys = [key for key in required_keys if key not in data]
        if missing_keys:
            logging.error(f"Error: Missing essential top-level keys in '{json_path}': {missing_keys}")
            return {}

        # Check for missing ivr_config details
        ivr_config_keys = ["languages_supported", "welcome_message", "max_attempts"]
        missing_config_keys = [key for key in ivr_config_keys if key not in data.get("ivr_config", {})]
        if missing_config_keys:
            logging.warning(f"Warning: Missing IVR configuration keys: {missing_config_keys}")

        # ✅ **Handle Language-Based Welcome Prompt**
        language = "en"  # Change this based on user preference or IVR settings
        welcome_message = data.get("ivr_prompts", {}).get("general_prompts", {}).get(language, {}).get("welcome")

        # If not found, fall back to the general welcome message
        if not welcome_message:
            welcome_message = data.get("ivr_prompts", {}).get("general_prompts", {}).get("welcome", None)

        if not welcome_message:
            logging.warning(f"Warning: Missing 'welcome' prompt for language '{language}' and general fallback.")
        else:
            logging.info(f"Using welcome message: {welcome_message}")

        
        # Validate welcome prompt
        #if not data.get("ivr_prompts", {}).get("general_prompts", {}).get("welcome"):
        #    logging.warning("Warning: Missing 'welcome' prompt in 'general_prompts'.")

        logging.info(f"✅ Successfully loaded prompts from: {json_path}")
        return data

    except FileNotFoundError:
        logging.error(f"❌ Error: The file '{json_path}' was not found.")
        return {}
    except json.JSONDecodeError:
        logging.error(f"❌ Error: Could not decode JSON from '{json_path}'.")
        return {}
    except Exception as e:
        logging.error(f"❌ Unexpected error loading '{json_path}': {e}")
        return {}


def display_message(language, prompts, key, **kwargs):
    """Displays a localized message and also speaks it aloud."""
    lang_prompts = prompts.get(language, prompts.get("en", {}))
    prompt_text = lang_prompts.get(key, "Message unavailable").format(**kwargs)

    print(prompt_text)  # Display the message
    speak_text(prompt_text)  # Speak the message aloud
    if key not in lang_prompts:
        logging.warning(f"Missing prompt key '{key}' for '{language}'.")



def verify_high_risk_caller(caller_id, linked_account):
    """Requires extra authentication for flagged accounts."""
    security_questions = linked_account.get("security_questions", {})
    if not security_questions:
        logging.warning(f"Account for Caller ID {caller_id} marked high-risk but has no security questions.")
        display_message("en", ivr_prompts, "no_security_questions")
        return True # Proceed if no questions are set

    for question, correct_answer in security_questions.items():
        display_message("en", ivr_prompts, "security_question_prompt", question=question)
        response = retry_voice_input("security_question_prompt")
        if response is None or response.lower() != correct_answer.lower():
            logging.warning(f"Caller ID {caller_id} failed security question: {question}")
            display_message("en", ivr_prompts, "incorrect_security_answer")
            return False
        display_message("en", ivr_prompts, "correct_security_answer")
    return True



def categorize_caller_risk(caller_id, verification_attempts):
    """Assigns risk level based on current session attempts."""
    risk_levels = {
        0: "Safe",
        1: "Low Risk",
        2: "Moderate Risk",
        3: "High Risk",
        4: "Fraud Alert"
    }
    risk_score = min(verification_attempts, 4)  # Cap risk level at "Fraud Alert"
    return risk_levels[risk_score]



def update_caller_risk_in_database(caller_id, risk_level):
    """Persistently tracks fraud risk across multiple sessions (simulated)."""
    caller_risk_database[caller_id] = risk_level
    logging.info(f"Updated risk level for {caller_id}: {risk_level}")



def get_past_caller_risk(caller_id):
    """Retrieves the persistent risk level for a caller (simulated)."""
    return caller_risk_database.get(caller_id, "Safe")



def predict_fraud_risk(caller_id, past_risk, current_attempts, metadata):
    """Predicts risk level using historical patterns and current metadata."""
    # --- Integration Point for a Real ML Model ---
    # In a real application, you would feed caller_id, past_risk,
    # current_attempts, and the metadata dictionary to a trained
    # machine learning model here. The model would then output a
    # predicted risk level.
    # For this simulation, we'll use a rule-based approach:

    if metadata.get("call_frequency_flag", False):
        return "High Risk"
    if metadata.get("erratic_behavior_flag", False):
        return "Moderate Risk"

    if past_risk in ["High Risk", "Fraud Alert"] and current_attempts >= 1:
        return "Fraud Alert"
    elif past_risk == "Moderate Risk" and current_attempts >= 2:
        return "High Risk"
    return categorize_caller_risk(caller_id, current_attempts)



def analyze_call_metadata(caller_id, selections, language_changes):
    """Analyzes call behavior for potential fraud indicators."""
    metadata = {}
    current_time = time.time()

    if caller_id not in caller_metadata:
        caller_metadata[caller_id] = {"call_history": deque(maxlen=CALL_FREQUENCY_THRESHOLD), "language_changes": 0, "menu_changes": 0}

    caller_metadata[caller_id]["call_history"].append(current_time)
    if len(caller_metadata[caller_id]["call_history"]) == CALL_FREQUENCY_THRESHOLD and (current_time - caller_metadata[caller_id]["call_history"][0] < FREQUENCY_WINDOW):
        metadata["call_frequency_flag"] = True
        logging.warning(f"High call frequency detected for {caller_id}")

    caller_metadata[caller_id]["language_changes"] += language_changes
    if caller_metadata[caller_id]["language_changes"] >= ERRATIC_BEHAVIOR_THRESHOLD:
        metadata["erratic_behavior_flag"] = True
        logging.warning(f"Erratic language changes detected for {caller_id}")
        caller_metadata[caller_id]["language_changes"] = 0 # Reset after flagging

    # Simple erratic menu selection detection (can be expanded)
    if len(selections) > 5 and len(set(selections)) < 3: # Many selections but few unique ones
        metadata["erratic_behavior_flag"] = True
        logging.warning(f"Erratic menu selections detected for {caller_id}")

    return metadata



def alert_fraud_team(caller_id, risk_level):
    """Triggers fraud alert when risk level is critical."""
    if risk_level == "Fraud Alert":
        logging.critical(f"ALERT: Caller ID {caller_id} flagged as high-risk fraud attempt!")
        speak_text("Fraudulent activity detected. Alerting security team.")
        # Here, you can integrate an external fraud monitoring API or database update
        pass # Replace with actual alerting mechanism



def route_high_risk_caller(caller_id, risk_level):
    """Transfers flagged callers to manual review if necessary."""
    if risk_level in ["High Risk", "Fraud Alert"]:
        logging.critical(f"Routing Caller ID {caller_id} to security review.")
        display_message("en", ivr_prompts, "high_risk_routing")
        speak_text("You are being transferred to security verification.")
        # Integration with manual operator system could be added here.
        return True # Indicate that the call was routed
    return False # Indicate that the call was not routed



def get_language_selection(ivr_config, language_selection_prompts, general_prompts):
    """Prompts the user to select a language and returns the selection."""
    global current_language, language_changes
    languages = ivr_config.get("languages_supported", [])
    language = current_language # Use the current language
    attempts = 0

    while attempts < ivr_config.get("max_attempts", 3): # Default max attempts to 3
        display_message(language, language_selection_prompts, "language_prompt")
        language_choice = retry_voice_input("language_prompt")
        if language_choice is not None:
            if language_choice == "0":
                submenu = language_selection_prompts.get(language, {}).get("submenu", {})
                if submenu:
                    submenu_prompt = ""
                    submenu_map = {}
                    index_offset = 9 # Languages 1-9 are already covered
                    for i, (key, prompt) in enumerate(submenu.items()):
                        submenu_prompt += f"{key}. {prompt}\n"
                        submenu_map[str(i + 1)] = index_offset + i  # Use string keys for submenu map

                    print(submenu_prompt)
                    speak_text(submenu_prompt) # Speak the submenu
                    submenu_choice = retry_voice_input("submenu_prompt")
                    if submenu_choice in submenu_map:
                        selected_language_index = submenu_map[submenu_choice]
                        if 0 <= selected_language_index < len(languages):
                            new_language = languages[selected_language_index]
                            if new_language != current_language:
                                language_changes += 1
                                current_language = new_language
                            display_message(current_language, language_selection_prompts, "selected", language=current_language)
                            logging.info(f"Language selected: {current_language}")
                            return current_language
                        else:
                            attempts += 1
                            display_message(language, general_prompts, "invalid_selection")
                            logging.warning(f"Invalid language index selected: {selected_language_index}")
                    else:
                        attempts += 1
                        display_message(language, general_prompts, "invalid_selection")
                        logging.warning(f"Invalid submenu choice: {submenu_choice}")
                else:
                    attempts += 1
                    display_message(language, general_prompts, "invalid_selection")
                    logging.warning("User selected '0' for more languages, but no submenu is defined.")

            elif language_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                selected_language_index = int(language_choice) - 1
                if 0 <= selected_language_index < len(languages):
                    new_language = languages[selected_language_index]
                    if new_language != current_language:
                        language_changes += 1
                        current_language = new_language
                    display_message(current_language, language_selection_prompts, "selected", language=current_language)
                    logging.info



def handle_caller_identification(language, prompts, customers, caller_id, ivr_prompts): # Add this function here
    """Handles caller ID identification and account linking."""
    global verification_attempts, caller_risk_level, customer_name
    logging.info(f"Caller ID received: {caller_id}")
    display_message(language, prompts.get("caller_id_prompts", {}), "caller_id_prompt", caller_id_raw=caller_id, caller_id=caller_id)
    linked_account = next((cust for cust in customers.values() if cust.get("phone") == caller_id), None)

    past_risk = get_past_caller_risk(caller_id)
    verification_attempts = 0 # Reset attempts for the new session
    customer_name = "Guest" # Default name

    metadata = analyze_call_metadata(caller_id, call_selections, language_changes)
    predicted_risk = predict_fraud_risk(caller_id, past_risk, verification_attempts, metadata)
    caller_risk_level = predicted_risk
    update_caller_risk_in_database(caller_id, caller_risk_level)
    alert_fraud_team(caller_id, caller_risk_level)

    if route_high_risk_caller(caller_id, caller_risk_level):
        return None # Call routed, end identification

    if linked_account:
        customer_name = linked_account.get("name", "Customer")
        logging.info(f"Caller matched to: {customer_name}, Past Risk: {past_risk}, Current Predicted Risk: {caller_risk_level}")
        display_message(language, prompts.get("caller_id_prompts", {}), "identified", name=customer_name)
        if linked_account.get("high_risk", False) or past_risk in ["High Risk", "Fraud Alert"]:
            if verify_high_risk_caller(caller_id, linked_account, ivr_prompts):
                display_message(language, prompts.get("caller_id_prompts", {}), "identify_prompt")
                return linked_account # Identification successful
            else:
                display_message(language, prompts.get("caller_id_prompts", {}), "failed_verification")
                return None # Identification failed
        else:
            confirmation = retry_voice_input("identify_prompt", ivr_prompts)
            if confirmation and standardize_voice_response(confirmation) in ["1", "yes", "yeah", "yep"]:
                return linked_account # Identification confirmed
            else:
                display_message(language, prompts.get("caller_id_prompts", {}), "not_confirmed")
                return None # Identification not confirmed
    else:
        display_message(language, prompts.get("caller_id_prompts", {}), "unrecognized")
        return None # Caller ID not found



def display_main_menu(language, prompts, name="Guest"):
    """Displays the main menu options."""
    display_message(language, prompts.get("general_prompts", {}), "welcome", name=name)
    display_message(language, prompts.get("main_menu_prompts", {}), "main_menu_options")



def display_account_information_menu(language, prompts):
    """Displays the account information submenu."""
    display_message(language, prompts.get("account_information_prompts", {}), "account_information")
    account_options = prompts.get("account_information_prompts", {}).get(language, {}).get("account_options", prompts.get("account_information_prompts", {}).get("en", {}).get("account_options", []))
    for i, option in enumerate(account_options):
        print(f"{i+1}. {option}")
        speak_text(f"{i+1}. {option}") # Speak each account option with number
    print("0. Back to Main Menu")
    speak_text("0. Back to Main Menu")
    if not account_options:
        logging.warning("Account information options not found for the selected language or English.")
    # Add logic to handle selections from this menu later



def display_company_information(language, prompts):
    """Displays company information."""
    display_message(language, prompts.get("company_info_prompts", {}), "company_info")
    display_message(language, prompts.get("company_info_prompts", {}), "company_name")
    display_message(language, prompts.get("company_info_prompts", {}), "company_address")
    display_message(language, prompts.get("company_info_prompts", {}), "company_website")
    display_message(language, prompts.get("company_info_prompts", {}), "hours_of_operation")
    display_message(language, prompts.get("company_info_prompts", {}), "departments")
    display_message(language, prompts.get("company_info_prompts", {}), "sales_hours")
    display_message(language, prompts.get("company_info_prompts", {}), "support_hours")
    time.sleep(2)
    print("\nReturning to the main menu...")
    speak_text("Returning to the main menu.") # Speak the return message
    time.sleep(1)



def connect_to_operator_menu(language, prompts):
    """Displays the menu for connecting to an operator."""
    display_message(language, prompts.get("operator_menu_prompts", {}), "connecting_operator")
    # In a real system, you would initiate a transfer here.
    print("Connecting you to a live operator. Please wait...")
    speak_text("Connecting you to a live operator. Please wait...")
    time.sleep(3) # Simulate connection time
    print("You are now being connected.")
    speak_text("You are now being connected.")
    # You might want to exit the IVR or return to a previous menu after this.


def handle_main_menu_selection(language, prompts, selection):
    """Handles the user's selection from the main menu using a dispatch pattern."""
    menu_actions = {
        "1": display_account_information_menu,
        "2": display_company_information,
        "0": "exit",
        "9": display_main_menu
        # "3": connect_to_operator_menu, # Uncomment if you implement this
    }



def log_call_session(caller_id, selections, start_time, risk_level):
    """Logs the caller ID, menu selections, call duration, and risk level."""
    session_duration = round(time.time() - start_time, 2)
    with open("call_history.log", "a", encoding="utf-8") as file:
        file.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Caller ID: {caller_id}\n")
        file.write(f"Risk Level: {risk_level}\n")
        file.write(f"Session Duration: {session_duration} seconds\n")
        if selections:  # Ensure selections exist before writing
            file.write(f"Selections: {', '.join(selections)}\n")
        else:
            file.write("No selections made.\n")
        file.write("\n")




def timeout_handler(signum, frame):
    """Handles session timeout due to inactivity with a grace period."""
    print("\nSession timed out due to inactivity.")
    logging.warning("IVR session ended due to inactivity.")
    speak_text("Session timed out due to inactivity.") # Speak the timeout message

    response = retry_voice_input("timeout_prompt")
    if response is None or standardize_voice_response(response) != "0":
        print("Session resumed. Timeout reset.")
        logging.info("IVR session resumed after timeout interruption.")
        speak_text("Session resumed.") # Speak the resume message
        signal.signal(signal.SIGALRM, timeout_warning)  # Reset the warning timer
        signal.alarm(TIMEOUT_WARNING_DELAY)  # Reset the warning alarm
        return
    else:
        print("Exiting IVR system.")
        speak_text("Exiting IVR system.") # Speak the exit message
        global caller_id, call_selections, start_time, caller_risk_level # Declare as global to access
        log_call_session(caller_id, call_selections, start_time, caller_risk_level) # Log before exiting
        exit()



def timeout_warning(signum, frame):
    """Handles session timeout warning due to inactivity."""
    print("\nWarning: Your session will timeout in 60 seconds due to inactivity.")
    logging.warning("IVR session will timeout in 60 seconds.")
    speak_text("Warning: Your session will timeout in 60 seconds due to inactivity.") # Speak the warning
    signal.signal(signal.SIGALRM, timeout_handler) # Set the final timeout handler
    signal.alarm(60) # Set the 60-second alarm



def simulate_caller_id(customers, debug_mode=False, debug_caller_id=None):
    """Simulates an incoming call and returns either a random or custom caller ID."""
    if debug_mode and debug_caller_id:
        logging.info(f"Using debug caller ID: {debug_caller_id}")
        return debug_caller_id  # Use provided caller ID for debugging
    customer_phones = [customer.get("phone") for customer in customers.values() if customer.get("phone")]
    if customer_phones:
        caller_id = random.choice(customer_phones)
        logging.info(f"Simulated caller ID: {caller_id}")
        return caller_id
    else:
        logging.warning("No customer phone numbers found for simulation.")
        return "UNKNOWN"



def main():
    global start_time, caller_id, call_selections, caller_risk_level
    parser = argparse.ArgumentParser(description="Simulate an IVR system.")
    parser.add_argument("--config", type=str, default="ivr_simulator_RT.json", help="Path to IVR JSON config file")
    parser.add_argument("--debug_caller_id", type=str, help="Enter a custom caller ID for testing.")
    parser.add_argument("--verbose", action="store_true", help="Enable detailed logs.")
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Verbose mode enabled.")
    setup_logging(args.verbose) # Initialize logging with verbosity

    prompts_data = load_prompts(args.config) # This line is important
    if not prompts_data:
        return

    ivr_prompts = prompts_data.get("ivr_prompts", {}) # And this line
    if not ivr_prompts:
        logging.error("IVR prompts missing from JSON data!")
        return

    ivr_config = prompts_data.get("ivr_config", {})
    language_selection_prompts = ivr_prompts.get("language_selection_prompts", {})
    general_prompts = ivr_prompts.get("general_prompts", {})
    welcome_messages = ivr_config.get("welcome_message", {"en": "Welcome!"})
    customers = prompts_data.get("customers", {})

if __name__ == "__main__":
    main()