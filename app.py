import streamlit as st
import pandas as pd

st.title("Sales Data Calculator")

days = [f"Day {i}" for i in range(1, 11)]
sales = [12500, 8900, 15200, 9800, 17600, 11300, 14100, 7600, 16400, 13200]

total = sum(sales)
count = len(sales)
average = total / count
highest = max(sales)
lowest = min(sales)
best_day = days[sales.index(highest)]
worst_day = days[sales.index(lowest)]

st.header("Summary")
c1, c2 = st.columns(2)
c1.metric("Total sales", f"₹{total:,}")
c2.metric("Average sales", f"₹{average:,.2f}")
c3, c4 = st.columns(2)
c3.metric("Highest sale", f"₹{highest:,}", best_day)
c4.metric("Lowest sale", f"₹{lowest:,}", worst_day)

st.header("Daily sales")
df = pd.DataFrame({"Day": days, "Sales": sales})
st.table(df)
st.bar_chart(df.set_index("Day")["Sales"])

above = len([s for s in sales if s > average])
st.write(f"Days above average: {above} out of {count}")
