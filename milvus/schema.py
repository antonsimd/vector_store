from pymilvus import FieldSchema, CollectionSchema, DataType

def create_company_schema(collection_name: str) -> CollectionSchema:
    return CollectionSchema(
        fields=[
            FieldSchema(name="Company Name", dtype=DataType.VARCHAR, max_length=255, is_primary=True),
            FieldSchema(name="Company Description", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="Company Website", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="Past Clients", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="All Products", dtype=DataType.VARCHAR, max_length=3000),
            FieldSchema(name="All Products Embedding", dtype=DataType.FLOAT_VECTOR, dim=1536),
        ],  
        description=f"Collection for {collection_name}"
    )

def create_employee_schema(collection_name: str) -> CollectionSchema:
    return CollectionSchema(
        fields=[
            FieldSchema(name="Employee Name", dtype=DataType.VARCHAR, max_length=255, is_primary=True),
            FieldSchema(name="Employee Email", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="Employee Salary", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="Employee Job Title", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="Employee Company", dtype=DataType.VARCHAR, max_length=255),
        ],
        description=f"Collection for {collection_name}"
    )

