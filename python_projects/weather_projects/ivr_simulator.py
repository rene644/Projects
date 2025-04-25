customer_data = { 
    "5551234": "Ricardo Pérez", 
    "5555678": "Ana López", 
    "5559012": "Javier Gómez", 
    "5553456": "Isabella Vargas" 
}
account_data = { 
    "12345": "Ricardo Pérez", 
    "67890": "Ana López", 
    "13579": "Javier Gómez", 
    "24680": "Isabella Vargas" 
} # Language data is broken down into small dictionaries 
general_prompts = { 
    "en": { 
        "welcome": "Welcome to Acme Customer Service!", 
        "goodbye": "Thank you for calling Acme Customer Service. Goodbye!", "invalid_selection": "Invalid selection. Please try again.", "too_many_attempts": "Too many invalid attempts. Defaulting to English.", 
        "proceeding_menu": "Proceeding to the main menu...", 
        "thank_you": "Thank you, {name}.", 
        "unable_to_verify": "Thank you. We were unable to verify your account at this time.", 
}, 
    "es": { 
        "welcome": "¡Bienvenido a Servicio al Cliente de Acme!", 
        "goodbye": "Gracias por llamar a Acme Customer Service. ¡Adiós!", "invalid_selection": "Selección inválida. Por favor, intente de nuevo.", 
        "too_many_attempts": "Demasiados intentos inválidos. Se utilizará el inglés por defecto.", 
        "proceeding_menu": "Procediendo al menú principal...", 
        "thank_you": "Gracias, {name}.", 
        "unable_to_verify": "Gracias. No pudimos verificar su cuenta en este momento.", 
} 
} 
language_selection_prompts = { 
    "en": { 
        "language_prompt": "For English, press 1.\nPara Español, oprima 2.\nPlease enter your selection: ", 
        "english_selected": "\nYou have selected English.", 
        "spanish_selected": "\nHa seleccionado Español.", 
},  "es": { 
        "language_prompt": "For English, press 1.\nPara Español, oprima 2.\nPlease enter your selection: ", 
        "english_selected": "\nYou have selected English.", 
        "spanish_selected": "\nHa seleccionado Español.", } 
}

caller_id_prompts = { 
    "en":{ 
        "caller_id_prompt": "Simulating incoming call from: {caller_id_raw} (Cleaned: {caller_id})", 
        "identify_prompt": "We see a number linked to an account. Is this your number? (1 for Yes, 2 for No)", 
}, 
    "es":{ 
        "caller_id_prompt": "Simulando llamada entrante de: {caller_id_raw} (Limpiado: {caller_id})", 
        "identify_prompt": "Vemos un número vinculado a una cuenta. ¿Es su número? (1 para Sí, 2 para No)", 
        } 
} 
main_menu_prompts = { 
    "en": { 
        "main_menu": "\nMain Menu: {name}", 
        "main_menu_options": [ 
            "1. For Account Information", 
            "2. Company Information", 
            "0. Speak to a Representative", 
            "9. To repeat these options", 
            "# or 'exit' to exit" 
            ], 
            }, 
            "es": { 
                "main_menu": "\nMenú Principal: {name}", 
                "main_menu_options": [ 
                    "1. Para Información de Cuenta", 
                    "2. Información de la Compañía", 
                    "0. Hablar con un Representante", 
                    "9. Para repetir estas opciones", 
                    "# o 'salir' para salir" 
                    ], 
} 
} 
sales_inquiry_prompts = { 
    "en":{ 
        "sales_inquiries": "\nSales Inquiries:", 
        "sales_message": "Thank you for your interest in Acme products and services.\nA sales representative will be with you shortly to assist with your sales inquiry.", 
        }, 
        "es":{ 
            "sales_inquiries": "\nConsultas de Ventas:", 
            "sales_message": "Gracias por su interés en los productos y servicios de Acme.\nUn representante de ventas estará con usted en breve para ayudarle con su consulta de ventas.", 
            } 
} 
technical_support_prompts = { 
    "en":{ 
        "technical_support": "\nTechnical Support:", 
        "tech_issue_prompt": "Please briefly describe your technical issue.", "ticket_created": "Thank you. A ticket has been created for your issue: '{issue}'. A technical support representative will call you back within 24 to 72 hours.", 
        }, 
        "es":{ 
            "technical_support": "\nSoporte Técnico:", 
            "tech_issue_prompt": "Por favor, describa brevemente su problema técnico.", 
            "ticket_created": "Gracias. Se ha creado un ticket para su problema: '{issue}'. Un representante de soporte técnico le devolverá la llamada dentro de 24 a 72 horas.", 
            } 
}
account_information_prompts = { 
    "en": { 
        "account_information": "\nAccount Information:", 
        "account_options": [ 
            "1. Balance Inquiry", 
            "2. View Recent Transactions", 
            "3. Check Account Status", 
            "4. Request a Statement", 
            "9. Go back to Main Menu" 
            ], 
            "invalid_account_selection": "Invalid selection.", 
            }, 
            "es": { 
                "account_information": "\nInformación de Cuenta:", "account_options": [ 
                    "1. Consulta de Saldo", 
                    "2. Ver Transacciones Recientes", 
                    "3. Verificar Estado de Cuenta", 
                    "4. Solicitar Estado de Cuenta", 
                    "9. Volver al Menú Principal" ], "invalid_account_selection": "Selección inválida.", 
                    } 
} 
account_status_prompts = { 
    "en":{ 
        "account_status": "\nAccount Status: Your account is currently active and in good standing.", 
        }, 
        "es":{ 
            "account_status": "\nEstado de la Cuenta: Su cuenta está activa y al día.", 
            } 
} 
statement_prompts = { 
    "en":{ "statement_sent": "\nA copy of your account statement has been sent to your registered email address.", 
          }, 
          "es":{ 
              "statement_sent": "\nSe ha enviado una copia de su estado de cuenta a su dirección de correo electrónico registrada.", 
              } 
} 
recent_transactions_prompts = { 
    "en":{ 
        "recent_transactions": "\nRecent Transactions:", 
    }, 
    "es":{ 
        "recent_transactions": "\nTransacciones Recientes:", 
        } 
} 
balance_inquiry_prompts = { 
    "en":{ 
        "balance_inquiry": "Simulating Balance Inquiry: Your current balance is $1,234.56", 
    }, 
    "es":{ 
        "balance_inquiry": "Simulando Consulta de Saldo: Su saldo actual es de $1,234.56", 
        } 
}

general_inquiries_prompts = { 
    "en":{ 
        "general_inquiries": "\nGeneral Inquiries / Assistance:", "inquiry_prompt": "Please briefly describe your inquiry.", "inquiry_processing": "Thank you. We are processing your inquiry: '{inquiry}'.", 
        "wait_options": "To wait on the line, press 1.\nTo schedule a callback, press 2.", 
        "connecting": "Connecting you to the next available representative. Please hold...", 
        "callback_scheduled": "Thank you. A callback has been scheduled for {time}.", 
    }, 
    "es":{ 
        "general_inquiries": "\nConsultas Generales / Asistencia:", "inquiry_prompt": "Por favor, describa brevemente su consulta.", "inquiry_processing": "Gracias. Estamos procesando su consulta: '{inquiry}'.", 
        "wait_options": "Para esperar en línea, oprima 1.\nPara programar una devolución de llamada, oprima 2.", 
        "connecting": "Conectando con el siguiente operador disponible. Por favor, espere...", 
        "callback_scheduled": "Gracias. Se ha programado una devolución de llamada para las {time}.", 
    } 
} 
operator_menu_prompts = { 
    "en":{ 
        "operator_menu": "\nSpeak to a Representative:", "operator_menu_options": [ "1. Sales Inquiries", "2. Technical Support", "3. General Inquiries / Assistance", "9. Go back to Main Menu" ], 
    }, 
    "es":{ 
        "operator_menu": "\nHablar con un Representante:", "operator_menu_options": [ "1. Consultas de Ventas", "2. Soporte Técnico", "3. Consultas Generales / Asistencia", "9. Volver al Menú Principal" ], 
        } 
}
company_info_prompts = { 
    "en":{ 
        "company_info": "\nCompany Information:", 
        "company_name": "Acme Corporation", 
        "company_address": "Main Office: 123 Main St, Anytown, USA", "company_website": "Website: www.acme.com", 
        "hours_of_operation": "General Hours of Operation: Monday - Friday, 9 AM - 5 PM", 
        "departments": "Departments:", 
        "sales_hours": " Sales: 9 AM - 6 PM", 
        "support_hours": " Support: 24/7", 
    }, 
    "es":{ 
        "company_info": "\nInformación de la Compañía:", 
        "company_name": "Acme Corporación", 
        "company_address": "Oficina Principal: 123 Main St, Anytown, USA", "company_website": "Sitio Web: www.acme.com", 
        "hours_of_operation": "Horario General de Atención: Lunes a Viernes, 9 AM - 5 PM", 
        "departments": "Departamentos:", 
        "sales_hours": " Ventas: 9 AM - 6 PM", 
        "support_hours": " Soporte: 24/7", 
        } 
}

def get_language_selection(): 
    """Prompts the user to select a language (English or Spanish) and returns the selection.""" 
    language = "en" 
    attempts = 0 
    while attempts < 3: 
        language_choice = input(language_selection_prompts[language]["language_prompt"]) 
        if language_choice == "1": 
            print(language_selection_prompts["en"]["english_selected"]) 
            language = "en" 
            break 
        elif language_choice == "2": 
            print(language_selection_prompts["es"]["spanish_selected"]) 
            language = "es" 
            break 
        else: 
            attempts += 1 
            print(general_prompts[language]["invalid_selection"]) 
    else: 
            print(general_prompts[language]["too_many_attempts"]) 
            return language 
def get_caller_id(): 
    """Simulates getting the caller ID and cleans it to digits only.""" 
    simulated_caller_id_raw = "555-1234" 
    simulated_caller_id = ''.join(filter(str.isdigit, simulated_caller_id_raw)) 
    print(caller_id_prompts["en"]["caller_id_prompt"].
          format(caller_id_raw=simulated_caller_id_raw, caller_id=simulated_caller_id)) 
    return simulated_caller_id 
def identify_caller_by_id(caller_id, language): 
     """Identifies the caller by their ID and asks for confirmation.""" 
     if caller_id in customer_data: 
        customer_name = customer_data[caller_id] 
        first_name = customer_name.split()[0] 
        if language == "en": 
            print(caller_id_prompts["en"]["identify_prompt"]) 
        elif language == "es": 
            print(caller_id_prompts["es"]["identify_prompt"]) 
            response = input("Please enter 1 for Yes, 2 for No: ") 
            # Added prompt 
        if response == "1": 
            print(general_prompts[language]["thank_you"].
                  format(name=first_name)) 
            return True, first_name 
        elif response == "2": 
            return False, None 
        else: 
            print(general_prompts[language]["invalid_selection"]) 
            return False, None 
        # added return else: return False, None 
def identify_caller_by_account(language): 
    """Prompts the user for their account number and attempts to identify them.""" 
    account_number_prompt = "Please enter your account number followed by the '#' key (just press Enter): " 
    if language == "en":
     "Por favor, ingrese su número de cuenta seguido de la tecla '#' (solo presione Enter): " 
    account_number = input(account_number_prompt)
    if account_number in account_data: 
            first_name = account_data[account_number].split()[0] 
            print(general_prompts[language]["thank_you"].
                  format(name=first_name) + general_prompts[language]["proceeding_menu"]) 
            return True, first_name 
    else: print(general_prompts[language]["unable_to_verify"]) 
    return False, None

def main_menu(language="en", first_name=None): 
    """Displays the main menu options based on the selected language.""" 
    print(main_menu_prompts[language]["main_menu"].
          format(name=first_name or '')) 
    options = main_menu_prompts[language]["main_menu_options"] 
    for option in options: 
        print(option) 
def sales_inquiries(language="en"): 
    """Handle sales inquiries based on the selected language.""" 
    print(sales_inquiry_prompts[language]["sales_inquiries"]) 
    print(sales_inquiry_prompts[language]["sales_message"]) 
    input("Press Enter to return to the Main Menu.") 
def technical_support(language="en"): 
    """Handle technical support based on the selected language.""" 
    print(technical_support_prompts[language]["technical_support"]) 
    issue = input(technical_support_prompts[language]["tech_issue_prompt"]) 
    print(technical_support_prompts[language]["ticket_created"].
          format(issue=issue)) 
def account_information(language="en"): 
    """Handles account information options based on the selected language.""" 
    print(account_information_prompts[language]["account_information"]) 
    options = account_information_prompts[language]["account_options"] 
    for option in options: 
        print(option) 
    while True: # added a loop 
        account_choice = input("Please enter your selection: ") 
        # changed this 
        if account_choice == "1": 
            balance_inquiry(language) 
            break 
        elif account_choice == "2": 
            view_recent_transactions(language) 
            break 
        elif account_choice == "3": 
            check_account_status(language) 
            break 
        elif account_choice == "4": 
            request_statement(language) 
            break 
        elif account_choice == "9": 
            return 
        # Go back to main menu 
    else: 
        print(account_information_prompts[language]["invalid_account_selection"]) 
    account_information(language) 
        # Removed recursive call, continue the loop continue # Continue the loop 
def check_account_status(language="en"): 
    """Simulates checking account status.""" 
    print(account_status_prompts[language]["account_status"]) 
    input("Press Enter to return to the Account Information Menu.") 
def request_statement(language="en"): 
    """Simulates requesting an account statement.""" 
    print(statement_prompts[language]["statement_sent"]) 
    input("Press Enter to return to the Account Information Menu.") 
def view_recent_transactions(language="en"): 
    """Simulates displaying recent account transactions.""" 
    print(recent_transactions_prompts[language]["recent_transactions"]) 
    transactions = [ {"date": "2025-04-19", "description": "Deposit", "amount": "+$500.00"}, {"date": "2025-04-18", "description": "Withdrawal", "amount": "-$50.00"}, {"date": "2025-04-17", "description": "Online Transfer", "amount": "-$120.00"}, ] 
    for transaction in transactions: 
        print(f"{transaction['date']} - {transaction['description']}: {transaction['amount']}") 
        input("\nPress Enter to return to the Account Information Menu.") 
def balance_inquiry(language="en"): 
    """Simulates balance inquiry.""" 
    print(balance_inquiry_prompts[language]["balance_inquiry"]) 
    input("Press Enter to return to the Account Information Menu.") 
def general_inquiries(language="en"): 
    """Handle general inquiries with options to wait or schedule a callback.""" 
    print(general_inquiries_prompts[language]["general_inquiries"]) 
    inquiry = input(general_inquiries_prompts[language]["inquiry_prompt"]) 
    print(general_inquiries_prompts[language]["inquiry_processing"].
          format(inquiry=inquiry)) 
    print(general_inquiries_prompts[language]["wait_options"]) 
    while True: 
        choice = input("Please enter your selection: ") 
        if choice == "1": 
            print(general_inquiries_prompts[language]["connecting"]) 
            input("Press Enter to return to the Main Menu.") 
            break 
        elif choice == "2": 
            callback_time = input("Please enter your preferred callback time (e.g., HH:MM): ") 
            print(general_inquiries_prompts[language]["callback_scheduled"].
            format(time=callback_time)) 
            input("Press Enter to return to the Main Menu.") 
            break 
        else: 
            print(general_prompts[language]["invalid_selection"]) 
def speak_to_operator(language="en"): 
    """Simulate connecting to an operator.""" 
    print(general_inquiries_prompts[language]["connecting"]) 
    input("Press Enter to return to the Main Menu.")

def connect_to_operator_menu(language="en"): 
    """Displays the sub-menu for speaking to different representatives.""" 
    print(operator_menu_prompts[language]["operator_menu"]) 
    options = operator_menu_prompts[language]["operator_menu_options"] 
    for option in options: 
        print(option) 
        choice = input("Please enter your selection: ") 
        return choice 
def company_information(language="en"): 
    """Provides company information.""" 
    print(company_info_prompts[language]["company_info"]) 
    print(company_info_prompts["en"]["company_name"]) 
    print(company_info_prompts["en"]["company_address"]) 
    print(company_info_prompts["en"]["company_website"]) 
    print(company_info_prompts["en"]["hours_of_operation"]) 
    print(company_info_prompts["en"]["departments"]) 
    print(company_info_prompts["en"]["sales_hours"]) 
    print(company_info_prompts["en"]["support_hours"]) 
    input("Press Enter to return to the Main Menu.") 
def ivr_simulator(): 
    """Simulates an Interactive Voice Response (IVR) system.""" 
    print(general_prompts["en"]["welcome"]) 
    language = get_language_selection() 
    caller_id = get_caller_id() 
    identified_by_id, first_name = identify_caller_by_id(caller_id, language) 
    identified = False 
    # Initialize the overall identified status -important 
    if identified_by_id: 
        identified = True 
        print(general_prompts[language]["proceeding_menu"]) 
    else: # Phone number not recognized or confirmed 
        attempts = 0 
        while attempts < 3 and not identified: 
            account_or_phone_prompt = "Please enter your account number OR the phone number associated with your account: " 
            if language == "en":
                "Por favor, ingrese su número de cuenta O el número de teléfono asociado con su cuenta: " 
            user_input = input(account_or_phone_prompt) # Try to identify by account number 
            if user_input in account_data: 
                first_name_account = account_data[user_input].split()[0] 
                print(general_prompts[language]["thank_you"].
                      format(name=first_name_account) + general_prompts[language]["proceeding_menu"]) 
                identified = True # Could check if the input matches another phone number in customer_data here as well. 
            elif user_input in customer_data: 
                first_name_by_phone = customer_data[user_input].split()[0] 
                print(general_prompts[language]["thank_you"].
                      format(name=first_name_by_phone) + general_prompts[language]["proceeding_menu"]) 
                identified = True 
            else: 
                attempts += 1 
                if attempts < 3: 
                    print(general_prompts[language]["invalid_selection"]) 
                    if not identified: 
                        print(general_prompts[language]["goodbye"]) 
                        return # Exit the ivr_simulator function # Interactive Main Menu 
                    while True: 
                        main_menu(language=language, first_name=first_name) 
                        choice = input("Please enter your selection: ") 
                        if choice == "1": 
                            account_information(language) 
                        elif choice == "2": 
                            company_information(language) 
                        elif choice == "0": 
                            operator_choice = connect_to_operator_menu(language) 
                            if operator_choice == "1": 
                                sales_inquiries(language) 
                            elif operator_choice == "2": 
                                technical_support(language) 
                            elif operator_choice == "3": 
                                general_inquiries(language) 
                            elif operator_choice == "9": 
                                continue # Go back to the main menu 
                            else: print(general_prompts[language]["invalid_selection"]) # added language here 
                        elif choice == "9": 
                            continue 
                        elif choice.strip() == "#" or  choice.strip().lower() == "exit" or  choice.strip().lower() == "salir": 
                        # Added salir print(general_prompts[language]["goodbye"]) # added language here 
                            break 
                        else: 
                            print(general_prompts[language]["invalid_selection"]) 
                            # added language here 
                        if __name__ == "__main__": ivr_simulator()