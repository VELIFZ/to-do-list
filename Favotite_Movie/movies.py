# store removed ones somewhere else to reach out later if not delete in 30 days
    # make a trash bin
# movie titles are key, others information values 
    # key : Name 
    # values in nested dictionary Rating, Director, Year
    
# initializing an empty dictionary to store movie details that obtained from user
# movies ={}

movies = {'Ask':
     {'year': '2001',
      'director' : 'kar',
      'rating': '9'
     },
    'bos ev':
     {'year': '1990',
      'director' : 'kim',
      'rating': '9'
     }
}
# MARK: add
def add():
    # while loop to get information from user until they say otherwise
    while True:
        print('\nEnter all information about your favorites movies. If you do not know the information just enter empty space.')
        # Prompt for movie details
        name = input('\nName: ').strip().title()
        #! Add error handle for empty movie name entry blow this line
        if name == '':
            print('\nHave to have a movie name.')
            continue
        
        year = input('\nYear: ').strip().title()
        director = input('\nDirector: ').strip().title()
        rating = input('\nRating: ').strip().title()
        
        # Dictionary structure 
        movies[name] = {}
        # If inputs are empty or passed
        #? Should I add isdigit for rating and year?
        if year:
            movies[name]['Year'] = year
        else:
            movies[name]['Year'] = 'Unknown'
        if director:
            movies[name]['Director'] = director
        else: 
            movies[name]['Director'] = 'Unknown'
        if rating:
            movies[name]['Rating'] = rating
        else:
            movies[name]['Rating'] =  'Unknown'
            
        # Ask for more inputs
        add_more = input('\nAnother one? Yes or No ').strip().title()
        # Stop the program if user done with giving information
        if (add_more == 'No'):
            break
        
    print(movies)
#add()

# MARK: view
#? How can I show the movies better way?
def view():
    for m_name, info in movies.items():
        print(f"Name: {m_name}")
        for k, detail in info.items():
            # if unknown don't print
            if detail != 'Unknown':
                print(f"\n{k}: {detail}")
#view()

# MARK: delete
def delete():
    #! make a way to stop this if they choose 2 -delete movie option- as a mistake
    delete_movie = input('Which movie would you like to remove? ').strip().title()
    print(delete_movie)
    # tell if there is no movies to delete
    if not movies:
        print('There are no movies to delete')
    elif delete_movie not in movies:
        print(f'There is not a movie in your list named {delete_movie}.')
        delete()
    else:
        trash(delete_movie)
        #! should I add trash function features in here than make another function
        #del movies[delete_movie]
        #print(f'{delete_movie} is removed from the list')
        #view()
#delete()

def trash(delete_movie):
    # initiate an empty dict to store deleted ones
    trash_bin = {}
    if delete_movie in movies:
        trash_bin[delete_movie] = movies.pop(delete_movie)
    print(trash_bin)

        
# MARK: main 
def main():
    print('Choose one of the following options.')
    print('\nTo add movie: 1 \nTo delete: 2 \nView the list: 3  \nTo quit: 4')
    while True:
        choose = input("Enter your choose.").strip()
        if choose == '1':
            add()
        elif choose == '2':
            delete()
        elif choose == '3':
            view()
        elif choose == '4':
            break
main()