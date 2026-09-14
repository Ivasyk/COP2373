#This program sells tickets with a limit of 4 per person to customers until a total of 20 tickets is reached. After
#reaching 20 tickets the program outputs an accumulation of how many orders were placed(customers)

def main():
    #initialized accumulators
    tickets = 10
    fools = 0

    #while loop takes orders until there are no tickets left
    while True:
        #nested while loop used to force user to input valid data for order variable to stop code from breaking
        while True:
            try:
                order = int(input('We have ' + str(tickets) + ' tickets available with a limit of 4 per person. How many tickets you wanna buy fool?'))
            except ValueError:
                print('Please enter a number')
            else:
                break

        #if statements deal with unacceptable user inputs, when the user inputs an acceptable value, accumulators are updated
        if order > 4:
            print('There is a limit of 4 tickets per person. Please place an order of only up to 4 tickets')
        elif tickets - order <0:
            print('There are only' , tickets , 'tickets available')
        elif order == 0:
            print('Please place an order of at least 1 ticket')
        else:
            tickets = tickets - order
            fools += 1
            print('There are', tickets, 'tickets remaining')
            False

        #terminates function after reaching desired outcome
        if tickets == 0:
            #output required by coding overlords, also terminates function
            return fools

#second function required by coding overlords, only serves the purpose of printing output from main function
def returnvalues(main):
    print('There are', main() , 'customers')

#run second function with main function as an argument
returnvalues(main)