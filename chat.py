from openai import AzureOpenAI  
from dotenv import load_dotenv
import os

def get_user_prompt():
    user_prompt = input('\nEnter Your Question:\n')
    return user_prompt


def append_message(messages, role, content):
    messages.append({
        "role": role,
        "content": content
    })
    
def build_prompt():
    return """
              Add Your System Prompt Here.
              """
    
def chat_prompt(system_message):
    return [
        {
            "role": "system",
            "content": system_message
        }
    ]


def get_search_results(client, messages, azure_oai_deployment, azure_search_endpoint, azure_search_index, azure_search_key, system_message, azure_embedding_deployment, Sematic_Configuration, Query_Type):
  # Generate the completion  
  completion = client.chat.completions.create(  
    model=azure_oai_deployment,
    messages=messages,
    max_tokens=800,  
    temperature=0.5,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False,
    extra_body={
      "data_sources": [{
          "type": "azure_search",
          "parameters": {
            "endpoint": azure_search_endpoint,
            "index_name": azure_search_index,
            "semantic_configuration": Sematic_Configuration,
            "query_type": Query_Type,
            "fields_mapping": {},
            "in_scope": True,
            "role_information": system_message,
            "filter": None,
            "strictness": 3,
            "top_n_documents": 5,
            "authentication": {
              "type": "api_key",
              "key": azure_search_key
            },
            "embedding_dependency": {
              "type": "deployment_name",
              "deployment_name": azure_embedding_deployment
            }
          }
        }]
    }
  )
  return completion.choices[0].message.content


def main():
    try:
        
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        azure_search_key = os.getenv("AZURE_SEARCH_KEY")
        azure_search_index = os.getenv("AZURE_SEARCH_INDEX")
        azure_embedding_deployment = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")
        Sematic_Configuration = os.getenv("Semantic_Configuration")
        Query_Type = os.getenv("Query_Type")                   
        
        # Initialize Azure OpenAI Service client with key-based authentication    
        client = AzureOpenAI(  
            azure_endpoint=azure_oai_endpoint,  
            api_key=azure_oai_key,  
            api_version="2024-05-01-preview",
        )
        system_message = build_prompt()
        messages = chat_prompt(system_message)
        
        while True:
            Student_Message = get_user_prompt()
            append_message(messages, "user", Student_Message)
            
            output = get_search_results(client, messages, azure_oai_deployment, azure_search_endpoint, azure_search_index, azure_search_key, system_message, azure_embedding_deployment, Sematic_Configuration, Query_Type)
        
            # Output the result
            print("\n--- Answer ---\n")
            print(output)
            append_message(messages, "assistant", output)
            
    except Exception as ex:
        print("An error occurred:", ex)

if __name__ == '__main__':
    main()
