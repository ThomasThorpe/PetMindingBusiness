#Thomas Thorpe
#Pet Service System Filter Jobs For Today

from datetime import datetime

def GetJobsForToday(came_from, unfiltered_data): #used by startup reminder and search current jobs
    if len(unfiltered_data) == 0:
        came_from.PopulateTableView(unfiltered_data)
    else: #compare end_dates with date now, if so add to data to view
        filtered_data = []
        today_str = datetime.today().strftime("%Y/%m/%d")
        today = datetime.strptime(today_str, "%Y/%m/%d")
        for each in unfiltered_data:
            end_date_unformat = each[3]
            day = int(end_date_unformat[0:2])
            month = int(end_date_unformat[-7:-5])
            year = int(end_date_unformat[-4:])
            end_date = datetime(year,month,day)

            start_date_unformat = each[2]
            day = int(start_date_unformat[0:2])
            month = int(start_date_unformat[-7:-5])
            year = int(start_date_unformat[-4:])
            start_date = datetime(year,month,day)

            if end_date >= today and start_date <= today: #compare end date with today date to see if needed
                filtered_data.append(each)

            came_from.PopulateTableView(filtered_data)