import csv
from collections import defaultdict
from datetime import datetime


def extract_monthly_and_store_spending(csv_file, stores_to_track):
    monthly_spending = defaultdict(float)
    store_spending = defaultdict(float)
    store_monthly_spending = defaultdict(lambda: defaultdict(float))

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Transaction date in format DD/MM/YYYY
            transaction_date = datetime.strptime(row['Transaction Date'], '%d/%m/%Y')
            # Name of the shop
            transaction_description = row['Transaction Description']
            # Amount paid
            debit_amount = float(row['Debit Amount']) if row['Debit Amount'] else 0.0

            # Check if the store name matches any store name under stores_to_track
            for store_to_track in stores_to_track:
                if store_to_track in transaction_description:
                    month_key = transaction_date.strftime('%Y-%m')
                    monthly_spending[month_key] += debit_amount
                    store_spending[transaction_description] += debit_amount
                    store_monthly_spending[transaction_description][month_key] += debit_amount

    total_spending = sum(monthly_spending.values())
    return total_spending, monthly_spending, store_spending, store_monthly_spending


def main():
    csv_file = 'spending.csv'
    stores_to_track = ["TESCO", "SAINSBURY", "DELIVEROO"]  # Full names or partial store name
    total_spending, monthly_spending, store_spending, store_monthly_spending = extract_monthly_and_store_spending(
        csv_file, stores_to_track)

    print("Total Spending: £{:.2f}".format(total_spending))
    print("\nMonthly Spending:")
    for month, spending in sorted(monthly_spending.items()):
        print(f"{month}: £{spending:.2f}")

    print("\nStore Spending:")
    for store, spending in store_spending.items():
        print(f"{store}: £{spending:.2f}")

    print("\nMonthly Spending by Store:")
    for store, monthly_spending in store_monthly_spending.items():
        print(f"{store}:")
        for month, spending in sorted(monthly_spending.items()):
            print(f"\t{month}: £{spending:.2f}")


if __name__ == "__main__":
    main()
