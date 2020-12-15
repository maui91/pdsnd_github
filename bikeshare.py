import time
import pandas as pd
import numpy as np


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Auto-Reply: Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("\nAuto-Reply: Which city would you like to explore: chicago, new york city or washington? \n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("\nAuto-Reply:invalid input. Please enter a valid input\n")
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nAuto-Reply: Do you want details specific to a particular month? If yes, type month name from within first six months else type 'all'\n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("\nAuto-Reply:invalid input. Please enter a valid input\n")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nAuto-Reply:Do you want details specific to a particular day? If yes, type day name else type 'all'\n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("\nAuto-Reply:invalid input. Please enter a valid input\n")

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
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("\nAuto-Reply:Listing common month: {}\n".format(
        str(df['month'].mode().values[0]))
    )

    # display the most common day of week
    print("\nAuto-Reply:Listing common day of the week: {}\n".format(
        str(df['day_of_week'].mode().values[0]))
    )

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("\nAuto-Reply:The most common start hour: {}\n".format(
        str(df['start_hour'].mode().values[0]))
    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nAuto-Reply: Listing most common start station is: {} \n".format(
        df['Start Station'].mode().values[0])
    )

    # display most commonly used end station
    print("\n\nAuto-Reply: Listing most common end station is: {}\n".format(
        df['End Station'].mode().values[0])
    )

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("\nAuto-Reply: Listing most common start and end station combo is: {}\n".format(
        df['routes'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # display total travel time
    print(" total travel time : {}".format(
        str(df['duration'].sum()))
    )

    # display mean travel time
    print(" mean travel time: {}".format(
        str(df['duration'].mean()))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("\nAuto-Reply: According to user types:\n")
    print(df['User Type'].value_counts())

    if city != 'washington':
        # Display counts of gender
        print("\nAuto-Reply:According to gender:\n")
        print(df['Gender'].value_counts())


        # Display earliest, most recent, and most common year of birth
        print("\nAuto-Reply:earliest birth year: {}\n".format(
            str(int(df['Birth Year'].min())))
        )
        print("\nAuto-Reply:latest birth year: {}\n".format(
            str(int(df['Birth Year'].max())))
        )
        print("\nAuto-Reply:The common birth year: {}\n".format(
            str(int(df['Birth Year'].mode().values[0])))
        )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    choice = input('\nAuto-Reply: Want to check on row data? Answer with :Yes/No \n').lower()
    print()
    if choice=='yes' :
        choice=True
    elif choice=='no':
        choice=False    
    else:
        print('\nAuto-Reply: Invild input, try again\n')
        display_data(df)
        return

    if choice:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            choice = input('\nAuto-Reply:Another five? Answer with Yes/No\n').lower()
            if choice=='yes':
                continue
            elif choice=='no':
                break
            else:
                print('Auto-Reply: You did not enter a valid choice.')
                return



def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
