# simple_agent.py
import asyncio
import json
from anthropic import Anthropic
from mcp import ClientSession, StdioServerParameters

class SimpleFileAgent:
    def __init__(self, anthropic_api_key):
        self.anthropic = Anthropic(api_key=anthropic_api_key)
        self.mcp_session = None
        self.conversation_history = []
    
    async def connect_to_mcp_server(self):
        """Подключение к MCP серверу"""
        server_params = StdioServerParameters(
            command="python",
            args=["file_server.py"]
        )
        
        self.mcp_session = ClientSession(server_params)
        await self.mcp_session.initialize()
        
        # Получаем список доступных инструментов
        tools = await self.mcp_session.list_tools()
        print("Доступные инструменты:")
        for tool in tools.tools:
            print(f"- {tool.name}: {tool.description}")
    
    async def use_mcp_tool(self, tool_name, arguments):
        """Использование инструмента MCP сервера"""
        if not self.mcp_session:
            raise Exception("MCP сервер не подключен")
        
        result = await self.mcp_session.call_tool(tool_name, arguments)
        return result.content[0].text if result.content else "Нет результата"
    
    def analyze_request(self, user_input):
        """Анализ запроса пользователя для определения нужных действий"""
        system_prompt = """
        Ты помощник по работе с файлами. У тебя есть следующие инструменты:
        - list_files: показать файлы в директории
        - read_file: прочитать содержимое файла
        - create_file: создать новый файл
        - search_in_files: найти текст в файлах
        
        Проанализируй запрос пользователя и определи:
        1. Какой инструмент нужно использовать
        2. Какие параметры передать
        
        Ответь в формате JSON:
        {
            "tool": "название_инструмента",
            "arguments": {"параметр": "значение"},
            "explanation": "объяснение действия"
        }
        """
        
        response = self.anthropic.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=500,
            system=system_prompt,
            messages=[{
                "role": "user",
                "content": user_input
            }]
        )
        
        try:
            return json.loads(response.content[0].text)
        except:
            return {
                "tool": None,
                "arguments": {},
                "explanation": "Не удалось понять запрос"
            }
    
    async def process_request(self, user_input):
        """Обработка запроса пользователя"""
        print(f"\n🤖 Обрабатываю запрос: {user_input}")
        
        # Анализируем запрос
        analysis = self.analyze_request(user_input)
        print(f"📋 План действий: {analysis['explanation']}")
        
        if analysis['tool']:
            try:
                # Выполняем действие через MCP
                result = await self.use_mcp_tool(
                    analysis['tool'], 
                    analysis['arguments']
                )
                
                # Формируем ответ пользователю
                final_response = self.anthropic.messages.create(
                    model="claude-3-sonnet-20240229",
                    max_tokens=1000,
                    messages=[{
                        "role": "user",
                        "content": f"""
                        Пользователь спросил: {user_input}
                        
                        Я выполнил действие: {analysis['explanation']}
                        
                        Результат: {result}
                        
                        Сформулируй понятный ответ пользователю на основе этих данных.
                        """
                    }]
                )
                
                return final_response.content[0].text
                
            except Exception as e:
                return f"❌ Ошибка выполнения: {str(e)}"
        else:
            return "❓ Не понял, что нужно сделать. Попробуйте переформулировать запрос."

# Функция для запуска агента
async def main():
    # Замените на ваш API ключ Anthropic
    agent = SimpleFileAgent("your-anthropic-api-key")
    
    print("🚀 Запускаю AI агента...")
    await agent.connect_to_mcp_server()
    
    print("\n✅ Агент готов к работе!")
    print("Примеры команд:")
    print("- Покажи файлы в текущей папке")
    print("- Прочитай файл example.txt")
    print("- Создай файл test.txt с текстом 'Привет мир'")
    print("- Найди слово 'python' в файлах")
    
    while True:
        try:
            user_input = input("\n👤 Ваш запрос: ")
            if user_input.lower() in ['выход', 'quit', 'exit']:
                break
                
            response = await agent.process_request(user_input)
            print(f"\n🤖 Ответ: {response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Ошибка: {str(e)}")
    
    print("\n👋 До свидания!")

if __name__ == "__main__":
    asyncio.run(main())
