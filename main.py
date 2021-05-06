#ask user if they have played before
show_instructions=input("Have You Played This Game Before?").lower()

#if yes, 'program continues'
if show_instructions == "yes":
  print("program continues")

elif show_instructions == "y":
  print("program continues")

#if no, 'print instructions'
elif show_instructions == "no":
  print("Print Instructions")

elif show_instructions == "n":
  print("Print Instructions")

#if invalid, 'send error message'
else:
  print("Please Answer Yes/No")
