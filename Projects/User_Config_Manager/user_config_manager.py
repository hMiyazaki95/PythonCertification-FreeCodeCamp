# create a dictionary named test_settings and add some values to it.
test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}

#  define a function named add_setting.
# 4. add_setting should convert the key to lowercase.
# Failed:5. add_setting should convert the value to lowercase.
def add_setting(current_settings, new_settings):
    # new_settings = {
    #     key.lower(): value for key, value in test_settings.items()
    # }

    #separate the tuple into its key and value
    key, value = new_settings
    # conver both key and value to lowercase
    key = key.lower()
    value = value.lower()
    # Check whether the setting already exists.
    if key in current_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
        
    # Add the new key-value pair to the dictionary.
    current_settings[key] = value
    # Return the required success message.
    return f"Setting '{key}' added with value '{value}' successfully!"
    
    

    # this updates the current_settings by applying new settings
    current_settings.update(new_settings)
    # return current settings
    return current_settings

def update_setting(current_settings, new_settings):
    # Separate the tuple into its key and value.
    key, value = new_settings
    # Convert the key to lowercase.
    key = key.lower()
    # Convert the value to lowercase.
    value = value.lower()
    # Return an error if the key does not exist.
    if key not in current_settings:
        return (
    f"Setting '{key}' does not exist! "
    "Cannot update a non-existing setting."
)
    # Update the existing dictionary value.
    current_settings[key] = value

    return f"Setting '{key}' updated to '{value}' successfully!"
# delete setting will remove the key from the existing setting so the first argument is current_settings
# Since it's asking to delete the key, question will be which key we will delete so key will be the second parameter
def delete_setting(current_settings, key):
    # only asking to conver the key to lowercase so we only declair the key
    key = key.lower()
    if key not in current_settings:
        return "Setting not found!"
    
    del current_settings[key]
    return f"Setting '{key}' deleted successfully!"

# view setting is only to check the existing settings so it takes only one argument, current_settings
def view_settings(current_settings):
    if not current_settings:
        return "No settings available."
    formatted_settings = "Current User Settings:\n"
    for key, value in current_settings.items():
        formatted_settings += f"{key.capitalize()}: {value}\n"
    return formatted_settings


  

  