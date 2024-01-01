import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("Let's first select a city! Which city are you interested "+
                     "in: Chicago, New York City or Washington?\n\n")
        # make entries case-insensitive and use small letters, as applied when assigning city names at lines 7-9
        city = city.lower()
        
        # invalid input handling for city
        if city not in ('new york city', 'chicago', 'washington'):
            print("Please enter a valid city.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to analyze for " + city.title() + 
                      "? You can choose between January, February, March, " +
                      "April, May and June, or type all if you do not wish "+
                      "to specify a month.\n\n")
        # make entries case-insensitive and use small letters
        month = month.lower()
        
        # invalid input handling for month
        if month not in ('january', 'february', 'march', 'april', 'may', 
                         'june', 'all'):
            print("Please enter a valid month.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Great choice. Now, let's pick a day." +
                    "You can choose between Monday, Tuesday, Wednesday," +
                    "Thursday, Friday, Saturday or Sunday, or type all if " +
                    "you do not wish to specify a day.\n\n")
        # make entries case-insensitive and use small letters
        day = day.lower()
        
        # invalid input handling for month
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                       'saturday', 'sunday', 'all'):
            print("Please enter a valid day.")
            continue
        else:
            break
    


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all': 
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")


    # TO DO: display the most common day of week
    print("The most common day is: ", df['day_of_week'].value_counts().idxmax())


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour is: ", df['hour'].value_counts().idxmax())
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")

    # display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("The total mean time is", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users. Statistics will be calculated using NumPy."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # 1. convert user type to an NumPy array for subseqent counts
    usertypes = df['User Type'].values
    
    # 2. count the occurences of the different user types
    ct_subscriber  = (usertypes == 'Subscriber').sum()
    ct_customer = (usertypes == 'Customer').sum()
    
    # 3. print user type counts
    print('The number of subscribers in', city.title(), 'is:',ct_subscriber,'\n')
    print('The number of customers in', city.title(), 'is:',ct_customer,'\n')

    # Display counts of gender
    # Display earliest, most recent, and most common year of birth
    # gender and year of birth are missing from the Washington dataset
    if city.title() != 'Washington':
        # counts of gender
        # 1. convert gender to an NumPy array for subseqent counts
        gender = df['Gender'].values
        
        # 2. count the occurences of the different user types
        ct_male  = (gender == 'Male').sum()
        ct_female = (gender == 'Female').sum()
        
        # 3. print counts
        print('The number of male users in', city.title(), 'is:',ct_male,'\n')
        print('The number of female users in', city.title(), 'is:',ct_female,'\n')
        
        # year of birth
        # 1. convert gender to an NumPy array for subseqent statistics
        birthyear = df['Birth Year'].values
        
        # 2. get unique birth years and exclude NaNs
        birthyear_unique = np.unique(birthyear[~np.isnan(birthyear)])
        
        # 3. the latest birth year is the highest / maximum number
        latest_birthyear = birthyear_unique.max()
        
        # 4. the earliest birth year is the lowest / minimum number
        earliest_birthyear = birthyear_unique.min()
        
        # 5. print latest and earliest birth year
        print('The most recent birth year of users in', city.title(), 'is:',
              latest_birthyear ,'\n')
        print('The earliest birth year of users in', city.title(), 'is:',
              earliest_birthyear,'\n')   
        
        # 6. display most common birth year
        print('The most common birth year of users in', city.title(), 'is:', 
              df['Birth Year'].value_counts().idxmax(), '\n')
    
    else:
        # print message if Washington was chosen as city
        print('Sorry. Gender and birth year information are not available for Washington!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def raw_data(df):
    """Displays the data due filteration.
    5 rows will added in each press"""
    print('press enter to see row data, press no to skip')
    x = 0
    while (input()!= 'no'):
        x = x+5
        print(df.head(x))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()