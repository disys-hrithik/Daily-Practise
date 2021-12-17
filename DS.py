"Approach 1"
name="hrithik"


"Approach 2"
class friday:
    work="python"
    def __init__(self):
        self.tea=5
    def display(self):
        print(self.tea)

hrithik=friday()
hrithik.display()


"Approach  3"
saturday=("sleep","wash","outing")
print(saturday[2])



"Approach 4"
sunday={"morning":"soup","afternoon":"biryani","evening":"worry","night":"sleep"}
print(sunday["morning"])



"Approach 5"
print(saturday)
for i in  saturday :
    print(i)

for i in sunday.values():
    print(i)


"Approach 6"
students=[{"id":23,"name":"anu","branch":"bba"},{"id":25,"name":"nua","branch":"bca"}]
print(students[0],students[1])
for i in students:
    if i["name"]=="anu":
        print("anu is available")
    elif i["branch"]=="bba":
        print("bba")




"Approach 7"
funday=[{"internship":[{"empid":"DIN0067","dept":"software","reporting":"ak"},{"empid":"DIN0068","dept":"software","reporting":"ak"}]},
 {"fulltime job":[{"empid":"DIN0069","dept":"software","reporting":"ak"},{"empid":"DIN0076","dept":"software","reporting":"ak"}]},
 {"contract job":[{"empid":"DIN0080","dept":"software","reporting":"ak"},{"empid":"DIN0090","dept":"software","reporting":"ak"}]}]
print(funday)
for i in funday:
    if i["internship"][0]["empid"]=="DIN0067":
        print("it exists")
















        
        
