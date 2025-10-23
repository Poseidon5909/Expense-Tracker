import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from db.db.db_connect import get_connection

# PIE CHART → TOTAL SPENDING BY CATEGORY

def show_category_expense_chart():
  conn = get_connection()
  if conn is None:
    return
  
  try:
      cursor = conn.cursor()
      query = """
          SELECT category, SUM(amount)
          FROM fin_expenses
          GROUP BY Category
          ORDER BY SUM(amount) DESC;
      """
      cursor.execute(query)
      data = cursor.fetchall()

      if not data:
         print("No data found. Please add some expenses first.")
         return
      
      categories = [row[0] for row in data]
      totals = [float(row[1]) for row in data]

      plt.figure(figsize=(8, 8))
      plt.pie(
         totals,
         labels=categories,
         autopct=lambda p: f'{p:.1f}%' if p > 0 else '',
         startangle=90
      )

      plt.title("💰 Total Spending by Category")
      file_path = "category_expense_chart.png"
      plt.savefig(file_path)
      plt.close()
      print(f"✅ Category chart successfully saved to {file_path}")
      

  except Exception as e:
     print("❌ Error generating category chart:", e)
  finally:
     conn.close()    

# BAR CHART → MONTHLY EXPENSES

def  show_monthly_expense_chart():
   conn = get_connection()
   if conn is None:
      return
   
   try:
       cursor = conn.cursor()
       query = """
          SELECT TO_CHAR(date, 'YYYY-MM') AS month, SUM(amount)
          FROM fin_expenses
          GROUP By month
          ORDER By month
       """

       cursor.execute(query)
       data = cursor.fetchall()

       if not data:
         print("No data found. Please add some expenses first.")
         return
      
       months = [row[0] for row in data]
       totals = [float(row[1]) for row in data]

       plt.figure(figsize=(10, 6))
       plt.bar(months, totals)
       plt.xlabel("Month")
       plt.ylabel("Total Spent(₹)")
       plt.title("📅 Monthly Spending Overview")
       plt.xticks(rotation=45)
       plt.tight_layout()
       file_path = "monthly_expense_chart.png"
       plt.savefig(file_path)
       plt.close() # Close the figure to free memory
       print(f"✅ Monthly chart successfully saved to {file_path}")
       

   except Exception as e:
      print("❌ Error generating monthly chart:", e)
   finally:
      conn.close()   

if __name__ == "__main__":
    show_category_expense_chart()
    show_monthly_expense_chart()