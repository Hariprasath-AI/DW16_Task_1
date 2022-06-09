# importing 'json' module for handling json file
import json

numbers = ['0','1','2','3','4','5','6','7','8','9']

special_characters = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '|', '\\', '}', '{', '[', ']', "'", '"', ':', ';', '?', '/', '>', '<', '.', ',']

allowed_characters_in_username = ['0','1','2','3','4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                                  't', 'u', 'v', 'w', 'x', 'y', 'z']
only_alpha = ['a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']

only_alpha_upper = [x.upper() for x in only_alpha]

top_level_domain_alpha = ['a', 'b', 'c', 'd', 'e' , 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z','.']

# This function is used check whether the password we entered satisfies the constrains mentioned below:
# "1. One number is must", "2. One special character is must", "3. One lowercase alphabet is must", "4. One uppercase alphabet is must", sep = "\n"
def password_validation(val):
    upper_alpha_count = 0
    lower_alpha_count = 0
    special_char_count = 0
    numbers_count = 0
    for i in range(0, len(val)):
        if val[i] in only_alpha_upper:
            upper_alpha_count += 1
        elif val[i] in only_alpha:
            lower_alpha_count += 1
        elif val[i] in special_characters:
            special_char_count += 1
        elif val[i] in numbers:
            numbers_count += 1

    return upper_alpha_count, lower_alpha_count, special_char_count, numbers_count

# This function is used to whether the domain contains any special characters. Because, special characters not allowed in domain name.
def check_domain(val):
    domain_count = 0
    for i in range(0, len(val)):
        if val[i] not in only_alpha:
            domain_count += 1
        else:
            continue
    return domain_count

# This function is used to whether the top level domain contains any special characters. Because, special characters not allowed in top level domain name.
def top_level_domain_check(val):
    top_level_domain_count = 0
    for i in range(0, len(val)):
        if val[i] not in top_level_domain_alpha:
            top_level_domain_count += 1
        else:
            continue
    return top_level_domain_count

# This function is used to convert the upppercase letters in the E-mail ID to lowercase. Even if we enter E-mail ID in uppercase, it stores in lowercase.
def standard_format(val):
    string = list(val)
    for i in range(0, len(val)):
        if string[i].isalpha() and string[i].isupper():
            string[i] = string[i].lower()

    string = "".join(string)
    return string

# This function is used to check whether there is a special characters in the username. Because, special characters in username is not allowed
def user_name_sub_check(user_name_sub):
    count = 0
    for i in range(len(user_name_sub)):
        if (user_name_sub[i] not in allowed_characters_in_username):
            count += 1
        else:
            continue

    return count

# This "check_mail_id" function is used to validate the email_id that we entered
def check_mail_id(mail_id):
    if '@' and '.' in mail_id:
        for i in range(0, len(mail_id)):
            val = mail_id[i]
            if val == '@':
                at_the_rate_index = i
                break

        for j in range(at_the_rate_index + 1, len(mail_id)):
            if mail_id[j] == '.':
                dot_index = j
                break
            else:
                continue
        temp_mail_id = list(mail_id)

        # E-mail ID format must contains only one '@' special character. If condition no satisfied, it shows "Invalid mail format"
        count_of_at_the_rate = temp_mail_id.count('@')
        if at_the_rate_index < dot_index and count_of_at_the_rate == 1:
            list_mail_id = mail_id
            list_mail_id = list_mail_id.split("@")
            user_name = list_mail_id[0]


            list_mail_id = list_mail_id[1].split(".", 1)

            # Domain of E-mail
            domain = list_mail_id[0]

            # Top level domain of E-mail
            top_level_domain = list_mail_id[1]

            # Username , domain and top level domain. All the three must not be empty
            if len(user_name) != 0 and len(domain) != 0 and len(top_level_domain):
                # Process username from 2nd character onwards. Because in username 2nd character onwards numbers are allowed
                user_name_sub = user_name[1:]

                # 1st Character in username must not be number or special character. Or may be alphabets.
                if (user_name[0] not in numbers) and (user_name[0] in allowed_characters_in_username):
                    user_name_count = user_name_sub_check(user_name_sub)
                    domain_count = check_domain(domain)
                    top_level_domain_count = top_level_domain_check(top_level_domain)

                    # We have to check if the E-mail ID(username, domain, top level domain) contains any other characters which are not allowed.
                    # If contains only allowed characters, it will asks user to enter password. Else it shows "Invalid E-mail ID format"
                    if (user_name_count == 0) and (domain_count == 0) and (top_level_domain_count == 0):
                        mail_id = standard_format(mail_id)
                        print("-----Captial letters are not allowed in E-mail ID, so the standard format given below for suggesstion-----")
                        print("Standard format of Email ID:", mail_id)
                        new_password = str(input("Create a new password for registration: "))

                        # After entering password, we have to check whether the password meets the certain criteria
                        # Condition, 1. length is betweeen 5 and 16
                        if len(new_password) >= 5 and len(new_password) <= 16:
                            upper_alpha_count, lower_alpha_count, special_char_count, numbers_count = password_validation(new_password)

                            # Condition, 2. Uppercase letter, lowercase letter, special character, number.
                            # It is must to have all  the four type of characters in the password with the count minimum of one each.
                            if upper_alpha_count >= 1 and lower_alpha_count >= 1 and special_char_count >= 1 and numbers_count >= 1:
                                re_new_password = str(input("Re-enter the password your entered before : "))

                                # For the confirmation, we have to ask one more time to enter the password to validate and register!!
                                # If Both the password were perfectly matches, the E-mail ID will be registered successfully.
                                # Else it shows "Registration Failed Re-enter your password correctly"
                                if new_password == re_new_password:
                                    with open("Task_1.json", "r") as f:
                                        result = json.load(f)

                                    result[mail_id] = re_new_password

                                    with open("Task_1.json", "w") as f:
                                        json.dump(result, f)
                                    print("---------Registered Successfully-----------")
                                else:
                                    print("!!!!!!!!Registration Failed. Re-enter your password correctly!!!!!!!!")
                            else:
                                print("-----------Invalid password format-----------",
                                      "Constraints: ",
                                      "1. One number is must", "2. One special character is must", "3. One lowercase alphabet is must", "4. One uppercase alphabet is must", sep = "\n")
                                print("------------------Reason----------------------")
                                if upper_alpha_count < 1:
                                    print("One uppercase character is missing in the password you entered")
                                if lower_alpha_count < 1:
                                    print("One lowercase character is missing in the password you entered")
                                if special_char_count < 1:
                                    print("One special character is missing in the password you entered")
                                if numbers_count < 1:
                                    print("One number is missing in the password you entered")
                        else:
                            print("Length of the password is limited between 5 and 16")

                    else:
                        print("-----------Invalid E-mail ID format---------------")
                        print("Special characters are not allowed")
                else:
                    print("-----------Invalid E-mail ID format---------------")
                    if user_name[0] in numbers:
                        print("E-mail ID does not starts with number")
                    elif user_name[0] not in allowed_characters_in_username:
                        print("E-mail ID does not starts with special character")
            else:
                print("-----------Invalid E-mail ID format---------------")
                if len(user_name) == 0:
                    print("Username is must before '@' special character")
                if len(domain) == 0:
                    print("Mail Domain('gmail', 'yahoo', 'outlook',...) is must after '@' special character")
                if len(top_level_domain) == 0:
                    print("Top level domain('in', 'com') is must after '.' ")
        else:
            print("Invalid E-mail ID format, Hint :",
                  "1. Whether your mail ID contains two or more/zero number of '@' special character",
                  "2. Or '@', '.' were missing. Or position mismatched for those special character",
                  "E.g : username@gmail.com", sep = "\n")
    else:
        print("-----------Invalid E-mail ID format---------------",
              "'@' or '.' is missing in the E-mail ID", sep = "\n")

# Two option available if password forgotten. 1. retrieve password or 2. change password
def retrieve_or_change_password(mail_id):
    # if mail_id is correct, but password_input mismatches, it shows "Your Password is incorrect, so please try again!!!!"
    print("----------Your Password is incorrect, so please try again!!!!----------")
    print("Two option available if password forgotten. Type 1 or 2. (1. retrieve password or 2. change password)")
    choices = str(input("Type any one of the number mentioned above to make decision: "))

    # If the user input is '1', it means that the user decided to retrieve the password.
    # To retrieve the password, the user have input of E-mail ID.
    if choices == '1':
        mail_id_input = str(input("You decided to retrieve your password, so please enter your E-mail ID here: "))
        mail_id_input = standard_format(mail_id_input)

        with open("Task_1.json", "r") as f:
            result = json.load(f)

        if mail_id in result:
            retrieved_password = result[mail_id_input]
            print("Your password is", retrieved_password)
        else:
            print("To retrieve your password, you have give your mail ID correctly or go for Registration. Try again!!!")

    # If the user input is '2', it means that the user decided to change the password.
    # They have to follow the constraints for the password

    elif choices == '2':
        password_1 = str(input("You decided to change the password, enter your new password here: "))
        if len(password_1) >= 5 and len(password_1) <= 16:
            upper_alpha_count, lower_alpha_count, special_char_count, numbers_count = password_validation(password_1)

            # Condition, 2. Uppercase letter, lowercase letter, special character, number.
            # It is mandatory to have all the four type of characters in the password with the count minimum of one each.
            if upper_alpha_count >= 1 and lower_alpha_count >= 1 and special_char_count >= 1 and numbers_count >= 1:
                re_new_password = str(input("Re-enter the new password your entered before : "))

                # For the confirmation, we have to ask one more time to enter the password to validate and change password!!
                # If Both the password were perfectly matches, the password will be changed for that E-mail ID successfully.
                # Else it shows "!!!!!!!!Changing Password Failed. Try again!!!!!!!!"
                if password_1 == re_new_password:
                    with open("Task_1.json", "r") as f:
                        result = json.load(f)

                    result[mail_id] = re_new_password

                    with open("Task_1.json", "w") as f:
                        json.dump(result, f)
                    print("---------Password Changed Successfully-----------")
                else:
                    print("!!!!!!!!Changing Password Failed. Try again!!!!!!!!")
            else:
                print("-----------Invalid password format-----------",
                      "Constraints: ",
                      "1. One number is must", "2. One special character is must", "3. One lowercase alphabet is must",
                      "4. One uppercase alphabet is must", sep="\n")
                print("------------------Reason----------------------")
                if upper_alpha_count < 1:
                    print("One uppercase character is missing in the password you entered")
                if lower_alpha_count < 1:
                    print("One lowercase character is missing in the password you entered")
                if special_char_count < 1:
                    print("One special character is missing in the password you entered")
                if numbers_count < 1:
                    print("One number is missing in the password you entered")
        else:
            print("Length of the password is limited between 5 and 16")

# If this 'login' function called with specified arguments. It checks the login creditial that we get from input, perfectly matches with the Database.
def login_register(mail_id):

    # Here, we are opening the json file. And, the data in the json will be stored in the variable 'result'
    with open("Task_1.json", "r") as f:
        result = json.load(f)

    mail_id = standard_format(mail_id)
    # This block of code checks the input with the database. If correct, log in. Otherwise, it shows message what is the reason for not logging in.
    if mail_id in result:
        password_input = str(input("Enter your password here: "))
        password_in_json = result[mail_id]
        if password_input == password_in_json:
            # if mail_id and password_input perfectly matches, it shows "Logged in Successfully"
            print("----------Logged in Successfully-----------")
        else:
            # Call this function to make some decisions, if password were forgotten
            retrieve_or_change_password(mail_id)

    elif mail_id not in result:
        # if mail_id not in database, it shows "Sign Up/ Register before log in!!!!"
        print("----------Sign Up/ Register before log in!!!!----------")
        check_mail_id(mail_id)

# Main method
if __name__ == "__main__":
    print("-----------------------------------------")

    # First get E-mail Id as input from the user
    mail_id = str(input("Enter your main ID: "))

    # Calling a function by passing argument 'mail_id'
    login_register(mail_id)
