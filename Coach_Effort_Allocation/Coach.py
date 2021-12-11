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

# --------------------------------------------------------------------------------------------------------- 
# Creates a object of temporary schedule, which can be created for a coach multiple time or none at all.
# --------------------------------------------------------------------------------------------------------- 
class TemporarySchedule():
    def __init__(self, date: str, p_coaching: float, m_coaching: float, g_coaching: float) -> object:
        '''
        @param date
        Date in which the temporary schedule overrides the coache's baseline effort allocation.
        
        @param p_coaching
        Personal coaching allocation.
        
        @param m_coaching
        Managing coaching allocation.
        
        @param g_coaching
        Group coaching allocation.
        '''
        self.temp_date = date
        self.t_p_coaching = p_coaching
        self.t_m_coaching = m_coaching
        self.t_g_coaching = g_coaching
        

# --------------------------------------------------------------------------------------------------------- 
# Creates an object called coach, which houses functions that define the coache's activity.
# ---------------------------------------------------------------------------------------------------------      
class Coach():
    def __init__(self, name: str, p_coaching: float, m_coaching: float, g_coaching: float) -> object:
        '''
        @param name
        Name of the coach.
        
        @param p_coaching
        Personal coaching allocation.
        
        @param m_coaching
        Managing coaching allocation.
        
        @param g_coaching
        Group coaching allocation.
        '''
        self.name = name
        self.temp_schedule = []
        self.b_p_coaching = p_coaching
        self.b_m_coaching = m_coaching
        self.b_g_coaching = g_coaching 
        
    # A coach can have one or more temporary schedules and to account for that, the set_temp_schedule
    # method creates one or more temporay schedule object.
    def set_temp_schedule(self, date: str, p_coaching: float, m_coaching: float, g_coaching: float) -> list:
        '''
        @param date
        Date in which the temporary schedule overrides the coache's baseline effort allocation.
        
        @param p_coaching
        Personal coaching allocation.
        
        @param m_coaching
        Managing coaching allocation.
        
        @param g_coaching
        Group coaching allocation.
        '''
        
        # Creates the temporary schedule object by passing the coach's temp schedule date,
        # and the coaching allocations.
        schedule = TemporarySchedule(date, p_coaching, m_coaching, g_coaching)
        temp = []
        
        temp.append(schedule.temp_date)
        temp.append(schedule.t_p_coaching)
        temp.append(schedule.t_m_coaching)
        temp.append(schedule.t_g_coaching)
        
        self.temp_schedule.append(temp)
        
    # Calculates the coach's effort allcoation report based on the inputs.         
    def calc_report(self, start_date, end_date):
        '''
        @param start_date
        The start date to generate the effort allocation report for the coach.
        
        @param end_date
        The end date to generate the effort allocation report for the coach.
        '''
        
        # If there is no temporary schedule for a coach, the base line is 
        # presented in the report.
        if len(self.temp_schedule) == 0:
            print('Report: ' + start_date + ' through ' + end_date)
            print('personal: ' + "{:.0%}".format(self.b_p_coaching))
            print('managing: ' + "{:.0%}".format(self.b_m_coaching))
        
        # If there is only one temporary schedule for a coach, the average
        # of the baseline and the one temporary schedule is taken.
        elif len(self.temp_schedule) == 1:
            avg_p_coaching = mean([self.b_p_coaching, self.temp_schedule[0][1]])
            avg_m_coaching = mean([self.b_p_coaching, self.temp_schedule[0][2]])
            print('Report: ' + start_date + ' through ' + end_date)
            print('personal: ' + "{:.0%}".format(avg_p_coaching))
            print('managing: ' + "{:.0%}".format(avg_m_coaching))
            
        # If there are multiple temporary schedule for a coach, the average
        # of the baseline and the multiple temporary schedule is taken.
        else:
            # Empty lists to store the personal coaching allcoation and the
            # managing coaching allocations.
            p_coaching_list = []
            m_coaching_list = []
            
            # Iterates through the multiple temporary schedule.
            for index in range(len(self.temp_schedule)):
                p_coaching_list.append(self.temp_schedule[index][1])
                m_coaching_list.append(self.temp_schedule[index][2])
            
            # Adds the baseline personal coaching and managing allocation
            # which is used to create an average/mean effort percentage.
            p_coaching_list.append(self.b_p_coaching)
            m_coaching_list.append(self.b_m_coaching)
            
            avg_p_coaching = mean(p_coaching_list)
            avg_m_coaching = mean(m_coaching_list)
                
            print('Report: ' + start_date + ' through ' + end_date)
            print('personal: ' + "{:.0%}".format(avg_p_coaching))
            print('managing: ' + "{:.0%}".format(avg_m_coaching))
            

    
             
# Main executable program.      
if __name__ == '__main__':
    
    # Attributes of one coach and it's baseline.
    coach1 = Coach('Ashish', .50, .50, 0)  
     
    # Assigns a temporary schedule to the same coach.
    coach1.set_temp_schedule('2021-10-15', 1, 0, 0)
    
    # For testing purposes, I passed multiple temporary schedules.
    #coach1.set_temp_schedule('2021-10-20', .25, .25, .5)
    #coach1.set_temp_schedule('2021-10-25', .50, .25, .25)
    
    # Generates the effort allocation report.
    coach1.calc_report('2021-10-14', '2021-10-15')
        
    
