import tkinter as tk




def calculate_budget():
   salary = float(salary_entry.get())


   monthly_food_budget = float(food_entry.get())
   monthly_transportation_budget = float(transport_entry.get())
   monthly_entertainment_budget = float(entertainment_entry.get())
   monthly_utilities_budget = float(utilities_entry.get())


   housing_type = housing_var.get()
   monthly_rent = 0
   monthly_mortgage = 0
   yearly_tax = 0


   if housing_type == "apartment":
       monthly_rent = float(rent_entry.get())
   elif housing_type == "house":
       mortgage_or_tax = tax_or_mortgage_var.get()
       if mortgage_or_tax == "mortgage":
           monthly_mortgage = float(mortgage_entry.get())
       elif mortgage_or_tax == "property tax":
           yearly_tax_percent = float(tax_entry.get())
           yearly_tax = (yearly_tax_percent / 100) * salary


   yearly_food_budget = monthly_food_budget * 12
   yearly_transportation_budget = monthly_transportation_budget * 12
   yearly_entertainment_budget = monthly_entertainment_budget * 12
   yearly_utilities_budget = monthly_utilities_budget * 12
   yearly_rent = monthly_rent * 12
   yearly_mortgage = monthly_mortgage * 12


   yearly_expenses = (
           yearly_food_budget
           + yearly_transportation_budget
           + yearly_entertainment_budget
           + yearly_utilities_budget
           + yearly_rent
           + yearly_mortgage
           + yearly_tax
   )


   yearly_savings = salary - yearly_expenses




   if yearly_savings < 0:
       result_text = f"You are in debt by: ${-yearly_savings:.2f}"
   elif yearly_savings == 0:
       result_text = "You are breaking even. Consider lowering some costs to save for emergencies."
   else:
       result_text = f"Your yearly savings is: ${yearly_savings:.2f}"


   result_label.config(text=result_text)




root = tk.Tk()
root.geometry("1000x1000")
root.title("Yearly Budget Calculator")


tk.Label(root, text="Enter your yearly salary: ").grid(row=0, column=0)
salary_entry = tk.Entry(root)
salary_entry.grid(row=0, column=1)


tk.Label(root, text="Monthly Food Budget: ").grid(row=1, column=0)
food_entry = tk.Entry(root)
food_entry.grid(row=1, column=1)


tk.Label(root, text="Monthly Transport Budget: ").grid(row=2, column=0)
transport_entry = tk.Entry(root)
transport_entry.grid(row=2, column=1)


tk.Label(root, text="Monthly Entertainment Budget: ").grid(row=3, column=0)
entertainment_entry = tk.Entry(root)
entertainment_entry.grid(row=3, column=1)


tk.Label(root, text="Monthly Utilities Budget: ").grid(row=4, column=0)
utilities_entry = tk.Entry(root)
utilities_entry.grid(row=4, column=1)


housing_var = tk.StringVar(value="apartment")
tk.Label(root, text="Housing Type:").grid(row=5, column=0)
tk.Radiobutton(root, text="Apartment", variable=housing_var, value="apartment").grid(row=5, column=1)
tk.Radiobutton(root, text="House", variable=housing_var, value="house").grid(row=5, column=2)


tk.Label(root, text="If Apartment, enter rent:").grid(row=6, column=0)
rent_entry = tk.Entry(root)
rent_entry.grid(row=6, column=1)


tax_or_mortgage_var = tk.StringVar(value="mortgage")
tk.Label(root, text="If House, select:").grid(row=7, column=0)
tk.Radiobutton(root, text="Mortgage", variable=tax_or_mortgage_var, value="mortgage").grid(row=7, column=1)
tk.Radiobutton(root, text="Property Tax", variable=tax_or_mortgage_var, value="property tax").grid(row=7, column=2)


tk.Label(root, text="Enter Mortgage (if applicable):").grid(row=8, column=0)
mortgage_entry = tk.Entry(root)
mortgage_entry.grid(row=8, column=1)


tk.Label(root, text="Enter Property Tax % (if applicable):").grid(row=9, column=0)
tax_entry = tk.Entry(root)
tax_entry.grid(row=9, column=1)


tk.Button(root, text="Calculate Budget", command=calculate_budget).grid(row=10, column=0, columnspan=2)


result_label = tk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=2)


root.mainloop()

