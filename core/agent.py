from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from semantic_kernel.connectors.ai.ollama import OllamaChatPromptExecutionSettings
from typing import List
from plugin.serpapi import WebSearchPlugin
from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior

class SemanticKernelAgent:
    def __init__(self, web_search_plugin: WebSearchPlugin):
        self.kernel = Kernel()
        service_id = "ollama"
        self.kernel.add_service(
            OllamaChatCompletion(
                service_id=service_id,
                host="http://localhost:11434",
                ai_model_id="llama3.2:latest",
            )
        )

        self.system_prompt = "Il tuo obiettivo è rispondere alle domande dell'utente utilizzando le informazioni disponibili."
        self.execution_settings: OllamaChatPromptExecutionSettings = self.kernel.get_prompt_execution_settings_from_service_id(
            service_id, OllamaChatCompletion
        )
        
        # Configurazione delle opzioni di Ollama
        self.execution_settings.options = {
            "num_predict": 2000,  # Equivalente a max_tokens
            "temperature": 0.1,
            "top_p": 0.8
        }
        
        self.execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto(filters={"excluded_plugins": ["ask_plugin"]})

        self.kernel.add_plugin(web_search_plugin, plugin_name="web_search_plugin")

        self.ask_function = self.kernel.add_function(
            function_name="ask_function",
            plugin_name="ask_plugin",
            prompt="{{$system_prompt}}{{$user_input}}",
            prompt_execution_settings=self.execution_settings,
        )

    async def ask(self, question: str) -> str:
    
        return await self.kernel.invoke(
        self.ask_function, KernelArguments(settings=self.execution_settings, user_input=question, system_prompt=self.system_prompt)
    )

