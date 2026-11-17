def decode_str(s):
  num_stack = []
  str_stack = []

  current_str = ""
  current_num = 0

  for char in s:
    if char.isdigit():
      current_num = current_num * 10 + int(char)
    elif char == "[":
      num_stack.append(current_num)
      str_stack.append(current_str)
      current_str = ""
      current_num = 0
    elif char == "]":
      num = num_stack.pop()
      prev_str = str_stack.pop()
      current_str = prev_str+current_str * num
    else:
      current_str +=char
  return current_str

print(decode_str("2[abc]3[cd]ef"))
      