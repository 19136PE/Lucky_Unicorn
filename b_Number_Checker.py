#functions Go Here


#Main Routine Goes Here

error = "Please Enter A Whole Number Between 1 and 10\n"

valid = False
while not valid:
  try:
#ask the question
      response = int(input("How Much Would You Like To Play With? "))
#if the amount is to low/to high give
      if 0 < response <= 10:
        print("You Have Asked To Play With ${}".format(response))
#output response
      else:
        print(error)  
  except ValueError:
    print(error)