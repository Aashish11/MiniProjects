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

base_coaching_alloc = {'Ashish': [.50, .50, 0]}
temp_coaching_alloc = {'Ashish': [0, 1, 0]}


def calc_report(start_date, end_date, coach, base_allocation, temp_allocation):
    
    if start_date == '2021-10-15' or end_date == '2021-10-15':        
        avg_p_coach_alloc = mean([base_allocation[coach][0], temp_allocation[coach][0]])
        avg_m_coach_alloc = mean([base_allocation[coach][1], temp_allocation[coach][1]])
        avg_g_coach_alloc = mean([base_allocation[coach][2], temp_allocation[coach][2]])
    else:
        avg_p_coach_alloc = base_allocation[coach][0]
        avg_m_coach_alloc = base_allocation[coach][1]
        avg_g_coach_alloc = base_allocation[coach][2]
        
    return [avg_p_coach_alloc, avg_m_coach_alloc, avg_g_coach_alloc]
        
    

if __name__ == '__main__':
    report = []
    results = calc_report(start_date, end_date, 'Ashish', base_coaching_alloc, temp_coaching_alloc)
    report.append(results)
    
    print("report: " + start_date + ' through ' + end_date)
    print('personal: ' + "{:.0%}".format(report[0][0]))
    print('managing: ' + "{:.0%}".format(report[0][1]))