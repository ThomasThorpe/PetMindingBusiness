#Thomas Thorpe
#Pet Service System Validation Checking

import re
from datetime import datetime

from PetServiceDatabase import * #used when checking availability

#the value "-1" has be used if there is no validation error, when returned pervious window will not append this value
#other validations such as nothing entered I deemed too short code to be worth moving to this module and calling, wouldn't cut down on lines of code

def CheckPostcode(postcode):
    postcode_pattern = "[A-Z]([A-Z](\d{1,2}|\d[A-Z])|\d{1,2})\s\d[A-Z]{2}"
    if len(postcode) < 6:
        return("The postcode is not the right length")
    else:
        if re.match(postcode_pattern, postcode):
            return ("-1")
        else:
            return("The postcode is not a valid postcode")

def CheckMobileNumber(mobile_number):
    mobile_pattern = "^(07[\d]{8,12}|447[\d]{7,11})$"
    if re.match(mobile_pattern, mobile_number):
        return ("-1")
    elif len(mobile_number) < 10:
        return("The mobile number is too short")
    else:
        return("The mobile number is not valid")

def CheckHomeNumber(home_number):
    home_pattern = "^\s*\(?(020[78]?\)? ?[1-9][0-9]{2,3} ?[0-9]{4})|(0[1-8][0-9]{3}\)? ?[1-9][0-9]{2} ?[0-9]{3})\s*$"
    if re.match(home_pattern, home_number):
        return("-1")
    elif len(home_number) < 11:
        return("The home phone number is too short")
    else:
        return("That is not a valid home phone number")

def CheckEmailAddress(email_addr):
    email_pattern = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    if re.match(email_pattern, email_addr):
        return("-1")
    else:
        return("The email address is not valid")

def CheckPetDob(date):
    try:
        datetime.strptime(date, "%d/%m/%Y")
        if date[2] != "/" or date[5] != "/":
            return("The date of birth was the incorrect format, eg 8 should be 08 ")
        return ("-1")
    except ValueError:
        if date != "":
            return("The date of birth was the incorrect format")
        else:
            return("Nothing was entered for date of birth")

def CheckJobDatesTimes(start_date, end_date, start_time_1, start_time_2, end_time_1, end_time_2):
    check_results = []
    try:
        datetime.strptime(start_date, "%d/%m/%Y")
        if start_date[2] != "/" or start_date[5] != "/":
            check_results.append("The start date was the incorrect format, eg 8 should be 08 ")
            compare_dates = False
        else:
            compare_dates = True
    except ValueError:
        if start_date != "":
            check_results.append("The start date was the incorrect format")
        else:
            check_results.append("Nothing was entered for an start date")
        compare_dates = False

    try:
        datetime.strptime(end_date, "%d/%m/%Y")
        if end_date[2] != "/" or end_date[5] != "/":
            check_results.append("The end date was the incorrect format, eg 8 should be 08 ")
        if compare_dates: #variable to make sure they are the correct format before continuing to compare them
            if end_date < start_date: #check end date is after start date
                check_results.append("The end date must be later than the start date")
    except ValueError:
        if end_date != "":
            check_results.append("The end date was the incorrect format")
        else:
            check_results.append("Nothing was entered for an end date")

    try:
        datetime.strptime(start_time_1, "%H:%M")
        if start_time_1[2] != ":" or len(start_time_1) != 5:
            check_results.append("Start Time 1 is not in the right format")
            compare_times_1 = False
        else:
            compare_times_1 = True
    except ValueError:
        if start_time_1 != "":
            check_results.append("Start Time 1 is not in the right format")
        else:
            check_results.append("Nothing was entered for start time 1")
        compare_times_1 = False

    try:
        datetime.strptime(end_time_1, "%H:%M")
        if end_time_1[2] != ":" or len(end_time_1) != 5:
            check_results.append("End Time 1 is not in the right format")
        if compare_times_1: #variable to make sure they are the correct format before continuing to compare them
            if end_time_1 < start_time_1: #check end times are after start times
                check_results.append("The end time 1 must be later than start time 1")
    except ValueError:
        if end_time_1 != "":
            check_results.append("End Time 1 is not in the right format")
        else:
            check_results.append("Nothing was entered for end time 1")

    try:
        datetime.strptime(start_time_2, "%H:%M")
        if start_time_2[2] != ":" or len(start_time_2) != 5:
            check_results.append("Start Time 2 is not in the right format")
            compare_times_2 = False
        else:
            compare_times_2 = True
    except ValueError:
        if start_time_2 != "N/A" and start_time_2 != "n/a":
            if start_time_2 == "":
                check_results.append("Nothing was entered in start time 2. Did you want \"N/A\" ?")
            else:
                check_results.append("Start Time 2 is not in the right format")
        compare_times_2 = False

    try:
        datetime.strptime(end_time_2, "%H:%M")
        if end_time_2[2] != ":" or len(end_time_2) != 5:
            check_results.append("End Time 2 is not in the right format")
        if compare_times_2: #variable to make sure they are the correct format before continuing to compare them
            if end_time_2 < start_time_2: #check end times are after start times
                check_results.append("The end time 2 must be later than start time 2")
    except ValueError:
        if end_time_2 != "N/A" and end_time_2 != "n/a":
            if end_time_2 == "":
                check_results.append("Nothing was entered in end time 2. Did you want \"N/A\" ?")
            else:
                check_results.append("End Time 2 is not in the right format")
    return(check_results)

def CheckAvailability(start_date, end_date, start_time, end_time, edit_flag, record_id):
    #transforming paras to datetime objects
    start_date_unformat = start_date
    day = int(start_date_unformat[0:2])
    month = int(start_date_unformat[-7:-5])
    year = int(start_date_unformat[-4:])
    start_date_g = datetime(year,month,day)

    end_date_unformat = end_date
    day = int(end_date_unformat[0:2])
    month = int(end_date_unformat[-7:-5])
    year = int(end_date_unformat[-4:])
    end_date_g = datetime(year,month,day)

    start_time_g = datetime.strptime(start_time, "%H:%M").time()
    end_time_g = datetime.strptime(end_time, "%H:%M").time()

    #getting info to check against
    if edit_flag:
        sql = """SELECT StartDate, EndDate, StartTime1, EndTime1, StartTime2, EndTime2 FROM Jobs WHERE InvoiceSent = 0 AND JobID !={0} """.format(record_id)
    else:
        sql = """SELECT StartDate, EndDate, StartTime1, EndTime1, StartTime2, EndTime2 FROM Jobs WHERE InvoiceSent = 0"""
    unformated_data = database.FetchAllResult(sql)

    formated_data = [] #will contain all datetime objects
    for each in unformated_data: #making datetime objects
        temp_record = []
        start_date_unformat = each[0]
        day = int(start_date_unformat[0:2])
        month = int(start_date_unformat[-7:-5])
        year = int(start_date_unformat[-4:])
        start_date = datetime(year,month,day)
        temp_record.append(start_date)

        end_date_unformat = each[1]
        day = int(end_date_unformat[0:2])
        month = int(end_date_unformat[-7:-5])
        year = int(end_date_unformat[-4:])
        end_date = datetime(year,month,day)
        temp_record.append(end_date)

        start_time_1_unformat = each[2]
        start_time_1 = datetime.strptime(start_time_1_unformat, "%H:%M").time()
        temp_record.append(start_time_1)

        end_time_1_unformat = each[3]
        end_time_1 = datetime.strptime(end_time_1_unformat, "%H:%M").time()
        temp_record.append(end_time_1)

        if each[4] != "N/A" or each[5] != "N/A":
            start_time_2_unformat = each[4]
            start_time_2 = datetime.strptime(start_time_2_unformat, "%H:%M").time()
            temp_record.append(start_time_2)

            end_time_2_unformat = each[5]
            end_time_2 = datetime.strptime(end_time_2_unformat, "%H:%M").time()
            temp_record.append(end_time_2)
        else:
            temp_record.append(each[4])
            temp_record.append(each[5])

        formated_data.append(temp_record)

    #checking for if available
    ##check if dates collide, if so then check times_1, if not check times_2 also, exlcuding "N/A"
    for each in formated_data:
        if (start_date_g <= each[1] and start_date_g >= each[0]) or (end_date_g <= each[1] and end_date_g >= each[0]) or (start_date_g < each[0] and end_date_g > each[1]):
            if (start_time_g <= each[3] and start_time_g >= each[2]) or (end_time_g <= each[3] and end_time_g >= each[2]) or (start_time_g < each[2] and end_time_g > each[3]):
                return("There is already a job at this time.")
            else:
                if each[4] != "N/A"  and each[5] != "N/A":
                    if (start_time_g <= each[5] and start_time_g >= each[4]) or (end_time_g <= each[5] and end_time_g >= each[4]) or (start_time_g < each[4] and end_time_g > each[5]):
                        return("There is already a job at this time")
    return(-1)

def CheckTimeslots(start_time_1, end_time_1, start_time_2, end_time_2, job_name):
    start_time_1 = datetime.strptime(start_time_1, "%H:%M")
    end_time_1 = datetime.strptime(end_time_1, "%H:%M")


    time_diff_1 = str(end_time_1 - start_time_1)
    if start_time_2 != "N/A" and end_time_2 != "N/A":
        start_time_2 = datetime.strptime(start_time_2, "%H:%M")
        end_time_2 = datetime.strptime(end_time_2, "%H:%M")
        time_diff_2 = str(end_time_2 - start_time_2)
    else:
        time_diff_2 = "N/A"

    #checking half hours
    if job_name == "Dog Walking - Single Half Hour" or job_name == "Dog Walking - 2 For Half Hour" or job_name == "Dog Walking - 3 For Half Hour" or job_name == "Pet Sitting - Half Hour A Day":
        if time_diff_1 == "0:30:00" and time_diff_2 == "N/A":
            return(-1)
        else:
            return("The time slot wasn't half an hour") 
    #checking hours
    elif job_name == "Dog Walking - Single 1 Hour" or job_name == "Dog Walking - 2 For 1 Hour" or job_name == "Dog Walking - 3 For 1 Hour" or job_name == "Pet Sitting - Hour A Day":
        if time_diff_1 == "1:00:00" and time_diff_2 == "N/A":
            return(-1)
        else:
            return("The time slot wasn't an hour")
    #animal boarding
    elif job_name == "Animal Boarding - Dog" or job_name == "Animal Boarding - Small Animal" or job_name == "Animal Boarding - Birds":
        if start_time_2 != "N/A" or end_time_2 != "N/A":
            return("You cannot have a second set of times for animal boarding")
        else:
            return(-1)
    #two half hours
    elif job_name == "Pet Sitting - Hour A Day (Two Half Hours)":
        if time_diff_1 == "0:30:00" and time_diff_2 == "0:30:00":
            return(-1)
        else:
            return("One of the time slots wasn't half an hour")
    #hour + half
    elif job_name == "Pet Sitting - Hour And Half A Day":
        if (time_diff_1 == "0:30:00" and time_diff_2 == "1:00:00") or (time_diff_1 == "1:00:00" and time_diff_2 == "0:30:00"):
            return(-1)
        else:
            return("The two sessions didn't total 1.5 hours")
    #two hours
    elif job_name == "Pet Sitting - Two Hours A Day":
        if time_diff_1 == "1:00:00" and time_diff_2 == "1:00:00":
            return(-1)
        else:
            return("One of the sessions wasn't an hour")
     