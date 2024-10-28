# Spending Calculator

Fetches spending on each shop from a bank statement CSV. Outputs the total amount spent on all shops; total monthly 
spending; total spending on each shop; and monthly spending by store. 

Customisable, stores can be added/deleted as needed.

Format of the CSV file:

```
Transaction Date, Transaction Type, Sort Code, Account Number, Transaction Description, Debit Amount, Credit Amount, Balance
```

Where:

- `Transaction Date` represents the date of the transaction, obviously, in the format `DD/MM/YYYY`. Example "28/10/2024"
- `Transaction Description` represents the name of the shop. Example `TESCO`. **Case sensitive**
- `Debit Amount` represents the amount of the transaction. `10.00` means "10 pounds"
- Other fields not accounted for and have no impact on the output.