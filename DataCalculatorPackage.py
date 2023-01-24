from datetime import date, timedelta

class data_calculator_class:
    def data_calculator():
        firstDate = date(2023, 1, 1)
        todayDate = date.today()
        passedDays = todayDate - firstDate + timedelta(days=1)
        print(passedDays.days)
        return passedDays.days
    
if __name__ == '__main__':
    data_calculator_class.data_calculator()