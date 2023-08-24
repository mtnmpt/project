-- Create a new stored procedure called 'StoredProcedureName' in schema 'dbo'
-- Drop the stored procedure if it already exists
-- IF EXISTS (
-- SELECT *
--     FROM INFORMATION_SCHEMA.ROUTINES
-- WHERE SPECIFIC_SCHEMA = N'dbo'
--     AND SPECIFIC_NAME = N'StoredProcedureName'
--     AND ROUTINE_TYPE = N'PROCEDURE'
-- )
-- DROP PROCEDURE dbo.StoredProcedureName
-- GO
-- Create the stored procedure in the specified schema
ALTER PROCEDURE SP_item1_GetList
@ItemName         NVARCHAR(50) 
AS
BEGIN
    SELECT * 
    FROM   item1
    WHERE  ( ISNULL(@ItemName,'') = '' OR ItemName = @ItemName )
END
GO
-- example to execute the stored procedure we just created
-- execution 123
