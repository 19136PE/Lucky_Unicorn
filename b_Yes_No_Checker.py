#functions Go Here
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        elif response == "creeper":
            print("aww man")

        else:
            print("Invalid Input, Please answer yes / no")

def instuctions():
    print("*** How To Play ***")
    print()
    print("Instructions here")
    print()

#Main Routine Goes Here
show_instrustions = yes_no("Have You Played The Game Before?")
print("you chose {}".format(show_instrustions))

if show_instrustions == "no":
 instuctions()
