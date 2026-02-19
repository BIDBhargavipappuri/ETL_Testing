# ETL_Testing
Testing tasks performed 

•ETL testing begins with reviewing the Business Requirement Document (BRD), which provides info what data needs to be moved, transformed, and reported.

•From the BRD, testers identify key data sources, transformation rules, and target systems. 

•ETL Developers then create test cases to validate each ETL step—ensuring data is correctly extracted, transformed according to business logic, and loaded into the destination. 

•SQL queries are used to check data accuracy, completeness, and consistency between source and target.

•Usually, Testers will test the data in target , compare results with source.

•SCD Types – Slowly changing dimensions- 

SCD 0- Tables will get never updated once initially loaded. These are considered fixed or static values.

SCD 1 – in SCD type 1 data will be overwritten and the history won’t be available. Only most recent data will be available.  What type of changes are done can not be viewed. 

SCD 2 – in SCD type 2, historical data can be tracked, changes will be stored in new line.

In this type there will be Surrogate key, effective start date, end date, active flag columns will be there.

SCD type 3- no new row will be added , changes will be tracked in new column and we can see only one prior value , not full history can be viewed if multiple changes are done

# Checks Done as part of ETL testing –

Meta Data Validation – 

ETL Test Case Mapping (with SQL Examples)

1. Source Count Check- Verify number of records in source table.
	
 ```sql
 SELECT COUNT(*) FROM crm.customers;  
 ```

2.	Active Filter Validation-Ensure only active customers are loaded

```sql
SELECT COUNT(*) FROM staging.customers WHERE status <> 'Active';(Again, validating against BRD)
```

3.	Transformation Check-Confirm names are capitalized - (Again, validating against BRD)
	
```sql
SELECT customer_name FROM staging.customers WHERE customer_name != UPPER(customer_name);
```
    
4.	Duplicate Check-Ensure no duplicate customer IDs in target
   
```sql
SELECT customer_id, COUNT(*) FROM dw.customers GROUP BY customer_id HAVING COUNT(*) > 1;
 ```

5.	Row Count Match-Compare source active count with target count
	
```sql
SELECT (SELECT COUNT(*) FROM crm.customers WHERE status = 'Active') AS source_count, (SELECT COUNT(*)
FROM dw.customers) AS target_count;
```

6.	Source – Target validation– Ensure every record from the source system is correctly loaded into the target system.
	
```sql
SELECT * FROM SRC
EXCEPT
SELECT * FROM TGT
```

7.	Target – Source validation - Ensure every record in the target system has a corresponding source record.
    
```sql
SELECT * FROM TGT
EXCEPT
SELECT * FROM SRC
```
   	
8.	SOURCE_INTERSECT_TARGET-- records that are common between the source and target tables — confirming successful data transfer for matching keys.
    
 ```sql
 SELECT * FROM SRC
 INTERSECT
 SELECT * FROM TGT
 ```
  	
9.	TARGET_INTERSECT_SOURCE - Identify records in the target that also exist in the source — confirming that target data has valid origins.

 ```sql
 SELECT * FROM TGT
 INTERSECT
 SELECT * FROM SRC
 ```


After performing above validations automation can also be done if in cases the same SQL queries need to be ran again and again.

1.	ETL Testing Automation Workflow: Python → SQL → Power BI → Power Automate.
   
2.	Develop Python scripts to run ETL test cases using SQL queries.
	
3.	Capture test results (pass/fail status, row counts, error messages) and store them in a structured SQL table- dedicated table.
	
4.	Connect Power BI Desktop to the SQL database containing etl_test_results and publish to power BI service and schedule refresh in service.
	
    	•Design a dashboard to visualize:

	    •Total tests executed

	    •Pass vs Fail counts

	    •Test-wise status breakdown

        •Error summaries and timestamps
  	
6.  Create a Power Automate flow triggered by the refreshed Power BI dataset.
    
    •	If any test case fails:

    •	Send an email to testers with a summary of failed cases and error details.

    •   Optionally, include a link to the Power BI report for deeper analysis. 

7.	Automating and Scheduling Python ETL Test Script –
    
8. If we schedule python script using Cron Job (Automation Engine) only email alert will be sent, no history, no detailed view, if any non-technical user it’s hard to understand. 

9. But with power automated detailed visualization  can be provided as email alert.
p
10. I built a Python-based ETL test automation engine(Attached .py file) and scheduled it using windows task scheduler.
    
12. It logs results to SQL and integrates with Power BI for visualization and Power Automate for alerts. 
How to schedule task in task scheduler in windows.
     Press Windows + S and search for Task Scheduler
1.	Click Create Basic Task (right panel)
2.	 Name: ETL Test Automation
3.	Trigger: Choose Daily, set your preferred time (e.g., 7:00 AM)
4.	Action: Choose Start a program
5.	Program/script: Paste the path to Python:  C:\Users\bharg\OneDrive\Desktop\ETL\run_sql_files.py
6.	Click Finish. 




