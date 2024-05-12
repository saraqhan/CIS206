import csv

def cgp(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        regpay = 40 * rate
        otpay = (hours - 40) * (rate * 1.5)
        return regpay + otpay

def formatemail(fname, lname):
    return f"{fname[0].lower()}{lname.lower()}@gm.com"

def processcsv(inputfile, outputfile):
    try:
        with open(inputfile, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            with open(outputfile, 'w', newline='') as outputcsv:
                csvwriter = csv.writer(outputcsv)

                csvwriter.writerow(['Last Name', 'First Name', 'Gross Pay', 'Email'])
            
                next(csvreader)
                for row in csvreader:
                    fname, lname, hours, rate = row
                    hours = int(hours)
                    rate = float(rate)
                    grosspay = cgp(hours, rate)
                    email = formatemail(fname, lname)
                    csvwriter.writerow([lname, fname, grosspay, email])
        print("output file generated successfully.")
    except FileNotFoundError:
        print("Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    processcsv("input.csv", "output.csv")