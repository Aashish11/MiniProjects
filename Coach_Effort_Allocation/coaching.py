'''
@author: Ashish Singh
Created on: 2021-12-10

baseline:
    personal: 50%
    managing: 50%
    group: 0%
    
temporary: 2021-10-15
    managing: 100%
    
report: 2021-10-14 through 2021-10-15:
personal: 25%
managing: 75%
'''

from statistics import mean

# Variable to store the start and end date of the report.
start_date = '2021-10-14'
end_date = '2021-10-15'

# Dictionary that stores the coach's employee ID and their baseline and temporary 
# effort allocation.

# Since the dictionary needs unique key, I'm passing the employee ID rather than name,
# which I used on Friday. This way, we can store multiple coaches in the same dictionary
# and if there are coaches with the same name, it won't have an issues with the data structure.
base_coaching_alloc = {123456789: [.50, .50, 0]}
temp_coaching_alloc = {123456789: [0, 1, 0]}


# Function takes on the report start date, end date, the coach's employee ID and their
# base and temporary effort allocation.
def calc_report(start_date, end_date, emplID, base_allocation, temp_allocation) -> list:
    '''
    @param start_date
    The start date to generate the effort allocation report for the coach.
        
    @param end_date
    The end date to generate the effort allocation report for the coach.
    
    @param emplID
    Employee ID of the coach.
    
    @param base_allocation
    Base allocation of the coach.
    
    @param temp_allocation
    Temporary schedule of the coach.
    
    @return list
    A list that has the coach's personal, managing, and group effort allocation.
    '''
    
    # If the date falls the temporary schedule date, it take the average of the 
    # baseline and the temporary schedule.
    if start_date == '2021-10-15' or end_date == '2021-10-15':        
        avg_p_coach_alloc = mean([base_allocation[emplID][0], temp_allocation[emplID][0]])
        avg_m_coach_alloc = mean([base_allocation[emplID][1], temp_allocation[emplID][1]])
        avg_g_coach_alloc = mean([base_allocation[emplID][2], temp_allocation[emplID][2]])
        
    # If the date does not fall temporary schedule date, it then uses the coach's
    # baseline effort allocation.
    else:
        avg_p_coach_alloc = base_allocation[emplID][0]
        avg_m_coach_alloc = base_allocation[emplID][1]
        avg_g_coach_alloc = base_allocation[emplID][2]
        
    return [avg_p_coach_alloc, avg_m_coach_alloc, avg_g_coach_alloc]
        
    
# Main executable code.
if __name__ == '__main__':
    
    # An empty list to store the results of the same coach or other different coaches.
    report = []
    
    # Calls the calc_report function to calculate the personal, managing and group effort allocation.
    results = calc_report(start_date, end_date, 123456789, base_coaching_alloc, temp_coaching_alloc)
    
    # Adds the results to the report list, which will be used to print.
    report.append(results)
    
    print("report: " + start_date + ' through ' + end_date)
    print('personal: ' + "{:.0%}".format(report[0][0]))
    print('managing: ' + "{:.0%}".format(report[0][1]))