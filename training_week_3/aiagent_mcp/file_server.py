# file_server.py
from fastmcp import FastMCP
import os
import json
from pathlib import Path

# Создание MCP сервера
mcp = FastMCP("Simple File Server")

@mcp.tool()
def list_files(directory: str = ".") -> str:
    """Получить список файлов в указанной директории"""
    try:
        files = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            file_info = {
                "name": item,
                "type": "directory" if os.path.isdir(item_path) else "file",
                "size": os.path.getsize(item_path) if os.path.isfile(item_path) else 0
            }
            files.append(file_info)
        
        return json.dumps(files, indent=2)
    except Exception as e:
        return f"Ошибка: {str(e)}"

@mcp.tool()
def read_file(filepath: str) -> str:
    """Прочитать содержимое файла"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Ошибка чтения файла: {str(e)}"

@mcp.tool()
def create_file(filepath: str, content: str) -> str:
    """Создать новый файл с указанным содержимым"""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Файл {filepath} успешно создан"
    except Exception as e:
        return f"Ошибка создания файла: {str(e)}"

@mcp.tool()
def search_in_files(directory: str, search_term: str) -> str:
    """Поиск текста в файлах директории"""
    results = []
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(('.txt', '.py', '.md', '.json')):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if search_term.lower() in content.lower():
                                results.append({
                                    "file": filepath,
                                    "matches": content.lower().count(search_term.lower())
                                })
                    except:
                        continue
        
        return json.dumps(results, indent=2)
    except Exception as e:
        return f"Ошибка поиска: {str(e)}"

if __name__ == "__main__":
    mcp.run()
