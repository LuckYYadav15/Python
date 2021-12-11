class validity:

    def f(str):

        a= ['()', '{}', '[]'] 

        while any(i in str for i in a):

            for j in a:

                str = str.replace(j, '') 

        return not str 

s = input("enter : ")

print(s, "-", "is valid" 

      if validity.f(s) else "is invalid")