""" _______________________________ """
#!""" Dictionaries (OBJECTS) """

""" OBJECT use { 
  object_name={
    "KEY":"VAlUE"
  }
  KEY type number or string
  Value type number or string or boolean or array or object
} """
convert_month = {
  "Jan":"January",
  "Feb":"February",
  "Mar":"March",
  "Apr":"April",
  "May":"May",
  "Jun":"June",
}

print(convert_month["Mar"])   #* The output is March
print(convert_month.get("Jun"))   #* The output is June
print(convert_month.get("Hope"))   #* The output is None
""" print(object_name.get(KEY_value,ERROR_MSG)) """
print(convert_month.get("Hope","The value doesn't exist"))   #* The output is The value doesn't exist 
print(convert_month.get("Jan","The value doesn't exist"))   #* The output is January

""" _______________________________ """
