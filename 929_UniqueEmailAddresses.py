
def numUniqueEmails(self, emails: List[str]) -> int:
    if len(emails) == 0:
        return 0
    res = set()
    for mail in emails: 
        emailid, domain = mail.split("@")

        if "+" in emailid:
            emailid = emailid.split("+")[0].replace(".", "")
        else:
            emailid = emailid.replace(".","")

        res.add(emailid+"@"+domain)

    return len(res)
  
  
  def numUniqueEmails(emails: List[str]) -> int:
     if len(email) == 0:
        return 0
      res = set()
      
     for mail in emails:
        emailid, domain = mail.split("@")
        emailid = emailid.split("+")[0].replace(".","")
        res.add((emailid, domain))
     return len(res)
