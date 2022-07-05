""" _______________________________ """
#!""" Class Example (Child) """

from Doctor import Doctor

class FamilyDoctor(Doctor):
  def works_where(self):
    print("I work with families")

  def paid_by_who(self):
    print("I get paid by the people")

""" _______________________________ """