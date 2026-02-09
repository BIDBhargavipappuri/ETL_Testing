select * from Account_Details

select @@servername -- servername
SELECT DB_NAME()    -- DB name 

Select * from INFORMATION_SCHEMA.columns where TABLE_NAME = 'SO2'    -- to get column names in table

SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH,IS_NULLABLE FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME= 'Account_Details'                  -- all above details we will get
