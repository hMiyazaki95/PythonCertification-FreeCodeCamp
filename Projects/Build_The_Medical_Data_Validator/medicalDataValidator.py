# imported re to use a regular espression to check that patient_id also has a specific parttern
import re

# dictionary with sample medical records data
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
    # To test the second conditional statement, 
    # add two items of your choice that are not 
    # dictionaries at the end of the medical_records list. 
    # You should see two validation messages printed to the terminal.
    # "Not a dictionary"
    # 000111
]
# find invalid values in a dictionary
def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
         # 'patient_id' is the name of the field being validated.
        # isinstance() checks whether patient_id is a string.
        # If it is a string, re.search() checks whether it contains
        # the lowercase letter 'p'.
        # The second check runs only if the first check returns True.
        # lowercase p does not match P1001
        # and operator returns falsy 
        # since id can starts with lowercase or uppercase, add third argument (re.IGNORECASE) to use flags
        # add \d after p because \d means any digit from 0 to 9.
            #   p1     ✅ matches
            # P5     ✅ matches because of re.IGNORECASE
            # p1001  ✅ matches the beginning, "p1"
            # px     ❌ does not match
            # p.5    ❌ does not match because the digit is not immediately after p
        # add quantifier to regex patternto match one or more digit
        #'patient_id': isinstance(patient_id, str) and re.search('\d+', patient_id, re.IGNORECASE)
        # Replace the search call with a fullmatch function to ensure no extra characters are found in the string.
        'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE)
        # verify age is an integer 
        # age should not only be a integer, positive integer greater than or equal to 18
        'age': isinstance(age, int) and age >= 18
    }
    return constraints
# validate the data set
def validate(data):
    # You want to ensure that your data is either a list or a tuple. Therefore, within the validate function, 
    # declare a variable named is_sequence and assign 
    # it a call to isinstance. Pass in data as the first 
    # argument and a tuple containing list and tuple as the second argument.
    is_sequence = isinstance(data,(list, tuple))
    
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    
    is_invalid = False
    
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )
    # create the for loop to iterate over data
    # set index variable and item variable (dictionary)
    # for index, dictionary in enumerate(data):
    #     pass
    
    # The f-string fix: The {} placeholder automatically converts the integer into text for you.
    # Inside your for loop, if the item in dictionary is not an instance of dict, print Invalid format: expected a dictionary at position <index>. (where <index> should be replaced by the current index) and set is_invalid to True.
    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True
            
        # if the set of keys from the current dictionary is different from key_set
        # to test out comment out the age key in the first dictionary 
        # Output ###################################################
        # Invalid format: {'patient_id': 'P1001', 'gender': 'Female', 'diagnosis': 'Hypertension', 'medications': ['Lisinopril'], 'last_visit_id': 'V2301'} at position 0 has missing and/or invalid keys.
        if key_set != set(dictionary.keys()):
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            is_invalid = True
    
    if is_invalid:
        return False
    print("Valid format.")
    return True
    # output
    # // running tests
    # // tests completed
    # // console output
    # Valid format.
    
# To test the first if statement of your function
# # Invalid format: expected a list or tuple., turn medical_records into a string. You should see Invalid format: expected a list or tuple. printed to the terminal.
# medical_records = "string"

    # check keys are ordered and make sure it doesn't have a same numeber, extra, or misspelled.
    # key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

validate(medical_records)
# The ** operator can be used to unpack the elements in a dictionary and pass them as keyword arguments in a function call:
print(find_invalid_records(**medical_records[0]))