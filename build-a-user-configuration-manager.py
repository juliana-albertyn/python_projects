
# In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. 
# You will implement functions to add, update, delete, and view user settings.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair

# add_setting function should:

# Convert the key and value to lowercase.
# If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
# If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!.
# The messages returned should have the key and value in lowercase.
# You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

# update_setting function should:

# Convert the key and value to lowercase.
# If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
# If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
# The messages returned should have the key and value in lowercase.
# You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

# delete_setting function should:

# Convert the key passed to lowercase.
# If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
# If the key setting does not exist, return Setting not found!
# The messages returned should have the key in lowercase.
# You should define a function named view_settings with one parameter representing a dictionary of settings.

# view_settings function should:

# Return No settings available. if the given dictionary of settings is empty.
# If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
# Current User Settings:
# Theme: dark
# Notifications: enabled
# Volume: high

# For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.

# You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair
def add_setting(user_settings: dict[str,str], new_entry : tuple[str, str]) -> str:
    new_key, new_value = new_entry
    # Convert the key and value to lowercase.
    new_key = new_key.lower()
    new_value = new_value.lower()
    
    # If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
    # If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!.
    if new_key in user_settings.keys():
        return f"Setting '{new_key}' already exists! Cannot add a new setting with this name."
    else:
        user_settings[new_key] = new_value
        return f"Setting '{new_key}' added with value '{new_value}' successfully!"

# You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.
def update_setting(user_settings: dict[str,str], update_entry : tuple[str, str]) -> str:
    existing_key, new_value = update_entry
    # Convert the key and value to lowercase.
    existing_key = existing_key.lower()
    new_value = new_value.lower()

    # If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
    # If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
    if existing_key in user_settings.keys():
        user_settings[existing_key] = new_value
        return f"Setting '{existing_key}' updated to '{new_value}' successfully!"
    else:
        return f"Setting '{existing_key}' does not exist! Cannot update a non-existing setting."

# You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.
def delete_setting(user_settings: dict[str,str], delete_key : str) -> str:
    # Convert the key passed to lowercase.
    delete_key = delete_key.lower()
    
    # If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
    # If the key setting does not exist, return Setting not found!
    if delete_key in user_settings:
        user_settings.pop(delete_key, '')
        return f"Setting '{delete_key}' deleted successfully!"
    else:
        return f"Setting not found!"


# You should define a function named view_settings with one parameter representing a dictionary of settings.
def view_settings(user_settings: dict[str,str]) -> str:
# Return No settings available. if the given dictionary of settings is empty.
# If the dictionary contains any settings, return a string displaying the settings. 
# The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized. 
# For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
    if user_settings == {}:
        return "No settings available."
    else:
        s = "Current User Settings:\n"
        for key, value in user_settings.items():
            s += f'{key.capitalize()}: {value}\n' 
        return s    


test_settings = dict()

test_settings["theme"] = "dark"
print(add_setting(test_settings, ("Theme", "dark")))
print(add_setting(test_settings, ("Language", "English")))
print(add_setting(test_settings, ("Notifications", "enabled")))
print(add_setting(test_settings, ("Volume", "high")))

print(update_setting(test_settings, ("Volume", "low")))
print(update_setting(test_settings, ("Color", "pink")))

print(delete_setting(test_settings, "Theme"))
print(delete_setting(test_settings, "Color"))

print(view_settings(test_settings))
