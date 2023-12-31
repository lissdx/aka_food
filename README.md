# AKA FOOD POC
This is a simple POC project created by AKA FOOD project  
Python version: I've used 3.12

## How to Run Locally:
### Pre-Requirements:
1. Your system should support docker-compose
2. Optional: install cli jq 

### Setup ElasticSearch DB
1. Start ES stack:  
    from project root run  
    `make elk-local-up`
2. Prepare the ES data
   1. normalize your source files    
        `cat <data_source_file>.json | jq '.[]' | jq -c > <normalized_output>.json`
   2. upload the normalized files to ES via Kibana UI
3. If you've changed default values of ELK update the _config.py_ file 

### Setup Hugging Face
1. register on Hugging Face
2. get your [Hugging Face Token](http://hf.co/settings/tokens)  
3. export the given Hugging Face Token into your project's running env  
    `export HF_TOKEN=<your_hf_given_token>`

### Run Flask Server
1. `python app.py` 
    Note: It may be depended on your system setup
2. check endpoint are working:
   * /akafood/health  
     `curl --location 'http://127.0.0.1:7889/akafood/health'`  
   * /akafood/find/byingredient   
     `curl --location 'http://127.0.0.1:7889/akafood/find/byingredient/eggs'`  
   * /akafood/find/sentence_similarity  
   `curl --location 'http://127.0.0.1:7889/akafood/find/sentence_similarity?q=bread%20pudding%20%20carrot'`
3. Note: the host and port may be different. check your _config.py_ 
4. instead of _curl_ you welcome to use any other tool, like standard browser, postman etc...
