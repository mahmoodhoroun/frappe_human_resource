# Copyright (c) 2023, husam hammad and contributors
# For license information, please see license.txt

from frappe import *
from frappe.model.document import Document
from datetime import datetime
class Employee(Document):
	
 def validate(doc): 
  if doc.date_of_birth:
    today = datetime.now()
    dob = datetime.strptime(doc.date_of_birth, '%Y-%m-%d')
    doc.age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if doc.age > 60 and doc.status == "Active":
      throw("Cannot save employee with active status your age larger than 60.")
  else:
	    throw("choose your birthday")

