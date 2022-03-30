def driver(): 
  InfoDb = [] #InfoDB lists
# List with dictionary records placed in a list  
  InfoDb.append({  
               "CompanyName": "Microsoft",  
               "Founder": "Bill Gates, Paul Allen",  
               "CEO": "Satya Nadella",  
               "Headquarters": "Redmond, WA",  
               "Founded": "April 4, 1975, Albuquerque, NM",  
               "a_products":["Surface Pro 7","Microsoft Windows","Internet Explorer","Visual Studio", "Xbox 360"]  
              })  

  InfoDb.append({  
               "CompanyName": "Meta",  
               "Founder": "Mark Zuckerberg",  
               "CEO": "Mark Zuckerberg",  
               "Headquarters": "Redmond, WA",  
               "Founded": "February 2004, Cambridge, MA",  
               "a_products":["Facebook","Whatsapp","Facebook Messenger","Metaview", "Instagram"]   
              }) 

  InfoDb.append({ 
               "CompanyName": "Google",  
               "Founder": "Larry Page, Sergey Brin",  
               "CEO": "Sundar Pichai",  
               "Headquarters": "Mountain View, CA",  
               "Founded": "September 4, 1998, Menlo Park, CA",  
               "a_products":["Google Search","Google Scholar","Etsy","Chrome", "Google Ads"]  
              }) 

  InfoDb.append({ 
               "CompanyName": "Amazon",  
               "Founder": "Jeff Bezos",  
               "CEO": "Andy Jassy",  
               "Headquarters": "Seattle, WA",  
               "Founded": "July 5, 1994, Bellevue, WA",  
               "a_products":["Amazon Site","Zappos","Audible","Ring", "Souq"]  
              }) 

  print("InfoDB List:", InfoDb)

  def print_data(n): #print the list by appending products
    print(InfoDb[n]["CompanyName"], InfoDb[n]["Founder"])
    print("\t", "Products: ", end="")
    print(", ".join(InfoDb[n]["a_products"]))
    print()

  def for_loop(): #Loop runs through all values in InfoDB and prints them
    for n in range(len(InfoDb)):
      print_data(n)

  def while_loop(n): #while the running number is less than the length, keep printing
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

  def recursive_loop(n): #loops through each of the values recursively
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return 

  def recur_factorial(n): #print factorial recursively
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

  def tester():
    print("For loop") #run for loop
    for_loop()
    print("While loop") #run while loop
    while_loop(0)
    print("Recursive loop") #run recursive loop
    recursive_loop(0)
  print()
  print()
  tester()
