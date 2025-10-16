"""Configuration settings for the Senegal Orientation Chatbot."""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict # type: ignore
from pydantic import Field # type: ignore


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Application
    app_name: str = Field(default="Chatbot Orientation Sénégal", alias="APP_NAME")
    debug: bool = Field(default=False, alias="DEBUG")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    environment: str = Field(default="development", alias="ENVIRONMENT")
    
    # PostgreSQL
    postgres_host: str = Field(default="localhost", alias="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, alias="POSTGRES_PORT")
    postgres_db: str = Field(default="senegal_orientation_db", alias="POSTGRES_DB")
    postgres_user: str = Field(default="postgres", alias="POSTGRES_USER")
    postgres_password: str = Field(default="postgres", alias="POSTGRES_PASSWORD")
    
    # Ollama
    ollama_host: str = Field(default="http://localhost:11434", alias="OLLAMA_HOST")
    ollama_model: str = Field(default="llama3.2", alias="OLLAMA_MODEL")
    embedding_model: str = Field(default="nomic-embed-text", alias="EMBEDDING_MODEL")
    
    # Streamlit
    streamlit_server_port: int = Field(default=8501, alias="STREAMLIT_SERVER_PORT")
    streamlit_server_address: str = Field(default="0.0.0.0", alias="STREAMLIT_SERVER_ADDRESS")
    streamlit_server_headless: bool = Field(default=True, alias="STREAMLIT_SERVER_HEADLESS")
    
    # Vector Store
    vector_dimension: int = Field(default=768, alias="VECTOR_DIMENSION")
    similarity_threshold: float = Field(default=0.7, alias="SIMILARITY_THRESHOLD")
    top_k_results: int = Field(default=5, alias="TOP_K_RESULTS")
    chunk_size: int = Field(default=500, alias="CHUNK_SIZE")
    chunk_overlap: int = Field(default=50, alias="CHUNK_OVERLAP")
    
    # Security
    secret_key: str = Field(default="change-this-secret-key", alias="SECRET_KEY")
    api_key: Optional[str] = Field(default=None, alias="API_KEY")
    
    # FastAPI
    api_host: str = Field(default="0.0.0.0", alias="API_HOST")
    api_port: int = Field(default=8000, alias="API_PORT")
    api_reload: bool = Field(default=True, alias="API_RELOAD")
    
    # LLM Parameters
    temperature: float = Field(default=0.7, alias="TEMPERATURE")
    max_tokens: int = Field(default=2000, alias="MAX_TOKENS")
    context_window: int = Field(default=4096, alias="CONTEXT_WINDOW")
    
    # Admin
    admin_username: str = Field(default="admin", alias="ADMIN_USERNAME")
    admin_password: str = Field(default="changeme", alias="ADMIN_PASSWORD")
    
    @property
    def database_url(self) -> str:
        """Get the full database URL."""
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )
    
    @property
    def async_database_url(self) -> str:
        """Get the async database URL."""
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


# Create a singleton instance
settings = Settings()
