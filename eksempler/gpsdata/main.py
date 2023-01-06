import dataconverter
import gpscomputer
import gpsfiles

# https://www.w3schools.com/python/
# https://github.com/dat100hib/dat100-prosjekt/blob/master/docs/introduksjon.md
# https://github.com/lmkr/dat100-prosjekt-gps-complete/tree/abd8e7e9635c676730089a3245487415f64ec985

GPS_DATA_FILES = ['short', 'medium', 'long', 'vm']


def run_analysis(data_file):
    # TODO: You can try implementing the functions in 'dataconverter' and 'gpscomputer' to
    #  challenge yourself and practice some Python. Alternatively you can lookup a demo solution
    #  by looking into the branch 'gpscomputer' on the remote 'hvl' repository.

    # read the GPS data from the csv file
    gps_csv_data = gpsfiles.read_gps_file(data_file)
    # extract and convert the relevant part (time, latitude, longitude, elevation)
    gps_data = dataconverter.convert_data(gps_csv_data)
    # output summary and graphs
    gpscomputer.print_summary(gps_data)


if __name__ == '__main__':
    print("""
    Hei! and welcome to the GPS Track Analyzer!
    Please enter a number to select a data set you want to analyze:
    1: Short Track
    2: Medium Track
    3: Long Track
    4: World Championship Track
    or enter anything else to quit...
    """)
    user_input = input()
    if len(user_input) > 0 and user_input.isdigit() and 0 < int(user_input) < 5:
        selection = int(user_input) - 1
        file = GPS_DATA_FILES[selection]
        print(f"Selected dataset: {file}")
        run_analysis(file)
    else:
        print("Exiting")
