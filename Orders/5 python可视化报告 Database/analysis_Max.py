import csv
import matplotlib.pyplot as plt


# CSV_FILE_NAME
CSV_FILE_NAME = "Violent_Crime___Property_Crime_by_County__1975_to_Present.csv"


def read_csv(csv_file_name):
    """
    Read CSV file
    :param csv_file_name:
    :return:
    """
    with open(csv_file_name, "r", encoding="utf-8") as file:
        lst_row = []
        csv_reader = csv.reader(file)
        for row in csv_reader:
            lst_row.append(row)
        return lst_row



def show_menu():
    """
    Display menu
    :return:
    """
    print("""A) Show basic analysis
B) Show basic analysis by area
C) Show basic analysis by year
D) Show summary of violent crime
E) Show summary of property crime
F) Show area of crime with all crime type
G) Show graph of the total crime number by year
Q) Exit""")


def show_basic_analysis(lst_row):
    """
    Show basic analysis
       :param lst_row:
    :return:
    """
    # Data header
    lst_title = lst_row[0]
    # Related column index
    column_index_area = lst_title.index("JURISDICTION")
    column_index_year = lst_title.index("YEAR")
    column_index_grand_total = lst_title.index("GRAND TOTAL")
    # Total data
    datas_count = len(lst_row) - 1
    # Area number
    area_count = len(get_column_datas(lst_row, column_index_area, True))
    # Year number
    year_count = len(get_column_datas(lst_row, column_index_year, True))
    # Get the summary of grand total
    sum_grand_total, avg_grand_total, max_grand_total_row, min_grand_total_row = \
        get_specified_column_summary(lst_row, column_index_grand_total)
    # Print results
    print("-" * 80)
    print(f"Total Datas: {datas_count:>8}")
    print(f"Total Areas: {area_count:>8}")
    print(f"Total Years: {year_count:>8}\n")
    print(f"Maximum Total Crime: {max_grand_total_row[column_index_area]} in {max_grand_total_row[column_index_year]}: "
          f"{max_grand_total_row[column_index_grand_total]}")
    print(f"Minimum Total Crime: {min_grand_total_row[column_index_area]} in {min_grand_total_row[column_index_year]}: "
          f"{min_grand_total_row[column_index_grand_total]}")
    print(f"Average Crime Num: {avg_grand_total:.2f}")
    print(80 * '-')


def show_basic_analysis_by_area(lst_row):
    """
    Show the total number of crimes in different regions
    :param lst_row:
    :return:
    """
    # data header
    lst_title = lst_row[0]
    # Related column index
    column_index_area = lst_title.index("JURISDICTION")
    column_index_grand_total = lst_title.index("GRAND TOTAL")
    # Get the year crime dictionary
    dict_area_crime = get_specified_column_summary_group_by(lst_row, column_index_area, column_index_grand_total)
    # Sort by the number of criminals
    lst_area_crime = sorted(dict_area_crime.items(), key=lambda x: x[1][1], reverse=True)
    # print results
    print("-" * 80)
    for area, lst_summary_data in lst_area_crime:
        print(f"{area:25}, total:{lst_summary_data[0]}, average:{lst_summary_data[2]:.2f}, "
              f"max:{lst_summary_data[3][column_index_grand_total]}, "
              f"min:{lst_summary_data[3][column_index_grand_total]}")
    print("-" * 80)


def show_basic_analysis_by_year(lst_row):
    """
    Show the total number of crimes in different years
    :param lst_row:
    :return:
    """
    # data header
    lst_title = lst_row[0]
    # Related column index
    column_index_year = lst_title.index("YEAR")
    column_index_grand_total = lst_title.index("GRAND TOTAL")
    # Get the year crime dictionary
    dict_year_crime = get_specified_column_summary_group_by(lst_row, column_index_year, column_index_grand_total)
    # Sort by the number of criminals
    lst_year = sorted(dict_year_crime.keys())
    # print results
    print("-" * 80)
    for year in lst_year:
        lst_summary_data = dict_year_crime[year]
        print(f"{year:6}, total:{lst_summary_data[0]}, average:{lst_summary_data[2]:.2f}, "
              f"max:{lst_summary_data[3][column_index_grand_total]}, "
              f"min:{lst_summary_data[3][column_index_grand_total]}")
    print("-" * 80)


def show_summary_of_violent_crime(lst_row):
    """
    Show a summary of violent crimes
    :param lst_row:
    :return:
    """
    # data header
    lst_title = lst_row[0]
    # Related column index
    column_index_violent_crime = lst_title.index("VIOLENT CRIME TOTAL")
    sum_data, avg_data, max_row, min_row = get_specified_column_summary(lst_row, column_index_violent_crime)
    print("-" * 80)
    print(f"Total of violent crime: {sum_data}")
    print(f"The average of violent crime: {avg_data:.2f}")
    print(f"The max of violent crime: {max_row[column_index_violent_crime]}")
    print(f"The min of violent crime: {min_row[column_index_violent_crime]}")
    print("-" * 80)


def show_summary_of_property_crime(lst_row):
    """
    Show the summary of economic crimes
    :param lst_row:
    :return:
    """
    # data header
    lst_title = lst_row[0]
    # Related column index
    column_index_property_crime = lst_title.index("PROPERTY CRIME TOTALS")
    sum_data, avg_data, max_row, min_row = get_specified_column_summary(lst_row, column_index_property_crime)
    print("-" * 80)
    print(f"Total of property crime: {sum_data}")
    print(f"The average of property crime: {avg_data:.2f}")
    print(f"The max of property crime: {max_row[column_index_property_crime]}")
    print(f"The min of property crime: {min_row[column_index_property_crime]}")
    print("-" * 80)


def show_area_crime_with_all_type(lst_row):
    """
    Display data of different crime types in different regions
    :param lst_row:
    :return:
    """
    # data header
    lst_title = lst_row[0]
    # Regional list
    column_index_area = lst_title.index("JURISDICTION")
    lst_area = get_column_datas(lst_row, column_index_area, True)
    # Types of crime
    lst_crime_type = lst_title[3:9]
    # Define the result list, which is used to save the final data to be displayed. The list is a two-dimensional list.
    lst_result = []
    # Add title line
    lst_result.append(["City/Crime Type"] + lst_crime_type)
    # Define the dictionary type of region and crime type. Key is the region, and value is the list sorted by crime type. The elements in it are the sum of corresponding types in the region.
    dict_area_crime_type = {}
    # Statistics by type
    for crime_type_index, crime_type in enumerate(lst_crime_type):
        dict_area_crime_type_summary = get_specified_column_summary_group_by(lst_row, column_index_area,
                                                                             crime_type_index + 3)
        for area in dict_area_crime_type_summary:
            if area not in dict_area_crime_type:
                dict_area_crime_type[area] = [0] * len(lst_crime_type)
            dict_area_crime_type[area][crime_type_index] = dict_area_crime_type_summary[area][0]
    # Arrange the data in LST "result" in order
    for area in lst_area:
        row = [area] + dict_area_crime_type[area]
        lst_result.append(row)
    # Print information
    print("-" * 80)
    for row in lst_result:
        for col_index, col in enumerate(row):
            if col_index == 0:
                print(f"{col:<25}", end="")
            else:
                print(f"{col:>15}", end="")
        print()
    print("-" * 80)


def show_total_crime_graph_by_year(lst_row):
    """
    Map showing total crimes per year
    :param lst_row:
    :return:
    """
    # data header
    lst_title = lst_row[0]
    # Get the year crime dictionary
    column_index_year = lst_title.index("YEAR")
    column_index_grand_total = lst_title.index("GRAND TOTAL")
    dict_year_crime = get_specified_column_summary_group_by(lst_row, column_index_year, column_index_grand_total)
    lst_year = sorted(dict_year_crime.keys())
    plt.figure(figsize=(12, 6.5))
    plt.xlabel("Year")
    plt.ylabel("Total Crime")
    plt.title("Total Crime By Year")
    lst_total_crime = [dict_year_crime[year][0] for year in lst_year]
    #Because the x-axis scale year is too long, it can only be displayed one year apart, otherwise the scales will be too dense and cover each other.
    plt.plot(lst_year[::2], lst_total_crime[::2], linewidth=2)
    plt.show()


def get_column_datas(lst_row, col_index, is_without_repetition):
    """
    Get the data of a column in order
    :param lst_row: All row data
    :param col_index: Column index
    :param is_without_repetition: whether want to go heavy
    :return:
    """
    lst_col = [row[col_index] for row in lst_row[1:]]
    if is_without_repetition:
        lst_result = []
        for data in lst_col:
            if data not in lst_result:
                lst_result.append(data)
        return lst_result
    else:
        return lst_col


def get_specified_column_summary_group_by(lst_row, group_by_column_index, target_column_index):
    """
    Get the summary data of the target column, and return the total number, the maximum value row, the minimum value row and the average value respectively
    Group by specified group column
    :param lst_row:
    :param group_by_column_index:
    :param target_column_index:
    :return:
    """
    # Define a dictionary as the final return data. Key is the data of the specified column, and value is the summary result of the target column.
    # The result is a list: [total, count, average, maximum row, minimum row]
    dict_result = {}
    for row in lst_row[1:]:
        key = row[group_by_column_index]
        target_value = int(row[target_column_index])
        if key not in dict_result:
            dict_result[key] = [0, 0, 0, None, None]
        dict_result[key][0] += target_value
        dict_result[key][1] += 1
        dict_result[key][2] = dict_result[key][0] / dict_result[key][1]
        max_row = dict_result[key][3]
        if max_row is None or target_value > int(max_row[target_column_index]):
            dict_result[key][3] = row
        min_row = dict_result[key][4]
        if min_row is None or target_value < int(min_row[target_column_index]):
            dict_result[key][4] = row
    return dict_result


def get_specified_column_summary(lst_row, column_index):
    """
    Get the summary data of a column, and return the total number, average value, maximum value row and minimum value row respectively
    :param lst_row:
    :param column_index:
    :return:
    """
    sum_value = 0
    max_value = None
    max_row = None
    min_value = None
    min_row = None
    for row in lst_row[1:]:
        row_value = int(row[column_index])
        sum_value += row_value
        if max_value is None or row_value > max_value:
            max_value = row_value
            max_row = row
        if min_value is None or row_value < min_value:
            min_value = row_value
            min_row = row
    avg_value = sum_value / (len(lst_row) - 1)
    return sum_value, avg_value, max_row, min_row


def main():
    """
    The entry of main program 
    :return:
    """
    lst_row = read_csv(CSV_FILE_NAME)
    while True:
        show_menu()
        option = input("Please select an option: ").lower()
        if option == "a":
            show_basic_analysis(lst_row)
        elif option == "b":
            show_basic_analysis_by_area(lst_row)
        elif option == "c":
            show_basic_analysis_by_year(lst_row)
        elif option == "d":
            show_summary_of_violent_crime(lst_row)
        elif option == "e":
            show_summary_of_property_crime(lst_row)
        elif option == "f":
            show_area_crime_with_all_type(lst_row)
        elif option == "g":
            show_total_crime_graph_by_year(lst_row)
        elif option == "q":
            break
        else:
            print(f"Sorry, unknown option: {option}")


if __name__ == "__main__":
    main()
