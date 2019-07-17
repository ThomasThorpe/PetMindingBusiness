#Thomas Thorpe
#Pet Service Make Summary Information Class

from PetServiceDatabase import *
import re

def CreateSummary(record_id):
    #getting customer details
    sql = """SELECT CustomerID FROM "Jobs" WHERE JobID={0}""".format(record_id)
    data = database.FetchOneResult(sql)
    customer_id = data[0]

    sql = """SELECT FirstName, LastName, Addr1, Addr2, Addr3, Addr4, PostCode FROM "Customer" WHERE CustomerID={0}""".format(customer_id)
    customer_details = database.FetchOneResult(sql)

    #getting details required to format summary
    sql = """SELECT JobType, StartDate, EndDate FROM "Jobs" WHERE JobID={0}""".format(record_id)
    data = database.FetchOneResult(sql)
    job_type = data[0]
    start_date = data[1]
    end_date = data[2]

    #getting dates
    start_date_compare = datetime.strptime(start_date, "%d/%m/%Y")
    end_date_compare = datetime.strptime(end_date, "%d/%m/%Y")

    #regex to check job type
    dog_walking_pattern = "Dog Walking"
    pet_stting_pattern = "Pet Sitting"

    if re.match(dog_walking_pattern, job_type): #formatting summary for dog walks
        summary_number = end_date_compare - start_date_compare #get number of days
        summary_number = summary_number.days
        if summary_number != 1:
            summary_word = "walks"
        else:
            summary_word = "walk"

    elif re.match(pet_stting_pattern, job_type): #formatting summary for pet sitting
        if job_type == "Pet Sitting - Hour A Day (Two Half Hours)" or job_type == "Pet Sitting - Two Hours A Day" or job_type == "Pet Sitting - Hour And Half A Day":
            x = end_date_compare - start_date_compare
            days = x.days
            summary_number = days * 2
        else:
            summary_number = end_date_compare - start_date_compare #get number of days
            summary_number = summary_number.days

        if summary_number != 1:
            summary_word = "visits"
        else:
        	summary_word = "visit"

    else: #formatting for animal boarding
        summary_number = end_date_compare - start_date_compare #get number of days
        summary_number = summary_number.days
        if summary_number != 1:
            summary_word = "days boarded"
        else:
            summary_word = "day boarded"

    total_cost = WorkOutCost(record_id, summary_number)

    return (customer_details, summary_number, summary_word, start_date, end_date, total_cost) #return required informaion

def WorkOutCost(record_id, summary_number): #working out total cost algorithm from design
    sql = """SELECT JobType FROM Jobs WHERE JobID={0}""".format(record_id)
    data = database.FetchOneResult(sql)
    job_type = data[0]

    sql = """SELECT Price FROM Prices"""
    prices_information = database.FetchAllResult(sql)

    if job_type == "Dog Walking - Single 1 Hour":
        total_cost = summary_number * prices_information[0][0]
    elif job_type == "Dog Walking - Single Half Hour":
        total_cost = summary_number * prices_information[1][0]
    elif job_type == "Dog Walking - 2 For 1 Hour":
        total_cost = summary_number * prices_information[2][0]
    elif job_type == "Dog Walking - 2 For Half Hour":
        total_cost = summary_number * prices_information[3][0]
    elif job_type == "Dog Walking - 3 For 1 Hour":
        total_cost = summary_number * prices_information[4][0]
    elif job_type == "Dog Walking - 3 For Half Hour":
        total_cost = summary_number * prices_information[5][0]
    elif job_type == "Animal Boarding - Dog":
        total_cost = summary_number * prices_information[6][0]
    elif job_type == "Animal Boarding - Small Animal":
        total_cost = summary_number * prices_information[7][0]
    elif job_type == "Animal Boarding - Birds":
        total_cost = summary_number * prices_information[8][0]
    elif job_type == "Pet Sitting - Half Hour A Day":
        total_cost = summary_number * prices_information[9][0]
    elif job_type == "Pet Sitting - Hour A Day":
        total_cost = summary_number * prices_information[10][0]
    elif job_type == "Pet Sitting - Hour A Day (Two Half Hours)":
        total_cost = summary_number * prices_information[11][0]
    elif job_type == "Pet Sitting - Hour And Half A Day":
        total_cost = summary_number * prices_information[12][0]
    elif job_type == "Pet Sitting - Two Hours A Day":
        total_cost = summary_number * prices_information[13][0]

    total_cost = total_cost / 100 #change from pennies to pound.pennies
    return total_cost