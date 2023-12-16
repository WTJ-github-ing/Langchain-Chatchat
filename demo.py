#_*_coding:UTF-8_*_
#时间:2023-12-16 21:41
#文件名称：demo.py
#工具：PyCharm
# 启动模型
from transformers import AutoTokenizer,AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatqlm-6b",trust_remote_code=True)

model = AutoModel.from_pretrained("THUDM/chatglm-b",trust_remote_code=True).half().cuda()
chatglm = model.eval()

from langchain.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

filepath = "test.txt"
#加载文件
loader = UnstructuredFileLoader(filepath)
docs = loader.load()
#文本分割
text_splitter = CharacterTextSplitter(chunk_size=500,chunk_overlap=200)
docs = text_splitter.split_text(docs)
# 构建向量库
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs,embeddings)
# 根据提问匹配上下文
query ="Langchain 能够接入哪些数据类型?"
docs = vector_store.similarity_search(query)
context = [doc.page_content for doc in docs]
prompt = f"已知信息: \n{context}\n根据已知信息回答问题: \n{query}"
chatglm.chat(tokenizer,prompt,history=[])