


def calculate_weeks_pay(hours, hourly_pay):
    '''calcualtes the weeks pay
    
       Assumes that a 10% of the gross pay will be taken for the payments of taxes
       
       Parameters
       ----------
       hours : float
           the number of hours worked for the week
        hourly_pay : float
           the hourly payment
           
        Returns
        ---------
        float
           the net pay expected'''
        
    gross_pay = hours * hourly_pay
    net_pay = gross_pay * 0.90
    return net_pay

net_pay, gross_pay = calculate_weeks_pay(34.5, 16.25)

print('Your net pay is $'), "{:.2f}".format(net_pay)
print('Your gross pay pay is $'), "{:.2f}".format(gross_pay)