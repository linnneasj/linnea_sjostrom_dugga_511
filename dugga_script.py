#import libraries need for the tasks
import csv
import pandas as pd
import matplotlib.pyplot as plt

###Part 1###

numbers = [15, -5, -12, 7, 10, -7, 3, -10, 4] #create the list of numbers

#a)
sum_absolut = 0 #creates empty variable to store the sum
for num in numbers: #iterate over numbers in the list 
    val = abs(num) #get the absolute value of num. Used AI to help me understand the abs() function. Understand that the absolute value of num is save as the varible val. To check that it the code was working I counted the values >= 10 in the list.
    if val >= 10: #checks if value is greater or equal to 10
        sum_absolut += val #adds number to sum_absolut 
print(sum_absolut) #print variable
print("\n") #empty line

#b)
cube_numbers = [] #crete empty list to store the cubes of the negative numbers
for num in numbers: #iterate over numbers in the list
    if num < 0: #checks if number is negative
        cube_numbers.append(num**3) #calculates the cube of of num and append it to the list
print(cube_numbers) #prints list of cubes
print("\n") 

#c)
seen = [] #create empty list to store seen absolute values
first_repeat = None #variable to store the first repeated absolute value
for num in numbers: 
    val = abs(num)  #get get the absolute value of num
    if val in seen: #checks if the absolute value have been seen before
        first_repeat = val #stores the first repeated value
        break #stop loop
    else:
        seen.append(val) #append the first absolute value in the seen list
print(first_repeat if first_repeat is not None else "No repeats")
print("\n")

###Part 2###
#2.1
df = pd.read_csv('brca_head500_genes.csv', sep=',') #reads the csv file and store it as a data frame + adds separator as comma

#2.2.1/2.3
def histo_plot(): #creates function to plot histogram
    plt.hist(df['fpkm_log2'], bins=40, color='blue') #create histogram of the fpkm_log2 column in the data frame (df) saved in task #2.1
    plt.xlabel('Expression') #label x-axis
    plt.ylabel('Number of genes') #label y-axis
    plt.title('Distribution of gene expression') #title of the plot
    plt.savefig('fpkm_distribution.png') #save figure
    #plt.show() #shows the plot

#2.2.2
histo_plot() #call the function to plot the histogram










