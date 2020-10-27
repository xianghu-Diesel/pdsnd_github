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
    city = input("which city do you want to get (chicago,new york city,washington):\n").lower()
    if not city in CITY_DATA:
        while not city in CITY_DATA:
            print(city+" not in the citylist, please give a city once more\n")
            city = input("which city do you want to get (chicago,new york city,washington):\n").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("which month do you want to get (all, january, february, ... , june):\n").lower()
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    if not month in months:
        while not month in months:
            print(month + " not in the monthlist, please give a month once more\n")
            month = input("which month do you want to get (all, january, february, ... , june):\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("which day of week do you want to get (all, monday, tuesday, ... sunday):\n").lower()
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']
    if not day in days:
        while not day in days:
            print(day + " not in the day of week-list, please give a day of week once more\n")
            day = input("which day of week do you want to get (all, monday, tuesday, ... sunday):\n").lower()


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'], yearfirst=True)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
        month = months[month.lower()]

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months={1:'january',2:'february',3:'march',4:'april',5:'may',6:'june'}
    # TO DO: display the most common month
    print("the most common month: "+months[df['month'].value_counts().index[0]].title()+" Counts: "+str( df['month'].value_counts().values[0]))

    # TO DO: display the most common day of week
    print("the most common day of week: " + df['day_of_week'].value_counts().index[0] + " Counts: " +
          str(df['day_of_week'].value_counts().values[0]))


    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print("the most common hour: " + str(df['hour'].value_counts().index[0]) + " Counts: " +
          str(df['hour'].value_counts().values[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used start station: " + df['Start Station'].value_counts().index[0] + " Counts: " +
          str(df['Start Station'].value_counts().values[0]))

    # TO DO: display most commonly used end station
    print("the most commonly used end station: " + df['End Station'].value_counts().index[0] + " Counts: " +
          str(df['End Station'].value_counts().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    results= df['Start Station'].str.cat(df['End Station'],sep=' to ')
    print("the most frequent combination of start station and end station trip: " + results.value_counts().index[0] + " Counts: " +
          str(results.value_counts().values[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time: " +str(df['Trip Duration'].sum()//60)+" min "+ str(df['Trip Duration'].sum()%60)+" s")

    # TO DO: display mean travel time
    print("mean travel time: " + str(df['Trip Duration'].mean() // 60) + " min " + str(
        df['Trip Duration'].mean() % 60) + " s")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Type: " +df['User Type'].value_counts().index[0]+" Counts: "+str(df['User Type'].value_counts().values[0]))
    print("User Type: " + df['User Type'].value_counts().index[1] + " Counts: " + str(
        df['User Type'].value_counts().values[1]))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("User Gender: " + df['Gender'].value_counts().index[0] + " Counts: " + str(
            df['Gender'].value_counts().values[0]))
        print("User Gender: " + df['Gender'].value_counts().index[1] + " Counts: " + str(
            df['Gender'].value_counts().values[1]))
    else:
        print("no User Gender in the list")


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("earliest year of birth: " + str(df['Birth Year'].min()))
        print("most recent year of birth: " + str(df['Birth Year'].max()))
        print("most common year of birth: " + str(df['Birth Year'].value_counts().index[0]) + " Counts: " + str(
            df['Birth Year'].value_counts().values[0]))
    else:
        print("no User Birth Year in the list")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)



        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        i=0
        rawdata= input('\nWould you like to see the first 5 lines of raw data? Enter yes or no.\n')
        while rawdata=='yes':
            print(df.iloc[i:i+5])
            i+=5
            rawdata = input('\nWould you like to see the next 5 lines of raw data? Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()