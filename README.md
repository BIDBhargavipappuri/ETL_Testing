# ETL_Testing
Testing tasks performed 

•ETL testing begins with reviewing the Business Requirement Document (BRD), which provides info what data needs to be moved, transformed, and reported.

•From the BRD, testers identify key data sources, transformation rules, and target systems. 

•ETL Developers then create test cases to validate each ETL step—ensuring data is correctly extracted, transformed according to business logic, and loaded into the destination. 

•SQL queries are used to check data accuracy, completeness, and consistency between source and target.

•	Usually, Testers will test the data in target , compare results with source.

•SCD Types – Slowly changing dimensions- 

SCD 0- Tables will get never updated once initially loaded. These are considered fixed or static values.

SCD 1 – in SCD type 1 data will be overwritten and the history won’t be available. Only most recent data will be available.  What type of changes are done can not be viewed. 

SCD 2 – in SCD type 2, historical data can be tracked, changes will be stored in new line.

In this type there will be Surrogate key, effective start date, end date, active flag columns will be there.

SCD type 3- no new row will be added , changes will be tracked in new column and we can see only one prior value , not full history can be viewed if multiple changes are done.
