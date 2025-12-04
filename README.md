📊 E-Commerce Sales Analysis & Customer Insights Dashboard
A Complete End-to-End Data Analytics Project (Phases 1–6)

📝 Project Overview
This project analyzes an e-commerce dataset to uncover sales trends, customer behavior, and business insights using a full analytics pipeline.
It includes data cleaning, statistical analysis, visual dashboards, and machine learning models, along with an Excel-based KPI dashboard as the final deliverable.

🚀 Key Objectives
1.Understand customer purchase behavior
2.Analyze sales performance across categories
3.Identify pricing & discount patterns
4.Build interactive dashboards for business insights
5.Predictive modeling for customer segmentation and churn
6.Deliver a professional Phase-6 Excel dashboard with formulas, charts, and analytics

🗂 Project Structure (Phases 1–6)
📌 Phase 1 – Data Collection & Understanding
-Imported e-commerce dataset (499 rows, 16 columns)
-Performed data profiling
-Identified missing values, duplicates, anomalies
-Built the Data Dictionary
-Documented assumptions like price units, date formats, etc.

📌 Phase 2 – Data Cleaning & Transformation
-Tools: Pandas, Excel
-Removed nulls, duplicates, unwanted columns
-Standardized column formats
-Converted Purchase_Date → datetime
-Extracted Year, Month, Day, DayOfWeek
-Applied Label Encoding to categorical fields
-Exported cleaned dataset: clean_data.csv
✔️ Output used for visualization, modeling, and dashboards.

📌 Phase 3 – Statistical Analysis
-Applied foundational statistical techniques:
-Descriptive statistics (mean, median, std)
-Correlation matrix
-Distribution analysis
-Hypothesis Testing:
      -T-test → Weekend vs Weekday sales
      -ANOVA → Category impact
      -Chi-Square → Categorical associations

📌 Phase 4 – Data Visualization
i}Python Visualizations (Matplotlib / Seaborn)
-Revenue Time-Series
-Distribution plots
-Correlation Heatmap
-Scatter matrix
-Violin & Joint plots

ii}Power BI Dashboard
-KPI Cards (Revenue, Orders, AOV)
-Category-wise Revenue Bar Chart
-Payment Method Donut Chart
-Time Series Line Chart
-Interactive slicers

iii}Tableau-Style Mock Dashboard
-Designed dashboard layout for multi-view insight reporting.

📌 Phase 5 – Machine Learning & Advanced Analytics
✔️ K-Means Clustering (RFM Segmentation)
-Recency, Frequency, Monetary values
-Customer segmentation into behavioral groups

✔️ Linear Regression
-Predict Final Price
-Evaluated using RMSE and R²

✔️ Logistic Regression (Customer Churn Prediction)
-Label based on Recency > 90 days
-Accuracy, Precision, Recall calculated

✔️ Decision Tree Classifier
-Predicted product categories
-Extracted feature importance

📌 Phase 6 – Excel Analysis & Final Dashboard
-Includes Phase-6 Deliverables:

✔️ Excel Formulas
-VLOOKUP
-INDEX–MATCH
-SUMIFS
-Conditional formatting

✔️ Pivot Table Analytics
-Category-wise revenue
-Payment method analysis
-Monthly sales trends



🛠️ Tech Stack
Layer	----------------------------------Tools Used
Data Cleaning	--------------------------Python (Pandas), Excel
Analysis	------------------------------Python, NumPy, SciPy
Visualization---------------------------Matplotlib, Seaborn, Power BI
Machine Learning------------------------Scikit-Learn
Dashboarding----------------------------Excel, Power BI
Documentation---------------------------GitHub, MicrosoftWord, PPT

📁 Project Files Included
├── Data/
│   ├── raw_data.csv
│   ├── clean_data.csv
│
├── Notebooks/
│   ├── EDA_Visualization.ipynb
│   ├── Statistical_Analysis.ipynb
│   ├── ML_Models.ipynb
│
├── Dashboards/
│   ├── PowerBI_Dashboard.pbix
│   ├── Excel_Dashboard.xlsx
│
├── Models/
│   ├── linear_regression.pkl
│   ├── logistic_regression.pkl
│   ├── kmeans_model.pkl
│   ├── decision_tree.pkl
│
├── Reports/
│   ├── Final_Project_Report.pdf
│   ├── Presentation.pptx
│
└── README.md

📈 Key Insights (Summary)
-Electronics & Fashion categories generate the highest revenue
-Weekends show significantly higher sales volume
-Payment methods show strong preference for digital wallets
-Discounts strongly correlate with Final Price variance
-High-value customers form a small but extremely profitable segment

📍 Conclusion
This project demonstrates a complete end-to-end data analytics pipeline, transforming raw transactional data into:
✔️ Actionable Insights
✔️ Predictive Models
✔️ Professional Dashboards
✔️ Business Recommendations

It is suitable for:
-Academic submissions
-Portfolio showcasing
-Interview demonstrations
-Real-world business analytics
