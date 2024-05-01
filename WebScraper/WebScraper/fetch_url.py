import json
from duckduckgo_search import DDGS  # Import DDGS class for asynchronous usage
import asyncio
async def fetch_links(topic):
    input_text = str(topic)
   
    input_text_gfg = input_text + " by Geeks For Geeks"
    input_text_javat = input_text + " by Javatpoint"
    urls = []

    # Create an instance of DDGS
    ddgs = DDGS()

    # Fetch results for Geeks For Geeks
    results_gfg = ddgs.text(input_text_gfg, max_results=1)
    for result in results_gfg:
        urls.append(result["href"])

    # Fetch results for Javatpoint
    # results_javat =ddgs.text(input_text_javat, max_results=1)
    # for result in results_javat:
    #     urls.append(result["href"])

    return urls

# You can use asyncio to run the function and get the results
# Example usage:
# import asyncio
# urls = asyncio.run(fetch_links("Python async await"))
# print(urls)
