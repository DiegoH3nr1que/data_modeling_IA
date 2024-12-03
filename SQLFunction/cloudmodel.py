import streamlit as st
import json
import requests
import logging
import pandas as pd
from pymongo import MongoClient
from bson import ObjectId
import graphviz
import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword, DDL

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# PRIMEIRO INSTANCIAR NO COLLAB
# python -m streamlit run data_modeling_app.py (Para rodar o app).
# Streamlit, graphviz, sqlparse, pandas

NGROK_URL = "https://conversely-precise-moray.ngrok-free.app" #"(NGROK_LINK FREE APP)"

def query_ollama(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False 
    }
    
    logging.debug(f"Enviando prompt: {prompt}") 
    
    try:
        response = requests.post(f"{NGROK_URL}/api/generate", headers=headers, json=data)
        response.raise_for_status()  

        full_response = ""
        logging.debug(f"Resposta bruta: {response.text}") 
        
        json_response = json.loads(response.text)
        if 'response' in json_response:
            full_response = json_response['response']
        
        logging.debug(f"Resposta completa: {full_response}")
        return full_response

    except requests.RequestException as e:
        logging.error(f"Falha na requisição: {e}")
        return f"Erro ao fazer a requisição: {e}"

def generate_data_model(input_data):
    prompt = f"""
    Dada a seguinte estrutura de dados:
    {input_data}
    
    Gere um modelo de dados que represente essa estrutura de forma eficiente. 
    Inclua nomes de tabelas, nomes de colunas, tipos de dados e relacionamentos.
    Retorne o resultado como uma string JSON, um esquema SQL e uma explicação em texto claro sobre o modelo gerado.
    """
    return query_ollama(prompt)

def optimize_data_structure(current_model):
    prompt = f"""
    Dado o seguinte modelo de dados:
    {current_model}
    
    Otimize esse modelo de dados para melhorar a eficiência, reduzir redundâncias e aumentar a integridade dos dados.
    Retorne o resultado como uma string JSON, um esquema SQL e uma explicação em texto claro sobre as otimizações realizadas.
    """
    return query_ollama(prompt)

def generate_complete_documentation():
    """
    Gera documentação automática baseada no histórico das funções chamadas.
    """
    if "history" not in st.session_state or not st.session_state.history:
        return "Nenhuma ação foi registrada para gerar documentação."

    documentation = "### Documentação Completa\\n"
    for action in st.session_state.history:
        documentation += f"#### {action['function_name']}\\n"
        documentation += "**Entradas:**\\n"
        documentation += f"```json\\n{json.dumps(action['inputs'], indent=2)}\\n```\\n"
        documentation += "**Saídas:**\\n"
        documentation += f"```json\\n{json.dumps(action['outputs'], indent=2)}\\n```\\n"
    return documentation


def adapt_to_changes(current_model, new_requirements):
    prompt = f"""
    Dado o modelo de dados atual:
    {current_model}
    
    E os seguintes novos requisitos:
    {new_requirements}
    
    Adapte o modelo de dados para atender a esses novos requisitos, mantendo a eficiência e a integridade dos dados.
    Retorne o resultado como uma string JSON, um esquema SQL e uma explicação em texto claro sobre as mudanças realizadas.
    """
    return query_ollama(prompt)

def generate_sql_queries(current_model, query_type):
    prompt = f"""
    Dado o seguinte modelo de dados:
    {current_model}
    
    Gere exemplos de consultas SQL do tipo '{query_type}', como SELECT, INSERT, UPDATE ou DELETE, baseados nesse modelo de dados.
    Retorne as consultas geradas.
    """
    return query_ollama(prompt)

def process_csv_file(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        input_data = df.to_json(orient='records')
        return input_data
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo CSV: {e}")
        return None

def execute_schema(schema_json, db_url):
    try:
        
        client = MongoClient(db_url)
        db = client['data_model_db']
        
        
        schema = json.loads(schema_json)
        for table in schema.get('tables', []):
            collection_name = table['name']
            collection = db[collection_name]
            sample_data = {}
            
            
            for column in table['columns']:
                column_name = column['name']
                if 'sample_value' in column:
                    sample_data[column_name] = column['sample_value']
                else:
                    column_type = column['type'].lower()
                    if column_type == 'string':
                        sample_data[column_name] = "exemplo"
                    elif column_type == 'integer':
                        sample_data[column_name] = 0
                    elif column_type == 'double':
                        sample_data[column_name] = 0.0
                    elif column_type == 'boolean':
                        sample_data[column_name] = True
                    elif column_type == 'datetime':
                        sample_data[column_name] = "2023-01-01T00:00:00"
                    elif column_type == 'array':
                        sample_data[column_name] = []
                    elif column_type == 'object':
                        sample_data[column_name] = {}
                    elif column_type == 'objectid':
                        sample_data[column_name] = str(ObjectId())
                    else:
                        sample_data[column_name] = None
            
            
            collection.insert_one(sample_data)
        
        return "Esquema JSON executado com sucesso no banco de dados MongoDB fornecido."
    except Exception as e:
        logging.error(f"Erro ao executar esquema no banco de dados: {e}")
        return f"Erro ao executar esquema no banco de dados: {e}"

def extract_table_name(token):
    if isinstance(token, Identifier):
        return token.get_name()
    return None

def visualize_data_model(json_model=None, sql_model=None):
    try:
        dot = graphviz.Digraph(comment='Modelo de Dados', format='png', graph_attr={'rankdir': 'TB'})

        if json_model:
            model = json.loads(json_model)
            
            
            for table in model.get('tables', []):
                table_name = table['name']
                dot.node(table_name, table_name, shape='box')
                
                
                for column in table['columns']:
                    column_name = f"{table_name}.{column['name']} ({column['type']})"
                    dot.node(column_name, column_name, shape='ellipse')
                    dot.edge(table_name, column_name)
            
           
            for table in model.get('tables', []):
                for column in table['columns']:
                    if 'foreign_key' in column:
                        referenced_table = column['foreign_key']['table']
                        referenced_column = column['foreign_key']['column']
                        column_name = f"{table['name']}.{column['name']} ({column['type']})"
                        referenced_column_name = f"{referenced_table}.{referenced_column}"
                        dot.edge(column_name, referenced_table, label=f"FK to {referenced_column_name}", color="blue")
        
        elif sql_model:
            statements = sqlparse.split(sql_model)
            tables = {}
            
            
            for statement in statements:
                parsed = sqlparse.parse(statement)[0]
                tokens = [token for token in parsed.tokens if not token.is_whitespace]
                if tokens and tokens[0].ttype is DDL and tokens[0].value.upper() == 'CREATE':
                   
                    table_name = None
                    for token in tokens:
                        if isinstance(token, Identifier):
                            table_name = extract_table_name(token)
                            break
                        elif isinstance(token, IdentifierList):
                            for identifier in token.get_identifiers():
                                table_name = extract_table_name(identifier)
                                break
                    
                    if table_name:
                        columns = []
                        for token in tokens:
                            if isinstance(token, sqlparse.sql.Parenthesis):
                                columns = [str(col).strip() for col in token.get_sublists()]
                                break
                        tables[table_name] = columns
            
           
            for table_name, columns in tables.items():
                dot.node(table_name, table_name, shape='box')
                for column in columns:
                    column_name = f"{table_name}.{column}"
                    dot.node(column_name, column_name, shape='ellipse')
                    dot.edge(table_name, column_name)
        
        return dot
    except Exception as e:
        logging.error(f"Erro ao visualizar o modelo de dados: {e}")
        return None


st.title("Modelagem de Dados com IA")


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "history" not in st.session_state:
    st.session_state.history = []


action = st.selectbox("O que você gostaria de fazer?", 
                      ["Selecionar uma ação", "Gerar modelo de dados", "Otimizar estrutura", "Adaptar a mudanças", "Gerar consultas SQL", "Executar esquema JSON", "Visualizar modelo de dados",
        "Gerar documentação completa"])

if action == "Gerar modelo de dados":
    input_option = st.selectbox("Como você gostaria de fornecer os dados?", ["Descrição", "JSON", "CSV"])
    input_data = ""

    if input_option == "Descrição":
        input_data = st.text_area("Digite sua estrutura de dados (descrição):", height=150)
    elif input_option == "JSON":
        input_data = st.text_area("Cole seu JSON de entrada:", height=150)
    elif input_option == "CSV":
        uploaded_file = st.file_uploader("Envie seu arquivo CSV:", type=["csv"])
        if uploaded_file is not None:
            input_data = process_csv_file(uploaded_file)

    if st.button("Enviar"):
        if input_data:
            response = generate_data_model(input_data)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.history.append({
                "function_name": "generate_data_model",
                "inputs": input_data,
                "outputs": response
            })
            with st.chat_message("assistant"):
                st.markdown(response)


elif action == "Gerar documentação completa":
    if st.button("Gerar Documentação"):
        documentation = generate_complete_documentation()
        st.markdown(documentation)


elif action == "Otimizar estrutura":
    current_model = st.text_area("Digite seu modelo de dados atual:", height=150)
    if st.button("Enviar"):
        if current_model:
            response = optimize_data_structure(current_model)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.history.append({
                "function_name": "optimize_data_structure",
                "inputs": current_model,
                "outputs": response
            })
            with st.chat_message("assistant"):
                st.markdown(response)


elif action == "Adaptar a mudanças":
    current_model = st.text_area("Digite seu modelo de dados atual:", height=150)
    new_requirements = st.text_area("Digite novos requisitos:", height=150)
    if st.button("Enviar"):
        if current_model and new_requirements:
            response = adapt_to_changes(current_model, new_requirements)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.history.append({
                "function_name": "adapt_to_changes",
                "inputs": {
                    "current_model": current_model,
                    "new_requirements": new_requirements
                },
                "outputs": response
            })
            with st.chat_message("assistant"):
                st.markdown(response)


elif action == "Gerar consultas SQL":
    current_model = st.text_area("Digite seu modelo de dados atual:", height=150)
    query_type = st.selectbox("Qual tipo de consulta você gostaria de gerar?", ["SELECT", "INSERT", "UPDATE", "DELETE"])
    if st.button("Gerar Consultas"):
        if current_model:
            response = generate_sql_queries(current_model, query_type)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.history.append({
                "function_name": "generate_sql_queries",
                "inputs": {
                    "current_model": current_model,
                    "query_type": query_type
                },
                "outputs": response
            })
            with st.chat_message("assistant"):
                st.markdown(response)


elif action == "Executar esquema JSON":
    schema_json = st.text_area("Digite o esquema JSON que deseja executar:", height=150)
    db_url = st.text_input("Digite o URL do banco de dados:")
    if st.button("Executar Esquema"):
        if schema_json and db_url:
            response = execute_schema(schema_json, db_url)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.session_state.history.append({
                "function_name": "execute_schema",
                "inputs": {
                    "schema_json": schema_json,
                    "db_url": db_url
                },
                "outputs": response
            })
            with st.chat_message("assistant"):
                st.markdown(response)


elif action == "Visualizar modelo de dados":
    input_option = st.selectbox("Como você gostaria de fornecer o modelo?", ["JSON", "SQL"])
    if input_option == "JSON":
        json_model = st.text_area("Cole o JSON do modelo de dados:", height=150)
        if st.button("Visualizar Modelo"):
            if json_model:
                dot = visualize_data_model(json_model=json_model)
                if dot:
                    st.graphviz_chart(dot.source, use_container_width=True)
    elif input_option == "SQL":
        sql_model = st.text_area("Cole o esquema SQL do modelo de dados:", height=150)
        if st.button("Visualizar Modelo"):
            if sql_model:
                dot = visualize_data_model(sql_model=sql_model)
                if dot:
                    st.graphviz_chart(dot.source)