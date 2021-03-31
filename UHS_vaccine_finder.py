from selenium import webdriver
import time
from datetime import datetime, timedelta
import tkinter as tk

#tkinter set up
window = tk.Tk()
greeting = tk.Label(text="Hello, Student Badger Employee!")
L1 = tk.Label(window, text="UW NetID")
L2 = tk.Label(window, text="Password")
L1.place(x=60, y=60)
L2.place(x=60, y=80)
L3 = tk.Label(window, text="Birth Day#")
L4 = tk.Label(window, text="Birth Month#")
L5 = tk.Label(window, text="Birth Year#")
L3.place(x=60, y=00)
L4.place(x=60, y=20)
L5.place(x=60, y=40)

id = tk.Entry(window, text="UW NetID", bd=5)
id.place(x=140, y=60)
password = tk.Entry(window, text="Password", bd=5)
password.place(x=140, y=80)
birth_day = tk.Entry(window, text="Birth Day", bd=5)
birth_month = tk.Entry(window, text="Birth Month", bd=5)
birth_year = tk.Entry(window, text="Birth Year", bd=5)
birth_day.place(x=140, y=00)
birth_month.place(x=140, y=20)
birth_year.place(x=140, y=40)
#show results
def print_result(p_v, date_str):
    if p_v == 0:
        myLabel = tk.Label(window, text='No appointment in the week of ' + date_str)
    if p_v == 1:
        myLabel = tk.Label(window, text="There is an appointment in the week of " + date_str + " go make an appointment!")
    myLabel.pack()
#automates enteries/clicking in UHS portal
def start():
    uwid = id.get()
    passworD = password.get()
    month = str(int(birth_month.get())+1)
    day = str(int(birth_day.get())+1)
    year = str(int(birth_year.get()))
    url = 'https://myuhs.uhs.wisc.edu/login_dualauthentication.aspx'
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    log_in_button = driver.find_element_by_name('cmdStudentDualAuthentication')
    driver.execute_script("arguments[0].click();", log_in_button)
    user_name_entry = driver.find_element_by_name('j_username')
    password_entry = driver.find_element_by_name('j_password')
    user_name_entry.send_keys(uwid)
    password_entry.send_keys(passworD)
    log_in_button = driver.find_element_by_name('_eventId_proceed')
    driver.execute_script("arguments[0].click();", log_in_button)
    time.sleep(15)
    select_month = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/table[1]/tbody/tr/td/select[1]/option['+ month +']')
    select_month.click()
    select_day = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/table[1]/tbody/tr/td/select[2]/option['+ day +']')
    select_day.click()
    year_entry = driver.find_element_by_name('dtDOBYR')
    year_entry.send_keys(year)
    submit_button = driver.find_element_by_name('cmdStandardProceed')
    submit_button.click()
    url = 'https://myuhs.uhs.wisc.edu/appointments_home.aspx'
    driver.get(url)
    schedule_button = driver.find_element_by_name('cmdSchedule')
    schedule_button.click()
    covid_button = driver.find_element_by_name('rbgBranchingPage')
    covid_button.click()
    submit_button = driver.find_element_by_name('cmdProceed')
    submit_button.click()
    does_button = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[1]/td/span/input')
    does_button.click()
    submit_button = driver.find_element_by_name('cmdProceed')
    submit_button.click()
    student_employee_button = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/fieldset/table/tbody/tr[5]/td/span/input')
    student_employee_button.click()
    submit_button = driver.find_element_by_name('cmdProceed')
    submit_button.click()
    student_employee_button = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/span/fieldset/table/tbody/tr[1]/td/span/input')
    student_employee_button.click()
    submit_button = driver.find_element_by_name('cmdProceed')
    submit_button.click()
    submit_button = driver.find_element_by_name('cmdStandardProceed')
    submit_button.click()
    submit_button = driver.find_element_by_name('cmdStandardProceed')
    submit_button.click()
    today = datetime.today()
#try up to 12 weeks
    for i in range(13):
        new_date = today + timedelta(7*(i))
        date_str = new_date.strftime('%Y-%m-%d')
        url = 'https://myuhs.uhs.wisc.edu/appointments_book_list_available.aspx?startDate=' + date_str
        driver.get(url)
        text = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/form/p[2]')
        if text.text == 'No appointments are available for the specified range.':
            p_v = 0
            print_result(p_v, date_str)
        if text.text != 'No appointments are available for the specified range.':
            p_v = 1
            print_result(p_v, date_str)
            break
    return(driver)

btn = tk.Button(window, text="Find Does 1 Appointment", fg='blue', command=start)
btn.place(x=120, y=100)
window.geometry("400x600")
window.title('Badger Vaccine Finder')
window.mainloop()
