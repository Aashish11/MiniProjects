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

class TemporarySchedule():
    def __init__(self, date: str, p_coaching: float, m_coaching: float, g_coaching: float) -> object:
        self.temp_date = date
        self.t_p_coaching = p_coaching
        self.t_m_coaching = m_coaching
        self.t_g_coaching = g_coaching
        
        
class Coach():
    def __init__(self, name: str, p_coaching: float, m_coaching: float, g_coaching: float) -> object:
        self.name = name
        self.temp_schedule = []
        self.b_p_coaching = p_coaching
        self.b_m_coaching = m_coaching
        self.b_g_coaching = g_coaching 
        
        
    def set_temp_schedule(self, date: str, p_coaching: float, m_coaching: float, g_coaching: float):
        schedule = TemporarySchedule(date, p_coaching, m_coaching, g_coaching)
        temp = []
        
        temp.append(schedule.temp_date)
        temp.append(schedule.t_p_coaching)
        temp.append(schedule.t_m_coaching)
        temp.append(schedule.t_g_coaching)
        
        self.temp_schedule.append(temp)
                 
    def calc_report(self, start_date, end_date):
        
        if len(self.temp_schedule) == 0:
            print('Report: ' + start_date + ' through ' + end_date)
            print('personal: ' + "{:.0%}".format(self.b_p_coaching))
            print('managing: ' + "{:.0%}".format(self.b_m_coaching))
        elif len(self.temp_schedule) == 1:
            avg_p_coaching = mean([self.b_p_coaching, self.temp_schedule[0][1]])
            avg_m_coaching = mean([self.b_p_coaching, self.temp_schedule[0][2]])
            print('Report: ' + start_date + ' through ' + end_date)
            print('personal: ' + "{:.0%}".format(avg_p_coaching))
            print('managing: ' + "{:.0%}".format(avg_m_coaching))
        else:
            p_coaching_list = []
            m_coaching_list = []
            
            for index in range(len(self.temp_schedule)):
                p_coaching_list.append(self.temp_schedule[index][1])
                m_coaching_list.append(self.temp_schedule[index][2])
            
            p_coaching_list.append(self.b_p_coaching)
            m_coaching_list.append(self.b_m_coaching)
            
            avg_p_coaching = mean(p_coaching_list)
            avg_m_coaching = mean(m_coaching_list)
                
            print('Report: ' + start_date + ' through ' + end_date)
            print('personal: ' + "{:.0%}".format(avg_p_coaching))
            print('managing: ' + "{:.0%}".format(avg_m_coaching))
            

    
             
        
if __name__ == '__main__':
    coach1 = Coach('Ashish', .50, .50, 0)   
    coach1.set_temp_schedule('2021-10-15', 1, 0, 0)
    coach1.set_temp_schedule('2021-10-20', .25, .25, .5)
    coach1.set_temp_schedule('2021-10-25', .50, .25, .25)
    coach1.calc_report('2021-10-14', '2021-10-15')
        
    
