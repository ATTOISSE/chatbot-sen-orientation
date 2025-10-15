# 🎓 Chatbot d'Orientation Sénégal

Un chatbot intelligent d'orientation académique et professionnelle pour le Sénégal utilisant RAG (Retrieval-Augmented Generation) avec Ollama, PostgreSQL et Streamlit.

## 🎯 Objectif du Projet

Fournir un assistant virtuel intelligent pour aider les étudiants sénégalais à :
- Découvrir les formations disponibles selon leurs intérêts
- Explorer les établissements d'enseignement supérieur
- Comprendre les débouchés professionnels
- Naviguer dans le système éducatif sénégalais
- Obtenir des conseils d'orientation personnalisés

## ✨ Fonctionnalités

- 💬 **Chat Intelligent** : Conversation naturelle avec l'assistant d'orientation
- 🔍 **Recherche Sémantique** : Recherche avancée de formations par RAG
- 📊 **Statistiques** : Visualisation des données sur les formations et conversations
- 🎯 **Filtres Avancés** : Filtrage par domaine, niveau, localisation
- 📚 **Base de Données Complète** : Informations sur les formations et établissements
- 🤖 **IA Contextuelle** : Réponses adaptées au système éducatif sénégalais

## 🛠️ Technologies Utilisées

- **Backend** : Python 3.10+, FastAPI
- **Frontend** : Streamlit
- **Base de Données** : PostgreSQL + pgvector
- **LLM** : Ollama (Llama 3.2)
- **Embeddings** : nomic-embed-text
- **Orchestration** : LangChain
- **Conteneurisation** : Docker & Docker Compose

## 📋 Prérequis

- Python 3.10 ou supérieur
- PostgreSQL 15 avec extension pgvector
- Ollama installé et en cours d'exécution
- Docker et Docker Compose (pour le déploiement)

## � Installation

### Option 1 : Installation Locale

1. **Cloner le repository**
```bash
git clone https://github.com/ATTOISSE/chatbot-sen-orientation.git
cd chatbot-sen-orientation
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**
```bash
cp .env.example .env
# Éditer .env avec vos configurations
```

5. **Installer et démarrer Ollama**
```bash
# Télécharger Ollama depuis https://ollama.ai
# Puis télécharger les modèles
ollama pull llama3.2
ollama pull nomic-embed-text
```

6. **Initialiser la base de données**
```bash
python scripts/init_database.py
```

7. **Ingérer les données**
```bash
python scripts/ingest_data.py
```

8. **Lancer l'application**
```bash
streamlit run streamlit_app/app.py
```

### Option 2 : Docker Compose (Recommandé)

1. **Cloner et configurer**
```bash
git clone https://github.com/ATTOISSE/chatbot-sen-orientation.git
cd chatbot-sen-orientation
cp .env.example .env
```

2. **Démarrer les services**
```bash
docker-compose up -d
```

3. **Initialiser la base de données**
```bash
docker-compose exec backend python scripts/init_database.py
docker-compose exec backend python scripts/ingest_data.py
```

4. **Accéder à l'application**
- Streamlit : http://localhost:8501
- API : http://localhost:8000/docs

## 📖 Utilisation

### Interface Streamlit

1. Ouvrez votre navigateur à `http://localhost:8501`
2. Naviguez vers la page Chat (💬)
3. Posez vos questions sur l'orientation
4. Utilisez les filtres pour affiner les résultats

### API REST

Documentation Swagger disponible à `http://localhost:8000/docs`

Exemple de requête :
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Quelles formations en informatique à Dakar ?",
    "session_id": "test-session"
  }'
```

## 📁 Structure du Projet

```
chatbot-sen-orientation/
├── config/              # Configuration (settings, prompts)
├── data/               # Données (raw, processed, vector_store)
├── src/                # Code source
│   ├── database/       # Modèles et CRUD
│   ├── embeddings/     # Génération d'embeddings
│   ├── llm/           # Intégration LLM
│   ├── retrieval/      # Système de récupération
│   ├── agents/         # Agent conversationnel
│   └── utils/          # Utilitaires
├── streamlit_app/      # Interface Streamlit
├── api/                # API FastAPI
├── scripts/            # Scripts d'initialisation
├── tests/              # Tests
├── docker/             # Configuration Docker
└── docs/               # Documentation

```

## 🧪 Tests

```bash
# Exécuter tous les tests
pytest

# Avec couverture
pytest --cov=src tests/

# Tests spécifiques
pytest tests/test_agent.py
```

## 📚 Documentation Complète

Pour le guide de développement complet (étape par étape), voir ci-dessous.

---

## ÉTAPE 1 : Configuration Initiale du Projet

### Objectif
Créer la structure complète du projet et les fichiers de configuration de base.

### Actions à réaliser

1. **Créer l'arborescence complète** selon la structure fournie :
```
senegal-orientation-chatbot/
├── config/ (settings, prompts)
├── data/ (raw, processed, vector_store)
├── src/ (database, embeddings, llm, retrieval, agents, utils)
├── streamlit_app/ (pages, components, .streamlit)
├── api/ (routes)
├── scripts/
├── tests/
├── migrations/
├── docker/
└── logs/
```

2. **Créer le fichier `.gitignore`** avec :
   - Exclusions Python (__pycache__, *.pyc, venv/, env/)
   - Exclusions environnement (.env, .env.local)
   - Exclusions données (data/raw/*, data/processed/*, *.pkl)
   - Exclusions logs (logs/*.log)
   - Exclusions IDE (.vscode/, .idea/)
   - Exclusions Docker (docker-compose.override.yml)

3. **Créer le fichier `.env.example`** avec les variables :
   - PostgreSQL : POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
   - Ollama : OLLAMA_HOST, OLLAMA_MODEL, EMBEDDING_MODEL
   - Application : APP_NAME, DEBUG, LOG_LEVEL
   - Streamlit : STREAMLIT_SERVER_PORT, STREAMLIT_SERVER_ADDRESS
   - Vector Store : VECTOR_DIMENSION, SIMILARITY_THRESHOLD, TOP_K_RESULTS
   - Security : SECRET_KEY

4. **Créer un README.md initial** avec :
   - Description du projet
   - Technologies utilisées
   - Instructions d'installation
   - Structure du projet

5. **Initialiser Git** et créer le premier commit

### Commit
```bash
git add .
git commit -m "feat: initial project structure and configuration files"
```

---

## ÉTAPE 2 : Configuration des Dépendances

### Objectif
Définir toutes les dépendances Python et créer les fichiers d'initialisation des packages.

### Actions à réaliser

1. **Créer `requirements.txt`** avec les bibliothèques :
   - Frameworks : streamlit, fastapi, uvicorn
   - Base de données : psycopg2-binary, sqlalchemy, alembic, pgvector
   - LLM : langchain, langchain-community, ollama
   - Vector Store : chromadb ou faiss-cpu
   - Utils : pandas, numpy, python-dotenv, httpx
   - Testing : pytest, pytest-asyncio, pytest-cov

2. **Créer tous les fichiers `__init__.py`** dans :
   - config/
   - src/ et tous ses sous-répertoires
   - streamlit_app/ et ses sous-répertoires
   - api/ et api/routes/
   - tests/

3. **Créer `setup.py`** pour rendre le projet installable

### Commit
```bash
git add requirements.txt setup.py **/__init__.py
git commit -m "feat: add Python dependencies and package initialization"
```

---

## ÉTAPE 3 : Configuration du Projet (config/)

### Objectif
Créer les fichiers de configuration centralisés pour l'application.

### Actions à réaliser

1. **Créer `config/settings.py`** :
   - Classe `Settings` utilisant Pydantic BaseSettings
   - Charger les variables d'environnement depuis .env
   - Définir les configurations : database, ollama, vector_store, app
   - Créer une instance singleton `settings`

2. **Créer `config/prompts.py`** :
   - Template de prompt système pour l'orientation
   - Template de prompt pour la recherche de formations
   - Template de prompt pour les conseils d'orientation
   - Instructions de formatage des réponses
   - Contexte spécifique au Sénégal (système éducatif, formations disponibles)

3. **Tester l'import** :
```python
from config.settings import settings
from config.prompts import SYSTEM_PROMPT
```

### Commit
```bash
git add config/
git commit -m "feat: add configuration files with settings and prompts"
```

---

## ÉTAPE 4 : Base de Données (src/database/)

### Objectif
Configurer la base de données PostgreSQL avec pgvector et créer les modèles SQLAlchemy.

### Actions à réaliser

1. **Créer `src/database/connection.py`** :
   - Fonction `get_engine()` : créer le moteur SQLAlchemy
   - Fonction `get_session()` : générateur de sessions
   - Fonction `init_db()` : initialiser les tables et l'extension pgvector
   - Gestion des connexions asynchrones (optionnel)

2. **Créer `src/database/models.py`** :
   - Modèle `Formation` : id, titre, description, domaine, niveau, duree, etablissement, localisation, prerequisites, debouches, created_at, updated_at
   - Modèle `Etablissement` : id, nom, type, ville, contact
   - Modèle `Conversation` : id, session_id, user_message, bot_response, timestamp
   - Modèle `DocumentEmbedding` : id, content, embedding (vector), metadata, source
   - Relations entre modèles

3. **Créer `src/database/crud.py`** :
   - Fonctions CRUD pour Formation : create, read, update, delete, search
   - Fonctions CRUD pour Etablissement
   - Fonctions pour Conversation : save_conversation, get_history
   - Fonctions pour DocumentEmbedding : insert_embedding, search_similar

4. **Créer `migrations/alembic.ini`** et initialiser Alembic

5. **Créer `scripts/init_database.py`** :
   - Script pour créer les tables
   - Activer l'extension pgvector
   - Insérer des données de test

### Commit
```bash
git add src/database/ migrations/ scripts/init_database.py
git commit -m "feat: setup database models, CRUD operations and migrations"
```

---

## ÉTAPE 5 : Embeddings et Vector Store (src/embeddings/)

### Objectif
Implémenter la génération d'embeddings et le stockage vectoriel.

### Actions à réaliser

1. **Créer `src/embeddings/generator.py`** :
   - Classe `EmbeddingGenerator` :
     - Initialiser avec le modèle Ollama (nomic-embed-text)
     - Méthode `generate_embedding(text)` : générer un embedding
     - Méthode `generate_batch_embeddings(texts)` : traiter par batch
     - Gestion du cache pour éviter les recalculs

2. **Créer `src/embeddings/vector_store.py`** :
   - Classe `VectorStore` :
     - Initialiser avec connexion PostgreSQL + pgvector
     - Méthode `add_documents(documents, embeddings)` : stocker
     - Méthode `similarity_search(query_embedding, k)` : recherche
     - Méthode `delete_by_source(source)` : nettoyage
     - Index pour optimiser les recherches

3. **Créer `scripts/ingest_data.py`** :
   - Charger les données depuis data/raw/
   - Découper les documents en chunks
   - Générer les embeddings
   - Stocker dans la base de données
   - Afficher les statistiques d'ingestion

### Commit
```bash
git add src/embeddings/ scripts/ingest_data.py
git commit -m "feat: implement embeddings generation and vector store"
```

---

## ÉTAPE 6 : Intégration LLM (src/llm/)

### Objectif
Configurer Ollama et créer les chaînes LangChain pour le chatbot.

### Actions à réaliser

1. **Créer `src/llm/model.py`** :
   - Classe `OllamaModel` :
     - Initialiser la connexion Ollama
     - Méthode `generate(prompt, context)` : génération simple
     - Méthode `stream_generate(prompt, context)` : génération en streaming
     - Gestion des erreurs de connexion
     - Configuration des paramètres (temperature, max_tokens)

2. **Créer `src/llm/chains.py`** :
   - Fonction `create_rag_chain()` : créer une chaîne RAG complète
   - Fonction `create_conversational_chain()` : avec historique
   - Intégration des prompts depuis config/prompts.py
   - Formatage du contexte récupéré
   - Gestion de la mémoire conversationnelle

### Commit
```bash
git add src/llm/
git commit -m "feat: integrate Ollama LLM and create LangChain chains"
```

---

## ÉTAPE 7 : Système de Récupération (src/retrieval/)

### Objectif
Implémenter le système de récupération et de reranking des documents pertinents.

### Actions à réaliser

1. **Créer `src/retrieval/retriever.py`** :
   - Classe `DocumentRetriever` :
     - Initialiser avec VectorStore et EmbeddingGenerator
     - Méthode `retrieve(query, k, filters)` : récupérer documents
     - Méthode `retrieve_with_scores(query, k)` : avec scores de similarité
     - Filtrage par domaine, niveau, localisation
     - Formatage des résultats pour le LLM

2. **Créer `src/retrieval/reranker.py`** :
   - Classe `Reranker` :
     - Méthode `rerank(query, documents)` : réordonner par pertinence
     - Algorithme de reranking (BM25 ou cross-encoder)
     - Combinaison des scores vectoriels et sémantiques

### Commit
```bash
git add src/retrieval/
git commit -m "feat: implement document retrieval and reranking system"
```

---

## ÉTAPE 8 : Agent Chatbot (src/agents/)

### Objectif
Créer l'agent conversationnel principal qui orchestre toutes les composantes.

### Actions à réaliser

1. **Créer `src/agents/chatbot_agent.py`** :
   - Classe `OrientationAgent` :
     - Initialiser tous les composants (retriever, llm, vector_store)
     - Méthode `chat(user_message, session_id)` : traiter une requête
     - Méthode `get_chat_history(session_id)` : récupérer l'historique
     - Méthode `search_formations(criteria)` : recherche spécifique
     - Détection d'intention (orientation, information, recherche)
     - Sauvegarde des conversations
     - Gestion des erreurs et fallbacks

### Commit
```bash
git add src/agents/
git commit -m "feat: create main chatbot agent with conversation orchestration"
```

---

## ÉTAPE 9 : Utilitaires (src/utils/)

### Objectif
Créer les fonctions utilitaires pour le traitement des données et la validation.

### Actions à réaliser

1. **Créer `src/utils/data_loader.py`** :
   - Fonction `load_formations_from_csv(filepath)` : charger CSV
   - Fonction `load_formations_from_json(filepath)` : charger JSON
   - Fonction `validate_formation_data(data)` : valider structure
   - Fonction `parse_pdf_documents(directory)` : extraire texte PDF

2. **Créer `src/utils/text_splitter.py`** :
   - Classe `SemanticTextSplitter` :
     - Découper texte en chunks sémantiques
     - Conserver le contexte entre chunks
     - Paramètres : chunk_size, chunk_overlap

3. **Créer `src/utils/validators.py`** :
   - Fonction `validate_user_input(text)` : nettoyer input utilisateur
   - Fonction `validate_filters(filters)` : valider filtres recherche
   - Fonction `sanitize_output(text)` : nettoyer réponse LLM

### Commit
```bash
git add src/utils/
git commit -m "feat: add utility functions for data processing and validation"
```

---

## ÉTAPE 10 : Interface Streamlit - Page Principale (streamlit_app/)

### Objectif
Créer l'interface utilisateur principale avec Streamlit.

### Actions à réaliser

1. **Créer `streamlit_app/.streamlit/config.toml`** :
   - Configuration du thème
   - Configuration du serveur
   - Paramètres de performance

2. **Créer `streamlit_app/app.py`** :
   - Configuration de la page (title, icon, layout)
   - Sidebar avec navigation
   - Page d'accueil avec présentation
   - Initialisation de session_state
   - Import et setup de l'agent

3. **Créer `streamlit_app/components/chat_interface.py`** :
   - Fonction `render_chat_interface()` :
     - Affichage de l'historique des messages
     - Input utilisateur avec st.chat_input
     - Affichage des réponses en streaming
     - Gestion des avatars (user/assistant)
     - Bouton pour effacer l'historique

4. **Créer `streamlit_app/components/filters.py`** :
   - Fonction `render_filters()` :
     - Filtres par domaine (multiselect)
     - Filtres par niveau (selectbox)
     - Filtres par localisation (multiselect)
     - Bouton de réinitialisation
     - Retourner un dictionnaire de filtres

### Commit
```bash
git add streamlit_app/app.py streamlit_app/components/ streamlit_app/.streamlit/
git commit -m "feat: create main Streamlit interface with chat component"
```

---

## ÉTAPE 11 : Pages Streamlit Additionnelles

### Objectif
Créer les pages supplémentaires pour les statistiques, recherche et administration.

### Actions à réaliser

1. **Créer `streamlit_app/pages/1_💬_Chat.py`** :
   - Page de chat interactive
   - Utiliser le composant chat_interface
   - Filtres dans la sidebar
   - Suggestions de questions
   - Export de la conversation

2. **Créer `streamlit_app/pages/2_📊_Statistiques.py`** :
   - Statistiques sur les conversations
   - Graphiques (formations populaires, domaines recherchés)
   - Métriques clés (nombre de requêtes, taux de satisfaction)
   - Utiliser Plotly ou Altair pour les visualisations

3. **Créer `streamlit_app/pages/3_🔍_Recherche.py`** :
   - Recherche avancée de formations
   - Filtres multiples
   - Affichage en grille ou liste
   - Détails de chaque formation
   - Comparaison de formations

4. **Créer `streamlit_app/pages/4_⚙️_Admin.py`** :
   - Authentification simple
   - Gestion des formations (CRUD)
   - Réindexation des embeddings
   - Logs et monitoring
   - Configuration du modèle

5. **Créer `streamlit_app/components/visualizations.py`** :
   - Fonction `plot_domain_distribution(data)` : graphique des domaines
   - Fonction `plot_conversation_stats(data)` : stats temporelles
   - Fonction `display_formation_card(formation)` : carte formation

### Commit
```bash
git add streamlit_app/pages/
git commit -m "feat: add additional Streamlit pages for stats, search and admin"
```

---

## ÉTAPE 12 : API FastAPI (Optionnel)

### Objectif
Créer une API REST pour permettre l'intégration externe du chatbot.

### Actions à réaliser

1. **Créer `api/main.py`** :
   - Application FastAPI
   - Configuration CORS
   - Middleware de logging
   - Documentation Swagger
   - Health check endpoint

2. **Créer `api/dependencies.py`** :
   - Dépendance `get_db()` : session database
   - Dépendance `get_agent()` : instance agent
   - Dépendance `verify_api_key()` : authentification

3. **Créer `api/routes/chat.py`** :
   - POST `/chat` : envoyer message
   - POST `/chat/stream` : réponse en streaming
   - GET `/chat/history/{session_id}` : historique
   - DELETE `/chat/history/{session_id}` : effacer

4. **Créer `api/routes/formations.py`** :
   - GET `/formations` : liste avec filtres
   - GET `/formations/{id}` : détails
   - POST `/formations/search` : recherche sémantique
   - GET `/formations/domains` : liste des domaines

5. **Créer `api/routes/admin.py`** :
   - POST `/admin/formations` : créer formation
   - PUT `/admin/formations/{id}` : modifier
   - DELETE `/admin/formations/{id}` : supprimer
   - POST `/admin/reindex` : réindexer embeddings

### Commit
```bash
git add api/
git commit -m "feat: create FastAPI REST API for external integrations"
```

---

## ÉTAPE 13 : Docker Configuration

### Objectif
Conteneuriser l'application avec Docker et Docker Compose.

### Actions à réaliser

1. **Créer `docker/Dockerfile.backend`** :
   - Base Python 3.10
   - Installation des dépendances
   - Copie du code source
   - Configuration du WORKDIR
   - CMD pour lancer l'API ou les scripts

2. **Créer `docker/Dockerfile.streamlit`** :
   - Base Python 3.10
   - Installation des dépendances
   - Copie de streamlit_app/
   - Exposition du port 8501
   - CMD streamlit run app.py

3. **Créer `docker/Dockerfile.ollama`** :
   - Base ollama/ollama
   - Téléchargement des modèles
   - Configuration des volumes

4. **Créer `docker/nginx.conf`** :
   - Configuration reverse proxy
   - Routes vers Streamlit et API
   - SSL/TLS (optionnel)

5. **Créer `docker-compose.yml`** :
   - Service `postgres` : PostgreSQL 15 avec pgvector
   - Service `ollama` : Ollama avec GPU (optionnel)
   - Service `backend` : API FastAPI
   - Service `streamlit` : Interface Streamlit
   - Service `nginx` : Reverse proxy
   - Networks et volumes
   - Variables d'environnement
   - Health checks

6. **Créer `docker-compose.prod.yml`** :
   - Overrides pour production
   - Pas de volumes de développement
   - Logs configurés
   - Restart policies

7. **Créer `scripts/entrypoint.sh`** :
   - Attendre que PostgreSQL soit prêt
   - Exécuter les migrations
   - Initialiser les données
   - Lancer l'application

8. **Créer `scripts/wait-for-it.sh`** :
   - Script pour attendre la disponibilité des services

### Commit
```bash
git add docker/ docker-compose*.yml scripts/entrypoint.sh scripts/wait-for-it.sh
git commit -m "feat: add Docker configuration for all services"
```

---

## ÉTAPE 14 : Scripts d'Initialisation et Maintenance

### Objectif
Créer les scripts pour initialiser, maintenir et mettre à jour le système.

### Actions à réaliser

1. **Améliorer `scripts/init_database.py`** :
   - Créer les tables si elles n'existent pas
   - Charger les données initiales depuis data/raw/
   - Créer un utilisateur admin par défaut
   - Afficher un rapport de l'initialisation

2. **Améliorer `scripts/ingest_data.py`** :
   - Argument pour spécifier la source de données
   - Support CSV, JSON, PDF
   - Traitement par batch avec barre de progression
   - Validation des données avant insertion
   - Rapport détaillé avec statistiques

3. **Créer `scripts/update_vectors.py`** :
   - Régénérer les embeddings pour tous les documents
   - Option pour mettre à jour uniquement les nouveaux
   - Gestion de l'historique des versions
   - Backup avant mise à jour

4. **Créer `scripts/backup_database.py`** :
   - Export de la base de données
   - Export des embeddings
   - Compression et horodatage

5. **Créer `scripts/test_ollama.py`** :
   - Tester la connexion à Ollama
   - Vérifier les modèles disponibles
   - Générer un embedding de test
   - Générer une réponse de test

### Commit
```bash
git add scripts/
git commit -m "feat: add initialization and maintenance scripts"
```

---

## ÉTAPE 15 : Tests Unitaires et d'Intégration

### Objectif
Créer une suite de tests complète pour assurer la qualité du code.

### Actions à réaliser

1. **Créer `tests/conftest.py`** :
   - Fixtures pytest pour la base de données de test
   - Fixture pour l'agent
   - Fixture pour les données de test
   - Configuration de l'environnement de test

2. **Créer `tests/test_embeddings.py`** :
   - Test de génération d'embeddings
   - Test de la dimension des vecteurs
   - Test du batch processing
   - Test du cache

3. **Créer `tests/test_retrieval.py`** :
   - Test de recherche de similarité
   - Test des filtres
   - Test du reranking
   - Test de la pertinence des résultats

4. **Créer `tests/test_llm.py`** :
   - Test de génération de réponse
   - Test du streaming
   - Test de gestion du contexte
   - Test des erreurs de connexion

5. **Créer `tests/test_crud.py`** :
   - Test des opérations CRUD sur formations
   - Test des relations entre modèles
   - Test de la recherche dans la base
   - Test de la sauvegarde des conversations

6. **Créer `tests/test_agent.py`** :
   - Test du flux complet de conversation
   - Test de la détection d'intention
   - Test de l'historique conversationnel
   - Test des edge cases

### Commit
```bash
git add tests/
git commit -m "feat: add comprehensive test suite"
```

---

## ÉTAPE 16 : Documentation et CI/CD

### Objectif
Finaliser la documentation et configurer l'intégration continue.

### Actions à réaliser

1. **Améliorer `README.md`** :
   - Description détaillée du projet
   - Architecture du système
   - Guide d'installation complet
   - Guide d'utilisation
   - Guide de contribution
   - Exemples de requêtes
   - Troubleshooting
   - Crédits et licence

2. **Créer `docs/ARCHITECTURE.md`** :
   - Diagramme d'architecture
   - Description des composants
   - Flux de données
   - Décisions techniques

3. **Créer `docs/API.md`** :
   - Documentation complète de l'API
   - Exemples de requêtes/réponses
   - Codes d'erreur
   - Authentification

4. **Créer `docs/DEPLOYMENT.md`** :
   - Guide de déploiement en production
   - Configuration du serveur
   - Monitoring et logs
   - Backup et restauration
   - Scaling

5. **Créer `docs/CONTRIBUTING.md`** :
   - Comment contribuer
   - Standards de code
   - Processus de PR
   - Guide de développement

6. **Créer `.github/workflows/ci.yml`** :
   - Workflow GitHub Actions
   - Linting (flake8, black)
   - Tests (pytest)
   - Coverage
   - Build Docker
   - Déploiement automatique (optionnel)

7. **Créer `pyproject.toml`** ou `.flake8` :
   - Configuration des outils de qualité de code
   - Configuration de Black
   - Configuration de isort

### Commit
```bash
git add README.md docs/ .github/ pyproject.toml
git commit -m "docs: complete documentation and setup CI/CD pipeline"
```

---

## ÉTAPE 17 : Préparation des Données Initiales

### Objectif
Préparer et formater les données initiales de formations sénégalaises.

### Actions à réaliser

1. **Créer `data/raw/formations_senegal.csv`** :
   - Colonnes : id, titre, description, domaine, niveau, duree, etablissement, ville, prerequisites, debouches, contact
   - Au moins 50 formations variées
   - Couvrir différents domaines (technologie, santé, commerce, arts, etc.)
   - Différents niveaux (BTS, Licence, Master, Formation professionnelle)

2. **Créer `data/raw/etablissements.json`** :
   - Liste des établissements sénégalais
   - Informations : nom, type, ville, contact, site web

3. **Créer `data/raw/systeme_educatif_senegal.txt`** :
   - Description du système éducatif sénégalais
   - Parcours possibles après le bac
   - Équivalences de diplômes
   - Informations sur les concours

4. **Créer un script de validation** :
   - Vérifier la cohérence des données
   - Détecter les doublons
   - Valider les formats

### Commit
```bash
git add data/raw/
git commit -m "data: add initial dataset of Senegalese formations"
```

---

## ÉTAPE 18 : Tests d'Intégration Complète

### Objectif
Tester l'ensemble du système de bout en bout.

### Actions à réaliser

1. **Lancer les services Docker** :
```bash
docker-compose up -d
```

2. **Initialiser la base de données** :
```bash
docker-compose exec backend python scripts/init_database.py
```

3. **Ingérer les données** :
```bash
docker-compose exec backend python scripts/ingest_data.py
```

4. **Tester l'interface Streamlit** :
   - Accéder à http://localhost:8501
   - Tester plusieurs conversations
   - Tester les filtres
   - Tester la recherche
   - Vérifier les statistiques

5. **Tester l'API** :
   - Accéder à http://localhost:8000/docs
   - Tester les endpoints
   - Vérifier les réponses

6. **Créer `tests/test_e2e.py`** :
   - Test de bout en bout
   - Simulation d'une session utilisateur complète
   - Vérification de la cohérence des réponses

7. **Documenter les bugs trouvés** :
   - Créer des issues GitHub si nécessaire
   - Corriger les bugs critiques

### Commit
```bash
git add tests/test_e2e.py
git commit -m "test: add end-to-end integration tests"
```

---

## ÉTAPE 19 : Optimisations et Améliorations

### Objectif
Optimiser les performances et améliorer l'expérience utilisateur.

### Actions à réaliser

1. **Optimiser les requêtes de base de données** :
   - Ajouter des index sur les colonnes fréquemment recherchées
   - Optimiser les jointures
   - Mettre en cache les résultats fréquents

2. **Optimiser la génération d'embeddings** :
   - Batch processing plus efficace
   - Cache des embeddings
   - Parallélisation

3. **Améliorer l'interface Streamlit** :
   - Ajouter des animations de chargement
   - Améliorer le design
   - Ajouter des tooltips d'aide
   - Optimiser les temps de réponse

4. **Ajouter des fonctionnalités** :
   - Export de conversations en PDF
   - Partage de conversations
   - Feedback utilisateur (thumbs up/down)
   - Suggestions automatiques
   - Historique de recherche

5. **Améliorer les prompts** :
   - Tester différentes formulations
   - Ajouter plus de contexte sénégalais
   - Améliorer les réponses pour les cas limites

6. **Créer `config/logging.py`** :
   - Configuration centralisée des logs
   - Rotation des fichiers de logs
   - Niveaux de log par environnement

### Commit
```bash
git add .
git commit -m "perf: optimize performance and enhance user experience"
```