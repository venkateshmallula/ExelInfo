import streamlit as st
import pandas as pd

# Streamlit application title
st.title('Rider Revenue and Profit Calculation')

# Upload the Excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file:
    # Read the Excel file
    df = pd.read_excel(uploaded_file)
    
    # Creating columns for layout with specific widths
    col1, col2= st.columns([7, 3])

    # Display the DataFrame in the first column
    with col1:
        st.subheader('ExcelFile')
        st.write(df)
    
    # Input column names and outputs in the second column
    with col2:
        st.subheader('Insights:')
        id_column = "ID"
        name_column = "Name"
        gross_column = "Gross_Payout 2"
        final_net_payout_column = "Final Net Payout"
        working_hours_column = "Login_Time"
    
        if id_column and name_column and gross_column and final_net_payout_column and working_hours_column:
            try:
                # Rider count
                rider_count = df[id_column].nunique()
                st.write('Rider Count:', rider_count)

                # Total revenue
                total_revenue = df[gross_column]
                total_revenue_sum = total_revenue.sum()
                st.write('Total Revenue:', total_revenue_sum)

                # Riders' salaries
                riders_salaries = df[final_net_payout_column].sum()
                st.write('Riders Salaries:', riders_salaries)

                # Profit calculation
                profit = total_revenue_sum - riders_salaries
                st.write('Profit:', profit)

                # Profit percentage
                profit_percentage = (profit / total_revenue_sum) * 100
                st.write('Profit Percentage (%):', profit_percentage)


                # Average revenue per rider
                average_revenue_per_rider = total_revenue_sum / rider_count
                st.write('Average Revenue per Rider:', average_revenue_per_rider)

                # Average working hours per rider
                average_working_hours_per_rider = df.groupby(id_column)[working_hours_column].mean().mean()
                st.write('Average Working Hours per Rider:', average_working_hours_per_rider)

                # Total orders
                total_orders = df['Order'].sum()
                st.write('Total Orders:', total_orders)

                # Highest earning of the rider
                highest_earning_rider_id = df.loc[df[gross_column].idxmax()][id_column]
                highest_earning_rider_name = df.loc[df[gross_column].idxmax()][name_column]
                highest_earning_amount = df[gross_column].max()
                st.markdown("Highest Earning Rider: "+f'<span style="color:green"> {highest_earning_rider_name} (ID: {highest_earning_rider_id}) (Earning: {highest_earning_amount})</span>', unsafe_allow_html=True)                
            except KeyError as e:
                st.error(f"Column not found: {e}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
