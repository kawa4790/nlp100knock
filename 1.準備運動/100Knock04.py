# 04.元素記号
dic = {}
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s = s.replace(".", "")
s = s.split()
nums = {1, 5, 6, 7, 8, 9, 15, 16, 19}
for i in range(len(s)):
  if i + 1 in nums:
    dic[s[i][0]] = i+1
  else:
    dic[s[i][:2]] = i+1
print(dic)