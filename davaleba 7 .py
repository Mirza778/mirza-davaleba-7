#მეგობრებო, ქვემოთ კომენტარის სახედ მოცემულია დავალების პირობები. ყოველი ამოცანის ქვეშ დაწერეთ თქვენი პასუხი. პითონ ფაილის ჩამოტვირთვისას დააწერეთ davaleba 7 - elena bliadze.py 
# ოღონდ elena bliadze -ს ნაცვლად თქვენი სახელი და გვარი. გისურვებთ წარმატებას ! ასევე გაითვალისწინეთ მოცემული დავალება ფოლდერით უნდა ატვირთოთ გითჰაბზე და ლინკი კომენტარში დაურთოთ თქვენს მიერ ატვირთულ დავალებას.
#გისურვებთ წარმატებას!

# დაწერე (ჩაფასთე მარჯვნივ(გასწვრივ)) გითჰაბის ლინკი, სადაც ატვირთე შენი ფაილი:  


#1. მომხმარებლის რეგისტრაცია: შექმენი პროგრამა, რომელიც გაატარებს მოხმარებელს რეგისტრაციას დაგჭირდება ფუნქცია:
#register_user (username:str,password:str) , 1 - პარამეტრის სიგრძე მინიმუმ 3, 2 - პარამეტრის მინიმუ 5  წარმატებული რეგისტრაციის გავლის შემთხვევაში დააბრუნოს 
#შესაბამისი მესიჯი. (შენიშვნა: ფუნქციის გამოძახებისას შენ ჩააწოდე ორივე პარამეტრის მნიშვნელობა და არ გამოიყენო input())
# def register_user (username:str,password:str):
#     if len(username)<3:
#         print('სახელი არის პატარა')
#     elif len(password)<5:
#         print("პაროლი მინიმუმ უნდა შეიცავდეს 5 სიმბოლოს")
#     else :
#         print ('თქვენ გაიარეთ რეგისტრაცი')
# print(register_user('mirza','2009'))
# print(register_user('gela','12345'))
#2. კალკულალტორი: შექმენი პროგრამა, რომელიც იქნება მინი კალკულატორი , შემდეგი ოპერატორებისთვის +,-,*,/ :
#ფუნქციის დასახელება calculate(a,b,oper). ფუნქციას, როდესაც შესამოწმებელ რიცხვებს ჩააწოდებთ, ასევე შესაბამისი მესიჯი გამოჰქონდეს.
# print('აორჩიეთ ამ ოპერაციებიდან +,-,*,/')
# def calculate(a,b,oper):
#     if oper == '+':
#         print(a+b)
#     elif oper == '-':
#         print(a-b)
#     elif oper == '*':
#         print(a*b)
#     elif oper == '/':
#         print(a/b)
#     else :
#         print('რაღაც შეცდომა არის')
# print (calculate(10,20,'*'))

#3.გრადუსის კონვერტაცია: შექმენი ფუნქცია, რომელიც გადაგვიყვანს ჩაწოდებულ რიცხვს ფარენჰეითში ცელსიუსის შემთხვევაში და ფარენჰეითის ცელსიუსში :
#ფორმულები : (ცელსიუსი* 9/5) +32, (ფარენჰეითი-32)* (5/9) 
# def gradus(num,oper):
#     if oper == "C" or oper == "c":
#         print("ტემპერატურა ფარენჰტში არის",(num*9/5) + 32)
#     elif oper == "F" or oper == "f":
#         print('ტემპერატურა ცელსიუში არის ',(num-32)*(5/9))
#     else :
#         print('შეცდომა არის')
# print(gradus(10,'c'))
# print(gradus(50,'f'))
        
#4. ფაილის წაკითხვა: შექმენი ფუნქცია, რომელიც წაიკითხავს შენს ფაილს და წაიკითხავს შიგთავსს.
#შენიშვნა ფაილიც სავალდებულოა მოყვეს დავალება, ანუ აგდებთ მოცემულ და txt ფაილებს ფოლდერში.
# def read_file(name):
#     with open (f"{name}.txt","r") as file:
#         print(file.read())
# print(read_file('mirza'))
#5. შეაჯამე ფუნქცის არგსის გამოყენებით , შემდეგი მნიშვნელობები : (100.50, 200.75, 50.25)
# def sum1(*arg):
#     print(sum(arg))
# print(sum1(100.50, 200.75, 50.25))
#6. დაითვალე , მოცემული სიტყვების სიგრძე: ("Workout", "Grocery shopping", "Read", "Cook dinner")  
# words = ("Workout", "Grocery shopping", "Read", "Cook dinner")  
# for word in words:
#     print(len(word))
#7. მოიფიქრე ფუნქცია სადაც გამოიყენებ **kwargs
# def values1(**kwargs):
#     values2 = kwargs.values() 
#     print(len(values2))
# values1( key1='mirza', key2='nino', key3='hi' ) 
#8. გამოითვალე რიცხვების საშუალო მოცემული რიცხვებისთვის: [10, 20, 30, 40]
# a =[10, 20, 30, 40]
# print(sum(a)/len(a))
#9.შექმენი ფუნქცია რომელიც ამოიღებს დუბლიკატებს (მსგავსებს): [1, 2, 2, 3, 4, 4, 5]
# def duplicat_delet (a):
#     return(list(set(a)))
# nums =  [1, 2, 2, 3, 4, 4, 5]
# deleted_nums  =  duplicat_delet(nums)
# print(deleted_nums)
#10. შექმენი შენი საკუთარი მოდული და ნაცნობი მოდულების გამოყენებით, შექმენი შენთვის სასურველი პრპოგრამა.
import math

def calculate_area(radius):
    return math.pi * radius ** 2

print(calculate_area(5))


