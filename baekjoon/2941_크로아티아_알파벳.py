alpha_dict = {"c=": 1, "c-": 1, "dz=": 1, "d-": 1, "lj": 1, "nj": 1, "s=": 1, "z=": 1}
count = 0
pointer = 0

input_string = input()

while pointer < len(input_string):
  if alpha_dict.get(input_string[pointer]):
    pass
  if pointer<=len(input_string)-2  and alpha_dict.get(input_string[pointer:pointer+2]):
    pointer += 1
  elif pointer<=len(input_string)-3 and alpha_dict.get(input_string[pointer:pointer+3]):
    pointer += 2
  else:
    pass
  count +=1
  pointer += 1

print(count)