nric = input('Enter an NRIC number: ')

# Type your code below
weight = [0,2,7,6,5,4,3,2]
sum = 0
valid = True
for i in range(1,8):
  if not nric[i].isdigit():
    valid = False
    break
  sum += int(nric[i]) * weight[i]

if nric[0] == 'T' or nric[0] == 'G':
  sum += 4
sum %= 11
st_check = "JZIHGFEDCBA"
fg_check = "XWUTRQPNMLK"
if nric[0] == 'S' or nric[0] == 'T':
  if st_check[sum] != nric[-1]:
    valid = False
elif nric[0] == 'F' or nric[0] == 'G':
  if fg_check[sum] != nric[-1]:
    valid = False
else:
  valid = False

if valid:
  print("NRIC is valid.")
else:
  print("NRIC is invalid.")