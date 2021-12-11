'''
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

start_date = '2021-10-14'
end_date = '2021-10-15'

def get_coaching_percentage(name):
    b_coaching_list = [.50, .50, 0]
    t_coaching_list = [0, 1, 0]
    
    coaching_percentage = [b_coaching_list, t_coaching_list]
    
    return coaching_percentage

def calc_report(start_date, end_date):
    allocation = get_coaching_percentage('test name')
    
    if start_date == '2021-10-15' or end_date == '2021-10-15':        
        avg_p_coach_alloc = mean([allocation[0][0], allocation[1][0]])
        avg_m_coach_alloc = mean([allocation[0][1], allocation[1][1]])
        avg_g_coach_alloc = mean([allocation[0][2], allocation[1][2]])
    else:
        avg_p_coach_alloc = allocation[0][0]
        avg_m_coach_alloc = allocation[0][1]
        avg_g_coach_alloc = allocation[0][2]
        
    return [avg_p_coach_alloc, avg_m_coach_alloc, avg_g_coach_alloc]
        
    

if __name__ == '__main__':
    results = calc_report(start_date, end_date)
    
    print("report: " + start_date + ' through ' + end_date)
    print("personal: " + str(results[0] * 100) + '%')
    print('managing: ' + str(results[1] * 100) + '%')