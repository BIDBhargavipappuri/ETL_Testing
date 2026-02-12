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
    
5.	Duplicate Check-Ensure no duplicate customer IDs in target
   
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


