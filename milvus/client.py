from pymilvus import MilvusClient, Collection, CollectionSchema

client = MilvusClient(host="localhost", port="19530")

def create_collection(collection_name: str, schema: CollectionSchema) -> None:
    client.create_collection(collection_name, schema)

def get_collection(collection_name: str) -> Collection:
    return client.get_collection(collection_name)

def insert_data(collection_name: str, data: list[dict]) -> None:
    client.insert(collection_name, data)

def search(collection_name: str, query_embedding: list[float], top_k: int) -> list[dict]:
    return client.search(collection_name, query_embedding, top_k)
