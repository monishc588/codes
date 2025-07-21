# 1 - ask the user for their full name and print only the first name using slicing and indexing

# name = input("enter the full name :")
# first_name = name[:name.find(" ")]
# print("your first name is :", first_name)

#2 - Take the user's input for a city name and print it in uppercase, lowercase, and title case

# city = input("enter the city name: ")
# print(city.upper())
# print(city.lower())
# print(city.title())

#3 - Print the reversed version of the string 'Technology' using slicing.

# a = "technology"
# print(a[::-1])

#4 -  Combine the strings 'Data' and 'Science' with a hyphen and display the result.

# a = "data"
# b = "science"
# c = ( a + "-" + b)
# print(c)

#5 -  Ask the user for a product price and display it formatted as currency with two decimal places.

# price = float(input("enter the product price :"))
# print(f"${price:.2f}")

#6 - Store your name and age in variables, then print a sentence using f-string formatting.

# name = "monish"
# age = 20
# print(f"hello {name} are you {age} years old")

#7 - Check if the word 'Python' is present in the sentence 'Python is awesome' and print the result.
 
# a = "python is awesome"
# print("python" in a)

#8 - Ask the user for a sentence and display how many characters it contains (excluding leading/trailing spaces)


# sentence = input("Enter a sentence: ")
# char_count = len(sentence.strip())
# print(f"The sentence contains {char_count} characters (excluding leading/trailing spaces).")

#9 - Use assignment operators to add tax (5%) to a product price of 200 and print the final price.

# a = 200
# a += a *0.05
# print(f" the final price {a:.2f}")

#10 - Given name = 'Alice', print whether the character 'i' is in the name and also if 'z' is not.

# name = "alice"
# print( "i" in name)
# print("z" not in  name)

#11 -  Use arithmetic operators to calculate and print the average of three user-provided test scores.

# a = float(input("enter the 1 st score : "))
# b = float(input("enter the 2 nd score : "))
# c = float(input("enter the 3 rd score : "))
# print((a+b+c)//3)

#12 -. Ask the user for their height in meters and weight in kilograms, then calculate and print their BMI (Body Mass Index).

# height = float(input("enter the height in meters : "))
# weight = float(input("enter the weight in kilograms : "))
# bmi = weight/(height**2)
# print(f"the bmi is {bmi:.2f}")

#13 -  Create a string 'I love Python!' and print the word 'love' using slicing

# sentence = 'i love python!'
# a = sentence[2:6]
# print(a)

#14 - Use string methods to replace 'bad' with 'good' in the sentence 'This is a bad idea.' and print the result

# sentence = "this is a bad idea"
# a = sentence.replace("bad","good")
# print(a)

#15 - Create two variables a = 1000 and b = 1000, then check and print if a is b (identity operator)

# a = 100
# b = 100
# print( a is b)
