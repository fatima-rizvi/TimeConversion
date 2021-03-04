def timeConversion(s):
    #
    # Write your code here.
    #
    # Input:
        # A string representing a clock in hh:mm:ssAM/PM
        # Example: 07:05:45PM
    # Output
        # A string representing the input, but in military time
        # Example: 19:05:45
    # Constraints
        # All inputs are valid
    # Solutions
        # Use slicing to check if input time is am or pm
        # Create a variable to hold the hours, because thats the only thing that really needs to change
        # If the time is PM
          # Check that the hours are not equal to 12
            # Increase the value of hours by 12
        # If the time is AM
            # Check if the hours are equal to 12
                # If so, set it to 0
                # Else, leave them alone
            
        # Create a new string to be returned as the result.
        # Add the value of hours as a string to the result
        # Using slicing, append the rest of the input string, minus the last two letters, to the result string
        # Return the result.
                
    # Edge cases
        # If the time passed in is 12PM, we don't need to alter the hours.
    # Tests
    
    time = s[-2:]
    hours = s[:2]
    if time == "PM":
        if hours != "12":
            hours = int(hours)
            hours += 12
    if time == "AM":
        if hours == "12":
            hours = "00"
    res = ''
    res += str(hours)
    res += s[2:-2]
    
    return res
