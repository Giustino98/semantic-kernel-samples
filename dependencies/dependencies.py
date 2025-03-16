from core.agent import SemanticKernelAgent
from plugin.serpapi import WebSearchPlugin
def get_websearch_agent():
    web_search_plugin = WebSearchPlugin()
    return SemanticKernelAgent(web_search_plugin)