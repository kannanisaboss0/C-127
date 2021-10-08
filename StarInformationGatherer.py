#-------------------------------------StarInformationGatherer.py-------------------------------------#

'''
Importing Modules:
-BeautifulSoup :- bs4
-webdriver :- selenium
-csv
-tm (tm)
-sys
'''
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time as tm 
import sys

print('Welcome to StarInformationGatherer.py')
print("We provide collection of data related to stars present in a Wikipedia page.")
print("We then compile the data into a csv or txt file, reaady for usage")
print("The method used to collect is called Scraping")

tm.sleep(3.4)

print("Loading Data...")

tm.sleep(2.7)

file_name=input("Please enter the name of the file to be created:")

#Verifying whether the file name is provided as an extension or not
#Case-1
if "." in file_name:
    file_name_section_1,file_name_section_2=file_name.split(".")
    file_name=file_name_section_1.strip()

extension_list=["unusable_element",".csv",".txt"]

#Running a loop over the list of extensions to show the user th choices
for index,extension in enumerate(extension_list):
    print("{}:{}".format(index,extension))

extension_input=int(input("Please enter the index of the extension desired from the above options."))

user_choice=None

#Verifying the validity of the user's input
#Try block
try:
    user_choice=extension_list[extension_input]
#Except block
except:
    sys.exit("Invalid Input.")   

file_name_extended=file_name+user_choice

url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser=webdriver.Chrome("/Users/kannan/Coding/chromedriver")
browser.get(url)

final_list=[]

tm.sleep(2.3)

#Running a for loop to assess thw number of times to scrape pages
for i in range(1):
    bs=BeautifulSoup(browser.page_source,"html.parser")
    count=0

    tbody_tag=bs.find("tbody")

    #Running a for loop over all tr tags
    for tr_tag in tbody_tag.find_all("tr"):
        star_list=[]

        #Running a for loop over all enumerated td tags within a tr tag
        for td_index,td_tag in enumerate(tr_tag.find_all("td")):

            #Assessing the index of the td tag to conduct further actions
            #Case-1
            if(td_index==0 or td_index==2 or td_index==4):
                None

            #Case-2
            elif (td_index==1):

                #Assessing whetehr the td tag contains an "a" attribute and performing necessary actions
                #Try block
                try:
                    star_list.append(td_tag.find_all("a")[0].contents[0])
                    count+=1
                #Except block
                except:
                    star_list.append(td_tag.contents[0])
                    count+=1
            #Case-3        
            else:
                star_list.append(td_tag.text)
                           
        final_list.append(star_list) 

new_final_list=[] 

#Running a for loop over the final list of star data lists
for star_set in final_list:
    new_star_list=[]

    #Runnning a for loop over each element of the enumerated star lists
    for index,star_set_element in enumerate(star_set):
        
        #Verifying whether each element contains certain characters or not 
        #Case-1
        if "," in star_set_element:
            star_set_element=star_set_element.replace(",", "")
        #Case-2
        if "\n" in star_set_element:
            star_set_element=star_set_element.replace("\n", "")
        #Cae-3
        if "-" in star_set_element:

            #Verifying whether the index is 0 or not
            #Case-1   
            if(index!=0):
                star_set_element_number_1,star_set_element_number_2=star_set_element.split("-")

                star_set_element_number_1_stripped=star_set_element_number_1.strip()
                star_set_element_number_2_stripped=star_set_element_number_2.strip()

                star_set_element_mean=(float(star_set_element_number_1_stripped)+float(star_set_element_number_2_stripped))/2
                star_set_element=star_set_element_mean
       
        new_star_list.append(star_set_element)

    new_final_list.append(new_star_list)


bs_headings=BeautifulSoup(browser.page_source,"html.parser")

th_tags=bs_headings.find_all("th",attrs={"class","headerSort"})  

header_list=[]

#Running a for loop over the enumerated th tags
for index,th_tag in enumerate(th_tags):

    #Verifying whether the index of the th tag is not 0,2 and 4
    #Case-1
    if(index!=0 and index!=2 and index!=4):
        th_tag_replaced=th_tag.text.replace("\n","")
        header_list.append(th_tag_replaced)
    
#Opening (Creating) a file with the name that of the user's choice
with open(file_name_extended,'w') as g:
    csv.writer(g).writerow(header_list)
    csv.writer(g).writerows(new_final_list)

#-------------------------------------StarInformationGatherer.py-------------------------------------#    