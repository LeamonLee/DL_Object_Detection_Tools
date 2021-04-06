
with open("text.txt", "r") as f_r:
  lines = f_r.readlines()
  modifyLine = ""
  modifyIdx = 0
  for line in lines:
    seekIdx = len(line) - 1
    print("seekIdx:", seekIdx)
    modifyLine = line[0:seekIdx] + "789" + line[-1:]
    break
  
  with open("text.txt", "w") as f_w:
      # f_w.seek(0)
      
      lines[modifyIdx] = modifyLine
      contents = "".join(lines)
      f_w.write(contents)

# with open("text.txt", "w") as f_w:
#     f_w.write("123\n")
#     f_w.write("456\n")
    
#     # f_w.write("123")
#     # f_w.write("456")

with open("text.txt", "r") as f_r:
    lines = f_r.readlines()
    print("lines:", lines)
    for line in lines:
        print(line)
        # print("lenth of line", len(line))