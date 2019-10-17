import requests
import csv


# CSV_FILE_NAME
CSV_FILE_NAME = "Violent_Crime___Property_Crime_by_County__1975_to_Present.csv"


def download_csv(url, download_file_name):
    """
    Download the CSV file according to the URL and save it to the specified location
    :param url:
    :param download_file_name:
    :return:
    """
    print("Ready to download...")
    response = requests.get(url, stream=True)
    with open(download_file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print("Download complete！")


if __name__ == "__main__":
    csv_url = "https://opendata.maryland.gov/api/views/jwfa-fdxs/rows.csv?accessType=DOWNLOAD"
    download_csv(csv_url, CSV_FILE_NAME)
