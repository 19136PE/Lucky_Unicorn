#functions Go Here
error = "Please Enter A Whole Number Between 1 and 10\n"
def num_check(question, low, high):
  valid = False
  while not valid:
    try:
      #ask the question
      response = int(input(question))
      #if the amount is to low / high give
      if low < response <= high:
        return response
      #output error
      else:
        print(error)
    except ValueError:
      print(error)

#Main Routine Goes Here
how_much = num_check("How Much Would You Like To Play With? ", 0, 10)

#print exspenditure
print("You will be spending ${}".format(how_much))