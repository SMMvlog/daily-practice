data = [ 

   { 

      "id":1,

      "name":"name1",

      "color":[ 

         "red",

         "green"

      ]

   },

   { 

      "id":2,

      "name":"name2",

      "color":[ 

         "pink",

         "yellow"

      ]

   },

   { 

      "id":3,

      "name":"name3",

      "color":[ 

         "green",

         "yellow"

      ]

   }

]

result = []

for dct in data:
        if "green" in dct.get("color"):
            result.append(dct["id"])
print(result)



 