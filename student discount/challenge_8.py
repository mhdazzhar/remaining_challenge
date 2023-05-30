def student_discount(amount):
    student_discount=amount*0.1
    return student_discount
def regularbuy_discount(amount):
    regularbuy_discount=amount*0.05
    return regularbuy_discount
def discount(amount):
    studentdiscount=student_discount(amount)
    final_price=regularbuy_discount(studentdiscount)
    return final_price

amount=int(input("Enter the amount"))
final_price=discount(amount)
print(final_price)
