is_Male = input("Are you male (True/False): ") == "True"
is_tall = input("Are you tall (True/False): ") == "True"

if is_Male and is_tall:
    print("He is male and tall.")
elif is_Male and not is_tall:
    print("He is male but not tall.")
elif not is_Male and is_tall:
    print("She is female but tall.")
else:
    print("She is female and not tall.")
