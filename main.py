from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="NLP to SQL API", version="1.0.0")

# Add CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class NLPRequest(BaseModel):
    query: str
    schema_info: str = ""  # Optional table schema info

class SQLResponse(BaseModel):
    sql_query: str
    confidence: str = "medium"
    explanation: str = ""

@app.get("/")
async def root():
    return {"message": "NLP to SQL API is running"}

@app.get("/health")
async def health_check():
    try:
        # Test if Ollama is running
        response = ollama.list()
        return {"status": "healthy", "ollama": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

@app.post("/convert-to-sql", response_model=SQLResponse)
async def convert_nlp_to_sql(request: NLPRequest):
    try:
        # Build prompt for SQLCoder
        prompt = f"""
Convert the following natural language query to SQL:

Query: {request.query}

Schema Information: {request.schema_info if request.schema_info else "No schema provided"}

Instructions:
- Generate only valid SQL syntax
- Use standard SQL conventions
- If schema is provided, use the exact table and column names
- Keep the query simple and efficient

SQL:
"""
        
        # Call Ollama with SQLCoder model
        response = ollama.generate(
            model='sqlcoder:7b',
            prompt=prompt,
            stream=False
        )
        
        generated_sql = response['response'].strip()
        
        # Basic cleanup - remove any markdown formatting
        if "```sql" in generated_sql:
            generated_sql = generated_sql.split("```sql")[1].split("```")[0].strip()
        elif "```" in generated_sql:
            generated_sql = generated_sql.split("```")[1].split("```")[0].strip()
        
        return SQLResponse(
            sql_query=generated_sql,
            confidence="medium",
            explanation=f"Converted: '{request.query}' to SQL"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating SQL: {str(e)}")

@app.get("/models")
async def list_models():
    """List available Ollama models"""
    try:
        models = ollama.list()
        return {"models": models}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)