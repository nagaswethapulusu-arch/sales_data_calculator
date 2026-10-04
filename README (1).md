# Sales Data Calculator

A beginner-friendly Python project that analyzes a collection of sales values and calculates the **total sales, average sales, highest sale, and lowest sale**.

## Objective

Understand basic numerical data analysis using Python.

## Tools Used

- Python 3
- Jupyter Notebook
- Streamlit (for the live demo)

## Dataset

A manually created dataset of daily sales for 10 days, stored in two Python lists (`days` and `sales`). Sales are in Indian rupees (₹).

| Day | Sales (₹) |
|-----|----------|
| Day 1 | 12,500 |
| Day 2 | 8,900 |
| Day 3 | 15,200 |
| Day 4 | 9,800 |
| Day 5 | 17,600 |
| Day 6 | 11,300 |
| Day 7 | 14,100 |
| Day 8 | 7,600 |
| Day 9 | 16,400 |
| Day 10 | 13,200 |

## Approach

1. **Create a list** of sales values (and a matching list of day labels).
2. **Total sales** is calculated using `sum(sales)`.
3. **Number of sales** is counted using `len(sales)`.
4. **Average sales** is the total divided by the number of sales: `total / len(sales)`.
5. **Highest and lowest sale** are found using `max(sales)` and `min(sales)`.
6. **Best and worst day** are found by getting the position of the value with `sales.index()` and using that position to pick the label from `days`.
7. **Bonus:** count how many days sold more than the average.

## Explanation of Results

- **Total sales** (₹126,600) is the overall revenue earned across all 10 days.
- **Average sales** (₹12,660.00) represents the typical sales amount for one day. Days above it performed better than usual, and days below it performed worse.
- **Highest sale** (₹17,600 on Day 5) shows the best-performing day.
- **Lowest sale** (₹7,600 on Day 8) shows the weakest day, which may need attention.
- 5 out of 10 days were above the average.

## How to Run

1. Install Python and Jupyter Notebook:
   ```
   pip install notebook
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   python -m notebook
   ```
4. Open `sales_data_calculator.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Sample Output

```
Total sales: ₹126,600
Number of sales days: 10
Average sales: ₹12,660.00
Highest sale: ₹17,600 (Day 5)
Lowest sale: ₹7,600 (Day 8)
Days above average: 5 out of 10
```

## Limitations

- If two days share the highest or lowest sale, `.index()` returns only the first one.
- The program does not handle an empty list (dividing by zero would cause an error).
- Sales values are typed in manually instead of being read from a file.

## Possible Improvements

- Read sales from a CSV file.
- Add median and standard deviation.
- Plot a bar chart of daily sales with the average line.

## Author

SwethaPulusu
