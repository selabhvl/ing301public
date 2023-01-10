import dataconverter
import gpscomputer
import gpsfiles
import visualise

# https://www.w3schools.com/python/
# https://github.com/dat100hib/dat100-prosjekt/blob/master/docs/introduksjon.md
# https://github.com/lmkr/dat100-prosjekt-gps-complete/tree/abd8e7e9635c676730089a3245487415f64ec985

GPS_DATA_FILES = ['short', 'medium', 'long', 'vm']

GPS_DATA_FILE = GPS_DATA_FILES[3]

WEIGHT = 80.0

if __name__ == '__main__':

    # read the GPS data from the csv file
    gps_csv_data = gpsfiles.read_gps_file(GPS_DATA_FILE)

    for line in gps_csv_data:
        print(line)

    # extract and convert the relevant part (time, latitude, longitude, elevation)
    gps_data = dataconverter.convert_data(gps_csv_data)

    for point in gps_data:
        print(point)

    # output summary and graphs
    gpscomputer.print_summary(WEIGHT, gps_data)

    visualise.plot_route(gps_data)
    visualise.plot_elevation(gps_data)
    visualise.plot_speeds(gps_data)


