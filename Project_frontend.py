import tkinter as tk
from tkinter import messagebox
from linear_regression import execute_linear_regression
from elbow_method import elbow
from kmeans_quality_of_sleep import k_means

def show_kmeans_results():
    sleep_quality_predicted=[0,0,0]
    result_window = tk.Toplevel()
    result_window.title("Clustering by K-Means")
    result_window.geometry("600x500")

    result_window.configure(bg='#ADD8E6')  # Light shade of blue

    # Label for Linear Regression heading
    heading_label = tk.Label(result_window, text="K-Means Clustering", font=("Helvetica", 16, "bold"), bg='#ADD8E6', pady=10)
    heading_label.pack()

    description_label = tk.Label(
        result_window,
        text="The K-Means algorithm has been used to group different types of people based on their Physical Activity "
             "level and their Stress Levels. The number of groups is decided by using elbow method",
        font=("Arial", 12),
        wraplength=420,
        bg='#ADD8E6',
    )
    description_label.pack(pady=10)

    result_label = tk.Label(result_window, text="Result", font=("Arial", 14, "bold"), bg='#ADD8E6', pady=10)
    result_label.pack()

    results=elbow('Stress Level', 'Physical Activity Level')
    no_of_cluster_label = tk.Label(result_window, text=f"Number of Clusters: {results}",font=("Arial", 12), bg='#ADD8E6')
    no_of_cluster_label.pack()

    results_1=k_means()
    coeff1_label = tk.Label(result_window,
                                  text=f"Centroid 1: Stress Level = {results_1[0][0]:.2f} Physical Activity Level ={results_1[0][1]:.2f}",
                                  font=("Arial", 12), bg='#ADD8E6')
    coeff1_label.pack()

    coeff2_label = tk.Label(result_window,
                            text=f"Centroid 2: Stress Level = {results_1[1][0]:.2f} Physical Activity Level ={results_1[1][1]:.2f}",
                            font=("Arial", 12), bg='#ADD8E6')
    coeff2_label.pack()

    coeff3_label = tk.Label(result_window,
                            text=f"Centroid 3: Stress Level = {results_1[2][0]:.2f} Physical Activity Level ={results_1[2][1]:.2f}",
                            font=("Arial", 12), bg='#ADD8E6')
    coeff3_label.pack()

    quality_label = tk.Label(result_window, text="Predicted Sleep Quality of Centroids from relation found :", font=("Arial", 14, "bold"), bg='#ADD8E6', pady=10)
    quality_label.pack()
    sleep_quality_predicted[0] = 0.1*results_1[0][0] - 0.6*results_1[0][1] + 9.97
    sleep_quality_predicted[1] = 0.1 * results_1[1][0] - 0.6 * results_1[1][1] + 9.97
    sleep_quality_predicted[2] = 0.1 * results_1[2][0] - 0.6 * results_1[2][1] + 9.97

    pred_quality_label = tk.Label(result_window, text=f" Centroid 1 = {sleep_quality_predicted[0]:.2f}", font=("Arial", 14), bg='#ADD8E6', pady=10)
    pred_quality_label.pack()

    pred_quality_label1 = tk.Label(result_window, text=f" Centroid 2 = {sleep_quality_predicted[1]:.2f}", font=("Arial", 14), bg='#ADD8E6', pady=10)
    pred_quality_label1.pack()

    pred_quality_label2 = tk.Label(result_window, text=f" Centroid 3 = {sleep_quality_predicted[2]:.2f}",
                                   font=("Arial", 14), bg='#ADD8E6', pady=10)
    pred_quality_label2.pack()

def show_linear_regression_results():
    # Create a new window for Linear Regression results
    result_window = tk.Toplevel()
    result_window.title("Linear Regression Results")
    result_window.geometry("600x400")  # Adjust the size as needed

    # Set background color
    result_window.configure(bg='#ADD8E6')  # Light shade of blue

    # Label for Linear Regression heading
    heading_label = tk.Label(result_window, text="Linear Regression", font=("Helvetica", 16, "bold"), bg='#ADD8E6', pady=10)
    heading_label.pack()

    # Label for Linear Regression description
    description_label = tk.Label(
        result_window,
        text="Linear regression establishes a relation between the target variable - Sleep Quality and independent variables Stress Level and Physical Activity Level.",
        font=("Arial", 12),
        wraplength=420,
        bg='#ADD8E6',
    )
    description_label.pack(pady=10)

    # Button to show graph
    #show_graph_button = tk.Button(result_window, text="Show Graph", command=execute_linear_regression(True))
    #show_graph_button.pack(pady=10)

    # Label for Linear Regression results
    result_label = tk.Label(result_window, text="Result", font=("Arial", 14, "bold"), bg='#ADD8E6', pady=10)
    result_label.pack()

    results= execute_linear_regression()

    coefficients_label = tk.Label(result_window, text=f"Physical Activity Level Coefficient: {results['coefficient'][0]:.2f}", font=("Arial", 12), bg='#ADD8E6')
    coefficients_label.pack()

    coefficients_label = tk.Label(result_window, text=f"Stress Level Coefficient: {results['coefficient'][1]:.2f}",font=("Arial", 12), bg='#ADD8E6')
    coefficients_label.pack()

    intercept_label = tk.Label(result_window, text=f"Intercept: {results['intercept']:.2f}", font=("Arial", 12),bg='#ADD8E6')
    intercept_label.pack()

    rs_label = tk.Label(result_window, text=f"R-squared: {results['rs']:.2f}%", font=("Arial", 12), bg='#ADD8E6')
    rs_label.pack()

    equation_label = tk.Label(result_window, text=f"Relation of Quality of Sleep = {results['line_equation']}", font=("Arial", 12),wraplength=580, bg='#ADD8E6')
    equation_label.pack(pady=10)

global sq
sq=0

def get_values():
    try:
        # Get values from text boxes and convert to float
        physical_activity = float(physical_activity_entry.get())
        stress_level = float(stress_level_entry.get())
        global sq
        sq= 0.1*physical_activity - 0.6*stress_level + 9.97
        print(sq)
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


# Create a Tkinter window
window = tk.Tk()
window.title("DMPA Project")

# Set window size
window.geometry("500x500")  # Adjust the size as needed

# Set background color
window.configure(bg='#ADD8E6')  # Light shade of blue

# Label for project name
project_name_label = tk.Label(window, text="Sleep Data Analysis", font=("Helvetica", 16, "bold"), pady=10, bg='#ADD8E6')
project_name_label.pack()

# Label for project information
project_info_label = tk.Label(
    window,
    text="The objective is to create an accurate prediction model that can detect abnormal sleep patterns, measure and predict the quality of sleep, and maybe even help with the early diagnosis of sleep-related diseases.",
    font=("Arial", 12),
    wraplength=380,
    bg='#ADD8E6',
)
project_info_label.pack(pady=10)

# Label for contributors
contributors_label = tk.Label(window, text="Done by Amogh KG and Rakshit Nadageri", font=("Arial", 10), bg='#ADD8E6')
contributors_label.pack()

# Button to execute K-Means clustering (replace with your K-Means function)
kmeans_button = tk.Button(window, text="Cluster by K-Means", command=show_kmeans_results, bg='#87CEEB')  # Sky Blue
kmeans_button.pack(pady=10)

# Button to execute Linear Regression
linear_regression_button = tk.Button(window, text="Predict by Linear Regression", command=show_linear_regression_results, bg='#87CEEB')  # Sky Blue
linear_regression_button.pack(pady=10)

physical_activity_label = tk.Label(window, text="Physical Activity Level:", bg='#87CEEB')
physical_activity_label.pack(pady=10)

physical_activity_entry = tk.Entry(window, bg='#87CEEB')
physical_activity_entry.pack(pady=10)

stress_level_label = tk.Label(window, text="Stress Level:", bg='#87CEEB')
stress_level_label.pack(pady=10)

stress_level_entry = tk.Entry(window, bg='#87CEEB')
stress_level_entry.pack(pady=10)
submit_button = tk.Button(window, text="Predict", command=get_values, bg='#87CEEB')
submit_button.pack(pady=10)


"""pred_stress_level_label = tk.Label(window, text=f"Predicted Stress Level: {sq}", font=("Helvetica", 13, "bold"), bg='#87CEEB')
pred_stress_level_label.pack(pady=10)"""


# Run the Tkinter event loop
window.mainloop()
