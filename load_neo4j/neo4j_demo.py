import json
from py2neo import Graph, Node, Relationship

# Connect to Neo4j database
graph = Graph("neo4j+s://56338587.databases.neo4j.io", auth=("neo4j", "123qwe!!"))

#data processing ,For the data format, see train_res3.json
data = []
count=0
with open("train_res3.json", "r") as file:
    for line in file:
        item = json.loads(line)
        if count<1999:
            data.append(item)
            count=count+1
spo_list_set = []
for item in data:
    spo_list = item["spo_list"]
    spo_list_set.extend(spo_list)
sample_data = {"spo_list_set": spo_list_set}


# Check if the node exists, if not, create the node
def get_or_create_node(name):
    query = f"MATCH (n:Entity {{name: '{name}'}}) RETURN n"
    result = graph.evaluate(query)
    if result:
        return result
    else:
        return Node("Entity", name=name)

# Create nodes and relationships
if __name__ == "__main__":
    for spo in sample_data["spo_list_set"]:
        subject_node = get_or_create_node(spo["subject"])
        object_node = get_or_create_node(spo["object"])
        relation = Relationship(subject_node, spo["predicate"], object_node)
        graph.create(subject_node | object_node | relation)
        print("数据导入完成。")

        # Close the connection to the Neo4j database
        graph.close()

# https://neo4j.com/ 注册并登录
# 创建AuraDB实例
# 通过graph = Graph("neo4j+s://56338587.databases.neo4j.io", auth=("neo4j", "123qwe!!"))
# 显示关系（边）
# MATCH (n)-[r]-()
# RETURN n, r