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
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name."
        )
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
        return(f"Setting {key} does not exist! Cannot update a non-existing setting.")
    # Update the existing dictionary value.
    current_settings[key] = value

    return f"Setting '{key}' updated to '{value}' successfully!"
    



  