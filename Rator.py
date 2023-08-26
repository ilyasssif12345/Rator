current_reviews = int(input("-current reviews : "))
current_rating = float(input("-current rating : "))

points = current_reviews * current_rating

def Tools():            
         print("_________Choose (1/2) _________")     
         print("1- I want to know the final rating")
         print("2- How much i should add")
         choice = int(input("---->"))
         if choice == 1:
                final_rating()
         elif choice == 2:
               review_added()
         else :
               print(" i don't have time for you")

def final_rating():
       while True :
              rev_added = input("-reviews added : ")
              if rev_added == "q":
                     Tools()
              else:
                     rev_added = int(rev_added )
                     final_rating = round((points + (5 * rev_added)) / (current_reviews + rev_added) , 1)
                     print(f"final rating : {final_rating}")
        
def review_added():     
      while True:
            final_rating = input("-final rating : ")
            if final_rating == "q":
                     Tools()
            else:
                     final_rating = float(final_rating)
                     rev_added = int((points - (final_rating * current_reviews)) / (final_rating - 5))
                     print(f"Add : {rev_added + 1}")
Tools()      